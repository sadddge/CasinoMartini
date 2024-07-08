import random
from customtkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class Crash(CTkFrame):
    def __init__(self, root, command):
        super().__init__(root)
        self.place(relwidth=1, relheight=1)

        self.command = command
        self.running = False
        self.time = 0
        self.scale = 1
        self.start_screen()

    def start_screen(self):
        self.clear_screen()
        back = CTkButton(self, text="Back", command=self.command)
        back.place(x=30, y=30)

        bet_label = CTkLabel(self, text="Bet:")
        bet_label.place(relx=0.1, rely=0.2, anchor="center")

        self.bet_entry = CTkEntry(self)
        self.bet_entry.place(relx=0.1, rely=0.25, anchor="center")

        retire_label = CTkLabel(self, text="Retire at:")
        retire_label.place(relx=0.1, rely=0.3, anchor="center")

        self.retire_entry = CTkEntry(self)
        self.retire_entry.place(relx=0.1, rely=0.35, anchor="center")

        self.bet_button = CTkButton(self, text="Bet", command=self.start_game)
        self.bet_button.place(relx=0.1, rely=0.4, anchor="center")

        self.win_label = CTkLabel(self, text="Win:")
        self.win_label.place(relx=0.1, rely=0.45, anchor="center")

    def start_game(self):
        self.bet = float(self.bet_entry.get())
        self.stop_at = round(random.uniform(1,600), 1)

        print(self.stop_at)

        self.running = True
        self.time = 0
        

        # Configurar la figura de matplotlib
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")
        self.multiplier_label = CTkLabel(self, text="Multiplier: 1")
        self.multiplier_label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Iniciar la animación
        self.animate()

    def animate(self):

        if self.time >= self.stop_at:
            self.running = False
            return
        
        if self.running:
            self.time += 0.1
            self.update_plot()
            self.after(100, self.animate)

    def update_plot(self):
        tiempo = np.linspace(0, self.time, 500)
        y = np.exp(0.0595 * tiempo)

        self.multiplier_label.configure(text=f"Multiplier: {round(y[-1], 2)}")
        self.multiplier_label.tkraise()

        self.ax.clear()
        self.ax.plot(tiempo, y)
        self.ax.set_xlabel('Tiempo (s)')
        self.ax.set_ylabel('Multiplicador')
        self.ax.set_title('Gráfica del Juego Crash')
        self.ax.set_xlim(0, self.time)
        self.ax.set_ylim(1, np.exp(0.0595 * self.time))
        self.canvas.draw()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
