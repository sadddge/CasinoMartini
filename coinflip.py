from customtkinter import *
import random

class Coinflip(CTkFrame):
    def __init__(self, root, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.label = CTkLabel(self, text="Coinflip")
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.heads = CTkButton(self, text="Cara", command=lambda:self.set_decision("Cara"))
        self.heads.place(relx=0.5, rely=0.3, anchor="center")

        self.tails = CTkButton(self, text="Sello", command=lambda:self.set_decision("Sello"))
        self.tails.place(relx=0.5, rely=0.4, anchor="center")

        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)

    def set_decision(self, decision):
        self.decision = decision
        self.flip_coin()

    def flip_coin(self):
        opciones = ["Cara", "Sello","¡Cayó vertical!"]
        prob = [0.495, 0.495, 0.01]
        result = random.choices(opciones,prob)[0]
        if result == self.decision:
            self.label.configure(text=f"¡Ganaste! El resultado fue {result}")
        else:
            self.label.configure(text=f"¡Perdiste! El resultado fue {result}")


    