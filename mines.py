from customtkinter import *
from PIL import Image
import random

class Mines(CTkFrame):
    def __init__(self, root: CTk, comando):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.open_imgs()
        self.label = CTkLabel(self, text="Mines")
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        self.multiplier = 1.0
        self.hits = 0

        self.interface_apuesta_cash()

        self.back = CTkButton(self, text="<-----", command=comando, width=50)
        self.back.place(x=30, y=30)
        
    def interface_apuesta_cash(self):
        self.label_apuesta = CTkLabel(self, text="Apuesta:")
        self.label_apuesta.place(relx=0.5, rely=0.3, anchor="center")

        self.entry_apuesta_cash = CTkEntry(self, placeholder_text="$")
        self.entry_apuesta_cash.place(relx=0.5, rely=0.4, anchor="center")

        self.boton_enviar = CTkButton(self, text="----->", command=self.set_apuesta_cash)
        self.boton_enviar.place(relx=0.5, rely=0.5, anchor="center")
    
    def set_apuesta_cash(self):
        self.apuesta_cash = self.entry_apuesta_cash.get()
        self.interface_select_minefield_size()

    def interface_select_minefield_size(self):
        self.label_apuesta.destroy()
        self.entry_apuesta_cash.destroy()
        self.boton_enviar.destroy()

        self.label_mines = CTkLabel(self, text="Selecciona el tamaño del campo de minas:")
        self.label_mines.place(relx=0.5, rely=0.4, anchor="center")

        self.button_minefield_3x3 = CTkButton(self, text="3x3", command=lambda: self.set_minefield_size(3), width=80, height=80)
        self.button_minefield_3x3.place(relx=0.4, rely=0.5, anchor="center")

        self.button_minefield_4x4 = CTkButton(self, text="4x4", command=lambda: self.set_minefield_size(4), width=80, height=80)
        self.button_minefield_4x4.place(relx=0.5, rely=0.5, anchor="center")

        self.button_minefield_5x5 = CTkButton(self, text="5x5", command=lambda: self.set_minefield_size(5), width=80, height=80)
        self.button_minefield_5x5.place(relx=0.6, rely=0.5, anchor="center")

    def set_minefield_size(self, side):
        self.side = side
        self.total_cells = side*side
        self.interface_select_mines()

    def interface_select_mines(self):
        self.label_mines.destroy()
        self.button_minefield_3x3.destroy()
        self.button_minefield_4x4.destroy()
        self.button_minefield_5x5.destroy()

        self.label_select_mines = CTkLabel(self, text="Selecciona la cantidad de minas:")
        self.label_select_mines.place(relx=0.5, rely=0.3, anchor="center")

        self.label_num_mines_selected = CTkLabel(self, text="1")
        self.label_num_mines_selected.place(relx=0.5, rely=0.35, anchor="center")

        self.slide_select_mines = CTkSlider(self, from_=1, to=self.total_cells-1, command=self.sliding)
        self.slide_select_mines.place(relx=0.5, rely=0.4, anchor="center")
        self.slide_select_mines.set(1)

        self.button_half_mines = CTkButton(self, text="1/2", command=lambda:self.quick_buttons_mines(2), width=80)
        self.button_half_mines.place(relx=0.4, rely=0.5, anchor="center")

        self.button_third_mines = CTkButton(self, text="1/3", command=lambda:self.quick_buttons_mines(3), width=80)
        self.button_third_mines.place(relx=0.5, rely=0.5, anchor="center")

        self.button_quarter_mines = CTkButton(self, text="1/4", command=lambda:self.quick_buttons_mines(4), width=80)
        self.button_quarter_mines.place(relx=0.6, rely=0.5, anchor="center")

        self.boton_enviar_mines = CTkButton(self, text="----->", command=self.set_mines)
        self.boton_enviar_mines.place(relx=0.5, rely=0.6, anchor="center")

    def sliding(self, value):
        self.label_num_mines_selected.configure(text=int(value))

    def quick_buttons_mines(self, divisor):
        value = self.total_cells//divisor
        self.slide_select_mines.set(value)
        self.sliding(value)

    def set_mines(self):
        self.mines = self.slide_select_mines.get()
        self.interface_game()

    def interface_game(self):
        self.label_select_mines.destroy()
        self.label_num_mines_selected.destroy()
        self.slide_select_mines.destroy()
        self.button_half_mines.destroy()
        self.button_third_mines.destroy()
        self.button_quarter_mines.destroy()
        self.boton_enviar_mines.destroy()

        self.minefield = [[0 for _ in range(self.side)] for _ in range(self.side)]
        self.minefield = self.set_minefield(self.minefield, self.mines)
        self.minefield_buttons = [[None for _ in range(self.side)] for _ in range(self.side)]
        self.interface_minefield()

    def set_minefield(self, minefield, mines):
        for _ in range(int(mines)):
            while True:
                row = random.randint(0, self.side-1)
                col = random.randint(0, self.side-1)
                if minefield[row][col] != -1:
                    minefield[row][col] = -1
                    break
        return minefield
    
    def update_multiplier(self):
        self.not_mines = int(self.total_cells-self.mines)
        p = 1/self.multiplier
        p *= ((self.not_mines-self.hits)/(self.total_cells-self.hits))
        self.multiplier = round(1/p,2)
        self.label_multiplier.configure(text=f"Multiplicador: {self.multiplier}x")

    def interface_minefield(self):
        self.set_axis()
        self.label_minesweeper = CTkLabel(self, text="Campo de minas")
        self.label_minesweeper.place(relx=0.5, rely=0.1, anchor="center")

        self.label_multiplier = CTkLabel(self, text=f"Multiplicador: {self.multiplier}x")
        self.label_multiplier.place(relx=0.5, rely=0.2, anchor="center")
        self.list_labels_mines = [[None for _ in range(self.side)] for _ in range(self.side)]

        for row in range(self.side):
            for col in range(self.side):
                button = CTkButton(self, text="", width=40, height=40, command=lambda row=row, col=col: self.click_minefield(row, col), corner_radius=5)
                if self.minefield[row][col] == -1:
                    self.list_labels_mines[row][col] = CTkLabel(self, text="", width=40, height=40, corner_radius=5, image=self.bomba_img, anchor="center")
                else:
                    self.list_labels_mines[row][col] = CTkLabel(self, text="", width=40, height=40, corner_radius=5, anchor="center", fg_color="grey")
                self.minefield_buttons[row][col] = button
        
        if self.side == 3:
            self.place_minefield_3x3()
        elif self.side == 4:
            self.place_minefield_4x4()
        else:
            self.place_minefield_5x5()

    

    def place_minefield_3x3(self):
        for row in range(3):
            for col in range(3):
                self.minefield_buttons[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")

    def place_minefield_4x4(self):
        for row in range(4):
            for col in range(4):
                self.minefield_buttons[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")

    def place_minefield_5x5(self):
        for row in range(5):
            for col in range(5):
                self.minefield_buttons[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")
                

        

    def click_minefield(self, row, col):
        self.minefield_buttons[row][col].destroy()
        if self.minefield[row][col] == -1:
            self.game_over()
        else:
            self.update_multiplier()
            self.hits += 1
            match self.side:
                case 3:
                    self.list_labels_mines[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")
                case 4:
                    self.list_labels_mines[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")
                case 5:
                    self.list_labels_mines[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")
            
                    
    def set_axis(self):
        if self.side == 3:
            self.x_axis = 1280/2-50
            self.y_axis = 720/2-50
        elif self.side == 4:
            self.x_axis = 1280/2-75
            self.y_axis = 720/2-75
        else:
            self.x_axis = 1280/2-100
            self.y_axis = 720/2-100

    def game_over(self):
        for row in range(self.side):
            for col in range(self.side):
                self.minefield_buttons[row][col].destroy()
                self.list_labels_mines[row][col].place(x=self.x_axis+50*col, y=self.y_axis+50*row, anchor="center")

    def open_imgs(self):
        self.bomba_img = CTkImage(light_image=Image.open("resources/gato.png"), size=(40,40))
