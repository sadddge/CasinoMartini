import random
from customtkinter import *
class Blackjack(CTkFrame):

    def __init__(self, root, comando):
        super().__init__(root)
        self.pack(fill="both", expand=True)
        self.root = root
        self.screen()

        self.cartas = []


        back = CTkButton(self, text="Back", command=comando)
        back.pack(side="bottom")

    def screen(self):
        self.entry = CTkEntry(self)
        self.entry.place(relx=0.5, rely=0.5, anchor="center")

        self.start = CTkButton(self, text="Start", command=self.start_game)
        self.start.place(relx=0.5, rely=0.6, anchor="center")

    def start_game(self):
        self.apuesta = self.entry.get()
        self.entry.destroy()
        self.start.destroy()

        self.label = CTkLabel(self, text=f"Apuesta: {self.apuesta}")
        self.label.place(relx=0.5, rely=0.9, anchor="center")

        self.iniciar_cartas()

        self.cartas_dealer = []
        self.cartas_jugador = []

        self.dealer = CTkLabel(self, text="Dealer")
        self.dealer.place(relx=0.5, rely=0.1, anchor="center")

        self.jugador = CTkLabel(self, text="Jugador")
        self.jugador.place(relx=0.5, rely=0.8, anchor="center")

        random.shuffle(self.cartas)
        self.cartas_dealer.append(self.cartas.pop())
        self.cartas_jugador.append(self.cartas.pop())
        self.cartas_dealer.append(self.cartas.pop())
        self.cartas_jugador.append(self.cartas.pop())


        self.valor_dealer = self.valor_cartas(self.cartas_dealer)
        self.valor_jugador = self.valor_cartas(self.cartas_jugador)


        self.label_dealer = CTkLabel(self, text=f"Cartas: {self.valor_dealer}")
        self.label_dealer.place(relx=0.5, rely=0.2, anchor="center")

        self.label_jugador = CTkLabel(self, text=f"Cartas: {self.valor_jugador}")
        self.label_jugador.place(relx=0.5, rely=0.7, anchor="center")

        self.hit = CTkButton(self, text="Hit", command=self.hit)
        self.hit.place(relx=0.5, rely=0.5, anchor="center")

        self.stand = CTkButton(self, text="Stand", command=self.stand)
        self.stand.place(relx=0.5, rely=0.6, anchor="center")

    
    def hit(self):
        self.cartas_jugador.append(self.cartas.pop())
        self.valor_jugador = self.valor_cartas(self.cartas_jugador)
        self.label_jugador.configure(text=f"Cartas: {self.valor_jugador}")

    def stand(self):
        while self.valor_dealer < 17:
            self.cartas_dealer.append(self.cartas.pop())
            self.valor_dealer = self.valor_cartas(self.cartas_dealer)
            self.label_dealer.configure(text=f"Cartas: {self.valor_dealer}")

        if self.valor_dealer > 21:
            self.label_dealer.configure(text="Dealer Pierde")
        elif self.valor_dealer > self.valor_jugador:
            self.label_dealer.configure(text="Dealer Gana")
        elif self.valor_dealer < self.valor_jugador:
            self.label_dealer.configure(text="Jugador Gana")
        else:
            self.label_dealer.configure(text="Empate")


    def valor_cartas(self, cartas):
        valor = 0
        for carta in cartas:
            valor += carta[2]
        return valor

    def iniciar_cartas(self):
        for i in range(4):
            for j in range(13):
                if j+1 > 10:
                    valor = 10
                else:
                    valor = j+1

                match i:
                    case 0:
                        self.cartas.append((j+1, "Corazones", valor))
                    case 1:
                        self.cartas.append((j+1, "Diamantes", valor))
                    case 2:
                        self.cartas.append((j+1, "Picas", valor))
                    case 3:
                        self.cartas.append((j+1, "Treboles", valor))



