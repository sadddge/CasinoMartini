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
        self.betting = False
        self.time = 0
        self.scale = 1

        self.canvas = None
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

        self.retire_button = CTkButton(self, text="Retire", command=self.retire, state="disabled")
        self.retire_button.place(relx=0.1, rely=0.5, anchor="center")

    def start_game(self):
        bet = self.bet_entry.get()

        if bet == "": return

        self.clear_graph()

        self.betting = True
        self.running = True
        self.bet = float(bet)
        self.stop_at = self.selec_random_stop()
        self.time = 0

        self.bet_button.configure(state="disabled")
        self.retire_button.configure(state="normal")

       

        # Configurar la figura de matplotlib
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor="center")
        self.multiplier_label = CTkLabel(self, text="Multiplier: 1")
        self.multiplier_label.place(relx=0.5, rely=0.1, anchor="center")

        # Iniciar la animación
        self.animate()

    def retire_time(self):
        retire = self.retire_entry.get()
        if retire == "": return None

        return float(retire)

    def retire(self):
        self.betting = False
        self.retire_button.configure(state="disabled")

    def clear_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.ax.clear()
            if hasattr(self, 'multiplier_label'):
                self.multiplier_label.destroy()

    def animate(self):
        
        if self.betting:
            if self.time >= self.stop_at:
                self.retire()

        if self.time >= self.stop_at:
            print("stop")
            self.betting = False
            self.running = False
            self.bet_button.configure(state="normal")
            self.retire_button.configure(state="disabled")
            return

        if self.running:
            print("running")
            self.time += 0.1
            self.update_plot()
            self.after(100, self.animate)

    def update_plot(self):
        tiempo = np.linspace(0, self.time, 500)
        y = self.multiplier(tiempo)

        self.multiplier_label.configure(text=f"Multiplier: {round(y[-1], 2)}")
        self.multiplier_label.tkraise()

        if self.betting:
            self.win_label.configure(text=f"Win: {self.bet * y[-1]:.2f}")

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

    def multiplier(self, t):
        return np.exp(0.0595 * t)

    def lambda_crash(self, t):
        return 1 / self.multiplier(t)

    def probability_crash(self, t1, t2):
        return np.exp(-self.lambda_crash(t1) * t1) - np.exp(-self.lambda_crash(t2) * t2)

    def selec_random_stop(self):
        ranges = [(0, 10), (10, 20), (20, 30), (30, 60), (60, 120), (120, 300), (300, 600)]
        probs = [self.probability_crash(t1, t2) for t1, t2 in ranges]
        acum_probs = np.cumsum(probs)

        r = np.random.rand()
        for i, (t1, t2) in enumerate(ranges):
            if r < acum_probs[i]:
                return np.random.uniform(t1, t2)
        return ranges[-1][1]

# Configurar la ventana principal
root = CTk()
root.geometry("1280x720")
root.title("Juego Crash")

# Instanciar la clase Crash
app = Crash(root, command=root.destroy)

# Iniciar el loop de la ventana principal
root.mainloop()
