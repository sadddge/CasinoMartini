from functools import partial
import random
from customtkinter import *
from PIL import Image

class Blackjack(CTkFrame):

    def __init__(self, root, user, comando):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.root = root
        self.user = user
        self.comando = comando
        self.cartas = []
        self.valor_dealer = 0
        self.valor_jugador = 0
        self.iniciar_cartas()
        self.start_screen()
        
    def reset(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        
        self.cartas_dealer.clear()
        self.cartas_jugador.clear()
        self.cartas.clear()
        self.valor_dealer = 0
        self.valor_jugador = 0
        self.iniciar_cartas()
        
        self.start_screen()
       
    def start_screen(self):
        
        back = CTkButton(self, text="Back", command=self.comando)
        back.place(x= 30, y= 30)

        self.money_label = CTkLabel(self, text=f"Dinero: ${self.user.money}", font=("Arial Black", 14))
        self.money_label.place(relx=0.9, rely=0.1, anchor="center")

        self.apuesta_entry = CTkEntry(self)
        self.apuesta_entry.place(relx=0.1, rely=0.9, anchor = "w")

        self.apuesta_label = CTkLabel(self, text= "Apuesta:", font=("Arial Black", 14))
        self.apuesta_label.place(relx=0.1, rely=0.85, anchor="w")

        self.jugar_button = CTkButton(self, text="Jugar", command=self.jugar)
        self.jugar_button.place(relx=0.5, rely=0.9, anchor="center")

        self.dealer = CTkLabel(self, text="Dealer", font=("Arial Black", 14))
        self.dealer.place(relx=0.5, rely=0.05, anchor="center")

        self.jugador = CTkLabel(self, text="Jugador", font=("Arial Black", 14))
        self.jugador.place(relx=0.5, rely=0.8, anchor="center")

        random.shuffle(self.cartas)

        
        self.baraja_label = CTkLabel(self, text="")
        self.baraja_label.place(relx=0.8, rely=0.3)

        self.update_baraja()


        self.cartas_dealer = []
        self.cartas_jugador = []

    def jugar(self):
        self.apuesta = int(self.apuesta_entry.get())
        self.apuesta_entry.delete(0, "end")
        

        if self.apuesta > 0:
            self.jugar_button.destroy()
            self.apuesta_entry.destroy()
            self.apuesta_label.configure(text=f"Apuesta: {self.apuesta}")

            self.user.remove_money(self.apuesta)
            self.money_label.configure(text=f"Dinero: ${self.user.money}")
            

            self.hit_button = CTkButton(self, text="Hit", command=self.hit)
            self.hit_button.place(relx=0.4, rely=0.9, anchor="center")
            self.hit_button.configure(state="disabled")

            self.stand_button = CTkButton(self, text="Stand", command=self.stand)
            self.stand_button.place(relx=0.6, rely=0.9, anchor="center")
            self.stand_button.configure(state="disabled")

            self.label_cartas_dealer = CTkLabel(self, text=f"Cartas: {self.valor_dealer}", font=("Arial Black", 14))
            self.label_cartas_dealer.place(relx=0.5, rely=0.1, anchor="center")

            self.label_cartas_jugador = CTkLabel(self, text=f"Cartas: {self.valor_jugador}", font=("Arial Black", 14))
            self.label_cartas_jugador.place(relx=0.5, rely=0.75, anchor="center")

            self.first_hand()


    def first_hand(self):
        first_x = 517.5
        second_x = 650

        for i in range(2):
            x = first_x if i == 0 else second_x
            show = True if i == 0 else False

            carta = self.cartas.pop()
            carta.hide()
            self.cartas_jugador.append(carta)

            self.root.after(500 + 1000*i, self.animate_cartas, x, carta)
            self.root.after(510 + 1000*i, self.update_valores)

            carta = self.cartas.pop()
            carta.hide()
            self.cartas_dealer.append(carta)

            self.root.after(1000 + 1000*i, partial(self.animate_cartas, x, carta, dealer=True, show=show))
            self.root.after(1100 + 1000*i, self.update_valores)

        self.root.after(3000, partial(self.hit_button.configure, state = "normal"))
        self.root.after(3000, partial(self.stand_button.configure, state = "normal"))
        

    def hit(self, dealer = False):
        self.move_cartas(dealer=dealer)

        current_cartas = self.cartas_dealer if dealer else self.cartas_jugador
        carta = self.cartas.pop()
        carta.hide()
        
        card_width = 225/2
        screen_width = 1280
        card_spacing = 20
        n = 1 + len(current_cartas)

        end_x = ((screen_width - card_width*n - card_spacing*(n-1))/2) + (n-1)*(card_width + card_spacing)

        self.animate_cartas(end_x, carta, dealer=dealer)
        self.root.after(500, self.update_valores)

        current_cartas.append(carta)

        self.hit_button.configure(state="disabled")
        self.stand_button.configure(state="disabled")

        if dealer:
            self.root.after(600, self.check_dealer_turn)
        else:
            self.root.after(600, self.check_jugador_turn)

        self.update_baraja()
    
    def stand(self):
        self.hit_button.configure(state="disabled")
        self.stand_button.configure(state="disabled")
        
        self.cartas_dealer[1].show()
        self.update_valores()
        self.check_dealer_turn()
           
    def end_game(self, winner):
        if winner == "jugador":
            text = f"Ganaste ${self.apuesta*2}!"
            self.user.add_money(self.apuesta*2)
        elif winner == "dealer":
            text = "Perdiste!"
        else:
            text = "Empate!"
            self.user.add_money(self.apuesta)

        self.money_label.configure(text=f"Dinero: ${self.user.money}")

        winner_label = CTkLabel(self, text=text, fg_color=None, font=("Arial Black", 14))
        winner_label.place(relx=0.5, y = 295, anchor="center")

        self.hit_button.destroy()
        self.stand_button.destroy()
        self.reset_button = CTkButton(self, text="Reset", command=self.reset)
        self.reset_button.place(relx=0.5, rely=0.9, anchor="center")

        
    
    def move_cartas(self, dealer = False):
        card_width = 225/2
        screen_width = 1280
        card_spacing = 20

        cartas = self.cartas_dealer if dealer else self.cartas_jugador

        n = 1 + len(cartas)

        end_x = (screen_width - card_width*n - card_spacing*(n-1))/2

        for i, carta in enumerate(cartas):
            x = carta.winfo_x()
            y = carta.winfo_y()
            self.animate_cartas(end_x + i*(card_width + card_spacing), carta, x, y, dealer=dealer)

    def animate_cartas(self,
                       end_x,
                       carta,
                       x = 1025,
                       y = 215,
                       dealer = False,
                       show = True):

        end_y_dealer = 110
        end_y_jugador = 325

        end_y = end_y_dealer if dealer else end_y_jugador

        vel = 10

        dx = vel if x < end_x else -vel
        dy = vel if y < end_y else -vel

        carta.place(x=x, y=y)

        if x == end_x and y == end_y:
            if show:
                carta.show()
            return

        x = x + dx
        y = y + dy

        if abs(x - end_x) <= 15:
            x = end_x
        
        if abs(y - end_y) <= 15:
            y = end_y
        
        
        self.root.after(10, self.animate_cartas, end_x, carta, x, y, dealer, show)
    

    def check_dealer_turn(self):

        if isinstance(self.valor_dealer, list):
            valor = max(self.valor_dealer)
        else: valor = self.valor_dealer

        if isinstance(self.valor_jugador, list):
            valor_jugador = max(self.valor_jugador)
        else: valor_jugador = self.valor_jugador

    
        if valor < 17:
            print("dealer hit")
            self.root.after(500, partial(self.hit, dealer=True))
        elif valor > 21:
            self.end_game("jugador")
        elif valor_jugador > valor:
            self.end_game("jugador")
        elif valor_jugador < valor:
            self.end_game("dealer")
        else: self.end_game("empate")

    def check_jugador_turn(self):
        self.hit_button.configure(state="normal")
        self.stand_button.configure(state="normal")
        if isinstance(self.valor_jugador, list):
            valor = max(self.valor_jugador)
        else: valor = self.valor_jugador

        if valor > 21:
            self.end_game("dealer")
        

    def valor_cartas(self, cartas):
        valor = 0
        if self.check_as(cartas):
            valor = [0,0]
            for carta in cartas:
                if carta.hiden:
                    continue

                if carta.num == 1:
                    valor[0] += 1
                    valor[1] += 11
                else:
                    valor[0] += carta.valor
                    valor[1] += carta.valor

            if valor[0] > 21 or valor[1] > 21:
                return min(valor)
            
        else:
            for carta in cartas:
                if carta.hiden:
                    continue
                valor += carta.valor



        return valor

    def check_as(self, cartas):
        for carta in cartas:
            if carta.num == 1 and carta.hiden == False:
                return True
        return False

    def iniciar_cartas(self):
        ancho_carta = 225
        alto_carta = 315
        filas = 4
        columnas = 13
        carta = Image.open("resources/cartas.png")
        red = Image.open("resources/red.png")
        blue = Image.open("resources/blue.png")

        red_reverso = CTkImage(light_image=red, size=(ancho_carta/2, alto_carta/2))
        blue_reverso = CTkImage(light_image=blue, size=(ancho_carta/2, alto_carta/2))

        for fila in range(filas):
            for columna in range(columnas):

                reverso = red_reverso if fila % 2 == 0 else blue_reverso

                x = columna * ancho_carta
                y = fila * alto_carta
                carta_cortada = carta.crop((x, y, x + ancho_carta, y + alto_carta))
                
                image = CTkImage(light_image=carta_cortada, size=(ancho_carta/2, alto_carta/2))
                self.cartas.append(Carta(self, columna + 1, image=image, image_reverse=reverso))
            
    def update_baraja(self):
        image = self.cartas[len(self.cartas)-1].image_reverse
        self.baraja_label.configure(image=image)
    
    def update_valores(self):
        self.valor_dealer = self.valor_cartas(self.cartas_dealer)
        self.valor_jugador = self.valor_cartas(self.cartas_jugador)
        self.label_cartas_dealer.configure(text=f"Cartas: {self.valor_dealer}")
        self.label_cartas_jugador.configure(text=f"Cartas: {self.valor_jugador}")


class Carta(CTkLabel):

    def __init__(self, root, num, image, image_reverse):
        super().__init__(root, image=image, text="", fg_color= "transparent")
        self.image_reverse =image_reverse
        self.image = image
        self.hiden = False
        self.num = num
        self.valor = 0
        self.set_valor()

    def set_valor(self):
        if self.num > 10:
            self.valor = 10
        else:
            self.valor = self.num

    def hide(self):
        self.configure(image=self.image_reverse)
        self.hiden = True

    def show(self):
        self.configure(image=self.image)
        self.hiden = False

