from customtkinter import *
from PIL import Image
import random

class Coinflip(CTkFrame):
    def __init__(self, root, user, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.root = root

        self.user = user

        self.font = ("Arial Black", 14)

        self.interface_apuesta_cash()
        self.init_images()


        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)

    def init_images(self):
        image = Image.open("resources/sello.png")
        self.sello_image = CTkImage(light_image=image, size=(300, 300))

        image = Image.open("resources/cara.png")
        self.cara_image = CTkImage(light_image=image, size=(300, 300))

        image = Image.open("resources/sello_half.png")
        self.sello_half_image = CTkImage(light_image=image, size=(300, 300))

        image = Image.open("resources/cara_half.png")
        self.cara_half_image = CTkImage(light_image=image, size=(300, 300))

        image = Image.open("resources/half.png")
        self.half_image = CTkImage(light_image=image, size=(300, 300))

    def interface_apuesta_cash(self):

        self.win_label = CTkLabel(self, text="Dinero: $"+str(self.user.money), font=self.font)
        self.win_label.place(relx=0.85, rely=0.1, anchor="center")

        self.label_apuesta = CTkLabel(self, text="Apuesta:", font=self.font)
        self.label_apuesta.place(relx=0.15, rely=0.35, anchor="center")

        self.entry_apuesta = CTkEntry(self, placeholder_text="$")
        self.entry_apuesta.place(relx=0.15, rely=0.4, anchor="center")

        self.boton_cara = CTkButton(self, text="Cara", command=lambda:self.set_apuesta_coin("Cara"), width=65)
        self.boton_cara.place(relx=0.12, rely=0.45, anchor="center")

        self.boton_sello = CTkButton(self, text="Sello", command=lambda:self.set_apuesta_coin("Sello"), width=65)
        self.boton_sello.place(relx=0.18, rely=0.45, anchor="center")

        self.boton_enviar = CTkButton(self, text="----->", command=lambda:self.set_apuesta(self.entry_apuesta.get()))

        self.label_image = CTkLabel(self, text="")
        self.label_image.place(relx=0.5, rely=0.5, anchor="center")

    def set_apuesta_coin(self, decision):
        self.decision = decision
        
        if self.decision == "Cara":
            self.boton_cara.configure(fg_color="green")
            self.boton_sello.configure(fg_color="dodgerblue3")
        else:
            self.boton_sello.configure(fg_color="green")
            self.boton_cara.configure(fg_color="dodgerblue3")

        self.boton_enviar.place(relx=0.15, rely=0.5, anchor="center")

    def animate(self, imag, time = 0):
        if time > 4:
            self.flip_coin()
            return

        if imag > 8:
            imag = 1
        
        match imag:
            case 1:
                self.label_image.configure(image=self.cara_image)
            case 2:
                self.label_image.configure(image=self.cara_half_image)
            case 3:
                self.label_image.configure(image=self.half_image)
            case 4:
                self.label_image.configure(image=self.sello_half_image)
            case 5:
                self.label_image.configure(image=self.sello_image)
            case 6:
                self.label_image.configure(image=self.sello_half_image)
            case 7:
                self.label_image.configure(image=self.half_image)
            case 8:
                self.label_image.configure(image=self.cara_half_image)

        self.root.after(100, self.animate, imag+1, time+0.1)

    def set_apuesta(self, cash):
        self.apuesta_cash = cash
        self.user.remove_money(int(self.apuesta_cash))
        self.win_label.configure(text="Dinero: $"+str(self.user.money))
        self.animate(1)

    def flip_coin(self):
        self.label_resultado = CTkLabel(self, font=self.font)

        opciones = ["Cara", "Sello","¡Cayó vertical!"]
        prob = [0.495, 0.495, 0.01]
        result = random.choices(opciones,prob)[0]

        match result:
            case "Cara":
                self.label_image.configure(image=self.cara_image)
            case "Sello":
                self.label_image.configure(image=self.sello_image)
            case "¡Cayó vertical!":
                self.label_image.configure(image=self.half_image)

        if result == self.decision:
            self.label_resultado.configure(text=f"¡Ganaste!")
            self.user.add_money(int(self.apuesta_cash)*2)
            self.win_label.configure(text="Dinero: $"+str(self.user.money))
        else:
            self.label_resultado.configure(text=f"¡Perdiste!")
        self.label_resultado.place(relx=0.5, rely=0.2, anchor="center")

        if result == "¡Cayó vertical!":
            self.label_resultado.configure(text="¡Perdiste! Cayó vertical :c")

        self.boton_cara.configure(state="normal")
        self.boton_sello.configure(state="normal")

            



    
    