
from customtkinter import *
from PIL import Image
import random

class RouletteGame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        
        # Configuración de la ventana
        self.master.title("Juego de Ruleta")
        self.master.geometry("1280x720")
        self.numbers = self.initialize_numbers()
        
        self.start_screen()

    def initialize_numbers(self):
        numbers_data = [
            (32, "red"), (15, "black"), (19, "red"), (4, "black"), (21, "red"),
            (2, "black"), (25, "red"), (17, "black"), (34, "red"), (6, "black"),
            (27, "red"), (13, "black"), (36, "red"), (11, "black"), (30, "red"),
            (8, "black"), (23, "red"), (10, "black"), (5, "red"), (24, "black"),
            (16, "red"), (33, "black"), (1, "red"), (20, "black"), (14, "red"),
            (31, "black"), (9, "red"), (22, "black"), (18, "red"), (29, "black"),
            (7, "red"), (28, "black"), (12, "red"), (35, "black"), (3, "red"),
            (26, "black"), (0, "green")
        ]
        
        numbers = [Number(num, col) for num, col in numbers_data]
        return numbers

    def start_screen(self):

        self.x = -random.randint(0, 6120)
        self.x2 = self.x + 7400
        
        image = Image.open("resources/roulette.png")
        roulette_image = CTkImage(light_image=image, size=(7400,200))

        self.roulette_label1 = CTkLabel(self, image=roulette_image, text="")
        self.roulette_label1.place(x = self.x, rely=0.6)

        self.roulette_label2 = CTkLabel(self, image=roulette_image, text="")
        self.roulette_label2.place(x = self.x2 + 7400, rely=0.6)


        self.spin_button = CTkButton(self, text="Girar", command=self.start_spin)
        self.spin_button.place(relx=0.5, rely=0.9, anchor="center")

    def start_spin(self):
        self.spin_button.configure(state="disabled")
        print(f"start, x: {self.x}, x2: {self.x2}")
        self.animate()

    def stop(self):
        self.spin_button.configure(state="normal")

        if self.x == min(self.x, self.x2):
            self.x2 = self.x + 7400
        else:
            self.x = self.x2 + 7400

        print(f"stop, x: {self.x}, x2: {self.x2}")
        self.roulette_label1.place(x=self.x, rely=0.6)
        self.roulette_label2.place(x=self.x2, rely=0.6)

        roulette_x = self.current_roulette()
        dist = abs(roulette_x - 690)
        index = int(dist / 200)
        num = self.numbers[index].number
        print(num)

    def current_roulette(self):
        if self.x > -6710 and self.x < 690:
            return self.x
        else:
            return self.x2
        
    def animate(self, time = 0, dx = 0):
        if dx < 0:
            self.stop()
            return

        time = time + 15

        if time > 6000:
            dx = dx - 0.2
        elif dx < 40:
            dx = dx + 0.4

        self.x = self.x - dx
        self.x2 = self.x2 - dx

        if self.x < -13520:
            self.x = 1280
        if self.x2 < -13520:
            self.x2 = 1280

        self.roulette_label1.place(x=self.x, rely=0.6)
        self.roulette_label2.place(x=self.x2, rely=0.6)
        self.master.after(15, self.animate, time, dx)
        
class Number:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.even = number % 2 == 0
        self.half = 0 if number < 19 else 1
        self.init_row()
        self.init_group()

    def init_row(self):
        x = self.number % 3
        match x:
            case 0:
                self.row = 3
            case 1:
                self.row = 1
            case 2:
                self.row = 2

    def init_group(self):
        if self.number in range(1, 13):
            self.group = 1
        elif self.number in range(13, 25):
            self.group = 2
        elif self.number in range(25, 37):
            self.group = 3


if __name__ == "__main__":
    root = CTk()
    app = RouletteGame(root)
    root.mainloop()
