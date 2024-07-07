from customtkinter import *
import random

class Coinflip(CTkFrame):
    def __init__(self, root, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.label = CTkLabel(self, text="Coinflip")
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.interface_apuesta_cash()

        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)

    def interface_apuesta_cash(self):
        self.label_apuesta = CTkLabel(self, text="Apuesta:")
        self.label_apuesta.place(relx=0.5, rely=0.3, anchor="center")

        self.entry_apuesta = CTkEntry(self, placeholder_text="$")
        self.entry_apuesta.place(relx=0.5, rely=0.4, anchor="center")

        self.boton_enviar = CTkButton(self, text="----->", command=self.set_apuesta_cash)
        self.boton_enviar.place(relx=0.5, rely=0.5, anchor="center")

    def set_apuesta_cash(self):
        self.apuesta_cash = self.entry_apuesta.get()
        self.interface_apuesta_coin()

    def interface_apuesta_coin(self):
        self.label_apuesta.destroy()
        self.entry_apuesta.destroy()
        self.boton_enviar.destroy()

        self.boton_cara = CTkButton(self, text="Cara", command=lambda:self.set_apuesta_coin("Cara"), width=120, height=120, font=("Arial", 18))
        self.boton_cara.place(relx=0.45, rely=0.5, anchor="center")

        self.boton_sello = CTkButton(self, text="Sello", command=lambda:self.set_apuesta_coin("Sello"), width=120, height=120, font=("Arial", 18))
        self.boton_sello.place(relx=0.55, rely=0.5, anchor="center") 

    def set_apuesta_coin(self, decision):
        self.decision = decision
        self.flip_coin()

    def flip_coin(self):
        self.label_resultado = CTkLabel(self)

        opciones = ["Cara", "Sello","¡Cayó vertical!"]
        prob = [0.495, 0.495, 0.01]
        result = random.choices(opciones,prob)[0]

        if result == self.decision:
            self.label_resultado.configure(text=f"¡Ganaste!")
        else:
            self.label_resultado.configure(text=f"¡Perdiste!")
        self.label_resultado.place(relx=0.5, rely=0.25, anchor="center")

        self.boton_cara.destroy()
        self.boton_sello.destroy()
        self.boton_enviar = CTkButton(self, text="Reiniciar", command=self.restart)
        self.boton_enviar.place(relx=0.5, rely=0.5, anchor="center")

    def restart(self):
        self.label_resultado.destroy()
        self.boton_enviar.destroy()

        self.interface_apuesta_cash()

    
    