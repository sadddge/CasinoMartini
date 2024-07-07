from customtkinter import *
from PIL import Image
import random

class Dados(CTkFrame):
    def __init__(self, root, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.comando = comando
        self.label = CTkLabel(self, text="Dados")
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        self.start_apuesta(comando)

        

    def start_apuesta(self, comando):
        self.label_mj = CTkLabel(self, text="Apuesta:")
        self.label_mj.place(relx=0.5, rely=0.4, anchor="center")

        self.apuesta_entry = CTkEntry(self)
        self.apuesta_entry.place(relx=0.5, rely=0.4625, anchor="center")

        self.enviar = CTkButton(self, text="----->", command=self.modos_de_juego)
        self.enviar.place(relx=0.5, rely=0.525, anchor="center")

        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)

    def modos_de_juego(self):
        self.apuesta_cash = self.apuesta_entry.get()

        self.apuesta_entry.destroy()
        self.enviar.destroy()

        self.label_mj.configure(text="Modos de juego:")

        self.label_mj_1 = CTkButton(self, text="Numero del dado", command=lambda: self.pre_set_dados("numero"))
        self.label_mj_1.place(relx=0.425, rely=0.5, anchor="center")

        self.label_mj_2 = CTkButton(self, text="Suma de los dados", command=lambda: self.pre_set_dados("suma"))
        self.label_mj_2.place(relx=0.575, rely=0.5, anchor="center")

    def pre_set_dados(self, modo_de_juego):
        self.modo_de_juego = modo_de_juego

        self.label_mj_1.destroy()
        self.label_mj_2.destroy()

        if self.modo_de_juego == "numero":
            self.label_mj.configure(text="Cantidad de dados (1-4):")
        else:
            self.label_mj.configure(text="Cantidad de dados (2-4):")

        self.entry = CTkEntry(self)
        self.entry.place(relx=0.5, rely=0.4625, anchor="center")

        self.enviar = CTkButton(self, text="----->", command=self.set_dados)
        self.enviar.place(relx=0.5, rely=0.525, anchor="center")

    def set_dados(self):
        self.dados = self.entry.get()
        self.entry.delete(0, "end")
        

        if self.modo_de_juego == "numero":
            if self.dados in ["1", "2", "3", "4"]:
                self.label_mj.configure(text="Número del dado a apostar:")
                self.pre_set_apuesta_dado() 
            else:
                self.label_mj.configure(text="¡Cantidad de dados no válida!, Elige la cantidad de dados (1-4):")      
        else:
            if self.dados in ["2", "3", "4"]:
                self.rango = f"({1*self.dados}-{6*int(self.dados)})"
                self.label_mj.configure(text=f"Suma de los dados a apostar {self.rango}:")
                self.pre_set_apuesta_dado()
            else:
                self.label_mj.configure(text="¡Cantidad de dados no válida!, Elige la cantidad de dados (2-4):")
        
    def pre_set_apuesta_dado(self):
        
        if self.modo_de_juego == "numero":
            self.entry.destroy()
            self.lista_entrys = []
            start_x = (1280-35*int(self.dados)-30*(int(self.dados)-1))/2
            self.enviar.configure(command=self.set_apuesta_dado)
            for i in range(int(self.dados)):
                self.lista_entrys.append(CTkEntry(self, width=35, height=35, placeholder_text=f"D{i+1}"))
                self.lista_entrys[i].place(x=start_x+65*i, rely=0.4325)
        else:
            self.enviar.configure(command=self.set_apuesta_dado)

    def set_apuesta_dado(self):
        correcto = True
        self.lista_apuestas_dados = []
        if self.modo_de_juego == "numero":
            for entry in self.lista_entrys:
                apuesta_dado = entry.get()
                if apuesta_dado not in ["1", "2", "3", "4", "5", "6"]:
                    self.label_mj.configure(text=f"¡El dado {entry.cget("placeholder_text")} no es válido!, Elige el número del dado a apostar (1-6):")
                    correcto = False
                    for entry in self.lista_entrys:
                        entry.delete(0, "end")
                    break
                self.lista_apuestas_dados.append(apuesta_dado)
            if correcto:
                self.mj_numero_dados()      
        else:
            self.apuesta_dados = self.entry.get()
            self.posibles_resultados = list(range(1*int(self.dados), 6*int(self.dados)+1))
            if int(self.apuesta_dados) in self.posibles_resultados:
                self.mj_suma_dados()
            else:
                self.label_mj.configure(text=f"¡Número no válido!, (Suma de los dados {self.rango}:")
            self.entry.delete(0, "end")

    def mj_numero_dados(self):
        resultado = "Resultado:"
        self.enviar.configure(text="Reiniciar",command=self.restart)
        
        

        self.lista_labels_result = []
        start_x = (1280-100*int(self.dados)-100*(int(self.dados)-1))/2
        
        lista_dados_random = []
        for entry in self.lista_entrys:
            i = self.lista_entrys.index(entry)
            dado_random = random.randint(1, 6)
            lista_dados_random.append(dado_random)

        
        for entry in self.lista_entrys:
            entry.destroy()
        
        for i in range(int(self.dados)):
            self.lista_labels_result.append(CTkLabel(self, text=f"Dado ganador D{i+1}: {lista_dados_random[i]}\nTu apuesta: {self.lista_apuestas_dados[i]}"))
            self.lista_labels_result[i].place(x=start_x+200*i, rely=0.4325)
        
        if self.lista_apuestas_dados == lista_dados_random:
            resultado += "\n¡Ganaste!"
        
        self.label_mj.configure(text=f"{resultado}")
        
            

    def mj_suma_dados(self):
        self.enviar.configure(text="Reiniciar",command=self.restart)
        green_check = Image.open("resources/green_check.png")
        red_x = Image.open("resources/red_x.png")

        suma_dados_random = random.randint(1*int(self.dados), 6*int(self.dados))
        resultado = f"Resultado: {suma_dados_random}\nTu apuesta: {self.apuesta_dados}\n"
        if int(self.apuesta_dados) == suma_dados_random:
            resultado_img = green_check
        else:
            resultado_img = red_x
        self.label_mj.configure(text=f"{resultado}")
        self.label_img = CTkLabel(self, image=CTkImage(light_image=resultado_img, dark_image=resultado_img, size=(30,30)), width=40, height=40)
        

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy() 

    def restart(self):
        self.clear_screen()
        self.start_apuesta(self.comando)
           
    
        