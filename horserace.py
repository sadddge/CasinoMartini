import random
from customtkinter import *

class HorseRace(CTkFrame):
    def __init__(self, root, back):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.grid_frame = CTkFrame(self, width=800, height=600)
        self.grid_frame.place(relx=0.5, rely=0.3, anchor="center")
        self.grid_frame.grid_size = (5, 12)  # 5 filas (caballos) x 12 columnas (distancia)
        self.horses = [0] * self.grid_frame.grid_size[0]  # Posiciones iniciales de los caballos
        self.buttons = [[None for _ in range(self.grid_frame.grid_size[1])] for _ in range(self.grid_frame.grid_size[0])]
        self.running = False

        back_button = CTkButton(self, text="Back", command=back)
        back_button.place(relx=0.01, rely=0.01)
        self.create_grid()
        self.create_controls()

    def create_grid(self):
        for i in range(self.grid_frame.grid_size[0]):
            for j in range(self.grid_frame.grid_size[1]):
                button = CTkLabel(self.grid_frame, text='', width=30, height=30, corner_radius=0)
                button.grid(row=i, column=j, padx=1, pady=1)
                self.buttons[i][j] = button
        self.update_grid()

    def create_controls(self):
        start_button = CTkButton(self, text="Start Race", command=self.start_race)
        start_button.place(relx=0.5, rely=0.9, anchor="center")

        reset_button = CTkButton(self, text="Reset", command=self.reset_race)
        reset_button.place(relx=0.5, rely=0.95, anchor="center")


    def start_race(self):
        self.running = True
        self.race()

    def reset_race(self):
        self.running = False
        self.horses = [0] * self.grid_frame.grid_size[0]
        self.update_grid()

    def race(self):
        if not self.running:
            return
        for i in range(self.grid_frame.grid_size[0]):
            if self.horses[i] < self.grid_frame.grid_size[1] - 1:
                self.horses[i] += random.choice([0, 1])
        self.update_grid()

        if all(position >= self.grid_frame.grid_size[1] - 1 for position in self.horses):
            self.running = False
        else:
            self.after(500, self.race)

    def update_grid(self):
        for i in range(self.grid_frame.grid_size[0]):
            for j in range(self.grid_frame.grid_size[1]):
                if j == self.horses[i]:
                    self.buttons[i][j].configure(text='🐎')
                else:
                    self.buttons[i][j].configure(text='')

# Configurar la ventana principal
root = CTk()
root.geometry("1280x720")
root.title("Horse Race Game")

# Instanciar la clase HorseRace
app = HorseRace(root, root.quit)

# Iniciar el loop de la ventana principal
root.mainloop()
