from functools import partial
import random
import time
from customtkinter import *
from PIL import Image

class Blackjack(CTkFrame):

    def __init__(self, root, comando):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.root = root
        self.comando = comando
        self.cartas = []
        self.valor_dealer = 0
        self.valor_jugador = 0
        self.iniciar_cartas()
        self.start_screen()
        

        
    def start_screen(self):
        
        back = CTkButton(self, text="Back", command=self.comando)
        back.place(x= 30, y= 30)

        self.apuesta_entry = CTkEntry(self)
        self.apuesta_entry.place(relx=0.1, rely=0.9, anchor = "w")

        self.apuesta_label = CTkLabel(self, text= "Apuesta:")
        self.apuesta_label.place(relx=0.1, rely=0.85, anchor="w")

        self.jugar_button = CTkButton(self, text="Jugar", command=self.jugar)
        self.jugar_button.place(relx=0.5, rely=0.9, anchor="center")

        self.dealer = CTkLabel(self, text="Dealer")
        self.dealer.place(relx=0.5, rely=0.05, anchor="center")

        self.jugador = CTkLabel(self, text="Jugador")
        self.jugador.place(relx=0.5, rely=0.8, anchor="center")

        random.shuffle(self.cartas)

        
        self.baraja_label = CTkLabel(self, text="")
        self.baraja_label.place(relx=0.8, rely=0.3)

        self.update_baraja()


        self.cartas_dealer = []
        self.cartas_jugador = []


    def reset(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.cartas_dealer.clear()
        self.cartas_jugador.clear()
        self.cartas.clear()
        self.iniciar_cartas()
        
        self.start_screen()

    def jugar(self):
        self.apuesta = int(self.apuesta_entry.get())
        self.apuesta_entry.delete(0, "end")

        if self.apuesta > 0:
            self.jugar_button.destroy()
            self.apuesta_entry.destroy()
            self.apuesta_label.configure(text=f"Apuesta: {self.apuesta}")
            

            self.hit_button = CTkButton(self, text="Hit", command=self.hit)
            self.hit_button.place(relx=0.4, rely=0.9, anchor="center")

            self.stand_button = CTkButton(self, text="Stand", command=self.stand)
            self.stand_button.place(relx=0.6, rely=0.9, anchor="center")

            self.label_dealer = CTkLabel(self, text=f"Cartas: {self.valor_dealer}")
            self.label_dealer.place(relx=0.5, rely=0.1, anchor="center")

            self.label_jugador = CTkLabel(self, text=f"Cartas: {self.valor_jugador}")
            self.label_jugador.place(relx=0.5, rely=0.75, anchor="center")

            self.first_hand()

        
    def update_baraja(self):
        image = self.cartas[len(self.cartas)-1].image_reverse
        self.baraja_label.configure(image=image)

    def first_hand(self):
        first_x = 517.5
        second_x = 650


        carta = self.cartas.pop()
        carta.hide()
        self.cartas_jugador.append(carta)
        self.root.after(500, self.animate_cartas, first_x, carta)

        carta = self.cartas.pop()
        carta.hide()
        self.cartas_dealer.append(carta)
        self.root.after(1000, partial(self.animate_cartas, first_x, carta, dealer=True))

        carta = self.cartas.pop()
        carta.hide()
        self.cartas_jugador.append(carta)
        self.root.after(1500, self.animate_cartas, second_x, carta)

        carta = self.cartas.pop()
        carta.hide()
        self.cartas_dealer.append(carta)
        self.root.after(2000, partial(self.animate_cartas, second_x, carta, dealer=True, show=False))

        self.root.after(2500, self.update_valores)


    def update_valores(self):
        self.valor_dealer = self.valor_cartas(self.cartas_dealer)
        self.valor_jugador = self.valor_cartas(self.cartas_jugador)
        self.label_dealer.configure(text=f"Cartas: {self.valor_dealer}")
        self.label_jugador.configure(text=f"Cartas: {self.valor_jugador}")

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
    

    def hit(self, dealer = False):
        
        self.move_cartas(dealer=dealer)

        cartas = self.cartas_dealer if dealer else self.cartas_jugador
        carta = self.cartas.pop()
        carta.hide()
        
        card_width = 225/2
        screen_width = 1280
        card_spacing = 20
        n = 1 + len(cartas)

        end_x = ((screen_width - card_width*n - card_spacing*(n-1))/2) + (n-1)*(card_width + card_spacing)

        self.animate_cartas(end_x, carta, dealer=dealer)
        
        
        if dealer:
            self.cartas_dealer.append(carta)
        else:
            self.cartas_jugador.append(self.cartas.pop())
            if self.valor_jugador > 21:
                self.label_jugador.configure(text="Perdiste")
                self.hit_button.destroy()
                self.stand_button.destroy()

                self.reset_button = CTkButton(self, text="Reset", command=self.reset)
                self.reset_button.place(relx=0.5, rely=0.9, anchor="center")
        
        self.root.after(500, self.update_valores)

    def stand(self):
        self.hit_button.configure(state="disabled")
        if self.valor_dealer < 17:
            self.hit(dealer=True)
            self.root.after(1000, self.stand)
        else:
            if self.valor_dealer > 21 or self.valor_jugador > self.valor_dealer:
                self.label_dealer.configure(text="Ganaste")
            elif self.valor_dealer > self.valor_jugador:
                self.label_dealer.configure(text="Perdiste")
            else:
                self.label_dealer.configure(text="Empate")

            self.hit_button.destroy()
            self.stand_button.destroy()

            self.reset_button = CTkButton(self, text="Reset", command=self.reset)
            self.reset_button.place(relx=0.5, rely=0.9, anchor="center")
            


    def valor_cartas(self, cartas):
        valor = 0
        for carta in cartas:
            if carta.hiden == False:  
                valor += carta.valor
        return valor

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

