from customtkinter import *
from PIL import Image
import random

class Mines(CTkFrame):
    def __init__(self, root, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.label = CTkLabel(self, text="Mines")
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        self.multiplier = 1.0
        self.hits = 0

        self.main_interface()

        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)
    
    def main_interface(self):
        self.label_apuesta = CTkLabel(self, text="Apuesta:")
        self.label_apuesta.place(relx=0.15, rely=0.3, anchor="center")

        self.label_multiplier = CTkLabel(self, text=f"Multiplicador: {self.multiplier}x")
        self.label_multiplier.place(relx=0.5, rely=0.2, anchor="center")

        self.entry_apuesta_cash = CTkEntry(self, placeholder_text="$")
        self.entry_apuesta_cash.place(relx=0.15, rely=0.35, anchor="center")

        self.label_num_mines = CTkLabel(self, text="Cantidad de minas:")
        self.label_num_mines.place(relx=0.15, rely=0.4, anchor="center")

        num_mines = [str(i) for i in range(1, 25)]
        self.optionmenu_num_mines = CTkOptionMenu(self, values=num_mines, width=10)
        self.optionmenu_num_mines.place(relx=0.15, rely=0.45, anchor="center")

        self.boton_enviar = CTkButton(self, text="Start", command=self.start_game)
        self.boton_enviar.place(relx=0.15, rely=0.52, anchor="center")

        self.place_buttons()
        
    def create_minefield(self):
        self.minefield = [[0 for _ in range(5)] for _ in range(5)]
        self.minefield = self.set_minefield(self.minefield, self.mines)
            
        self.place_buttons()

    def place_buttons(self):
        self.minefield_buttons = [[None for _ in range(5)] for _ in range(5)]

        for row in range(5):
            for col in range(5):
                x = (1280/2)-140 + col*70
                y = (720/2)-140 + row*70
                button = CTkButton(self, text="",
                                    width=60, 
                                    height=60, 
                                    command=lambda row=row, col=col: self.click_minefield(row, col), 
                                    corner_radius=5, 
                                    state="disabled", 
                                    fg_color="#284b78")
                button.place(x=x, y=y, anchor="center")
                self.minefield_buttons[row][col] = button

    def start_game(self):
        self.mines = int(self.optionmenu_num_mines.get())
        self.apuesta_cash = self.entry_apuesta_cash.get()
        self.create_minefield()
        for col in range(5):
            for row in range(5):
                self.minefield_buttons[row][col].configure(state="normal", fg_color="#3470bd")

    def set_minefield(self, minefield, mines):
        for _ in range(int(mines)):
            while True:
                row = random.randint(0, 4)
                col = random.randint(0, 4)
                if minefield[row][col] != -1:
                    minefield[row][col] = -1
                    break
        return minefield
    
    def update_multiplier(self):
        self.not_mines = int(25-self.mines)
        p = 1/self.multiplier
        p *= ((self.not_mines-self.hits)/(25-self.hits))
        self.multiplier = round(1/p,2)
        self.label_multiplier.configure(text=f"Multiplicador: {self.multiplier}x")   

    def click_minefield(self, row, col):
        if self.minefield[row][col] == -1:
            self.game_over()
        else:
            self.update_multiplier()
            self.hits += 1
            self.minefield_buttons[row][col].configure(state="disabled", fg_color="#37b244")

    def game_over(self):
        for row in range(5):
            for col in range(5):
                self.minefield_buttons[row][col].configure(state="disabled")
                if self.minefield[row][col] == -1:
                    self.minefield_buttons[row][col].configure(fg_color="#b93737")
                elif self.minefield_buttons[row][col].cget("fg_color") != "#37b244":
                    self.minefield_buttons[row][col].configure(fg_color="#284b78")
    
