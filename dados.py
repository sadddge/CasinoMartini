from customtkinter import *
import random

class Dados(CTkFrame):
    def __init__(self, root, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.label = CTkLabel(self, text="Dados")
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.label_entry = CTkLabel(self, text="Elige la cantidad de dados (1-3):")
        self.label_entry.place(relx=0.5, rely=0.2, anchor="center")

        self.entry = CTkEntry(self)
        self.entry.place(relx=0.5, rely=0.25, anchor="center")

        self.enviar = CTkButton(self, text="Comenzar", command=self.set_dados)
        self.enviar.place(relx=0.5, rely=0.3, anchor="center")

        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)

    def set_dados(self):
        self.dados = self.entry.get()
        self.entry.delete(0, "end")
        if self.dados in ["1", "2", "3"]:
            self.rango = f"{1*self.dados}-{6*int(self.dados)}"
            self.label_entry.configure(text=f"Numero a apostar (Suma de los dados {self.rango}):")
            self.enviar.configure(text="Tirar dados", command=self.tirar_dados)
        else:
            self.label_entry.configure(text="¡Cantidad de dados no válida!, Elige la cantidad de dados (1-3):")


    def tirar_dados(self):
        posibles_resultados = list(range(1*int(self.dados), 6*int(self.dados)+1))
        
        if int(self.entry.get()) in posibles_resultados:
            suma = 0
            for i in range(int(self.dados)):
                opciones = ["1", "2", "3", "4", "5", "6"]
                result = random.choice(opciones)
                suma += int(result)
            
            if suma == int(self.entry.get()):
                self.label_entry.configure(text="¡Ganaste!")
            else:
                self.label_entry.configure(text=f"¡Perdiste!, la suma de los dados fue: {suma}")
        else:
            self.label_entry.configure(text=f"¡Número no válido!, (Suma de los dados {self.rango}):")
        
        self.entry.delete(0, "end")
                

        