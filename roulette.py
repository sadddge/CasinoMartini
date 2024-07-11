from customtkinter import *
from PIL import Image
import random

class Roullete(CTkFrame):
    def __init__(self, root, user, command):
        super().__init__(root)
        self.root = root
        self.pack(fill="both", expand=True)

        
        self.user = user
        self.numbers = self.initialize_numbers()
        self.init_groups()
        
        back = CTkButton(self, text="Back", command=command)
        back.place(x=30, y=30)
        self.bets = {}

        self.start_screen()

    def init_groups(self):
        self.num_order = [3,6,9,12,15,18,21,24,27,30,33,36,2,5,8,11,14,17,20,23,26,29,32,35,1,4,7,10,13,16,19,22,25,28,31,34]
        self.black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.even = [i for i in range(1, 37) if i % 2 == 0]
        self.odd = [i for i in range(1, 37) if i % 2 != 0]
        self.first_half = [i for i in range(1, 19)]
        self.second_half = [i for i in range(19, 37)]
        self.first_row = [i for i in range(1, 37) if i % 3 == 0]
        self.second_row = [i for i in range(1, 37) if i % 3 == 2]
        self.third_row = [i for i in range(1, 37) if i % 3 == 1]
        self.first_third = [i for i in range(1, 13)]
        self.second_third = [i for i in range(13, 25)]
        self.third_third = [i for i in range(25, 37)]

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

        self.money_label = CTkLabel(self, text=f"Dinero: ${self.user.money}", font=("Arial Black", 14))
        self.money_label.place(relx=0.9, rely=0.1, anchor="center")
        
        image = Image.open("resources/roulette.png")
        roulette_image = CTkImage(light_image=image, size=(7400,200))

        self.roulette_label1 = CTkLabel(self, image=roulette_image, text="")
        self.roulette_label1.place(x = self.x, rely=0.15)

        self.roulette_label2 = CTkLabel(self, image=roulette_image, text="")
        self.roulette_label2.place(x = self.x2 + 7400, rely=0.15)

        num_selec_label = CTkLabel(self, text="", fg_color="black", width=15, height=50)
        num_selec_label.place(relx=0.5, rely=0.14, anchor="center")

        num_selec_label2 = CTkLabel(self, text="", fg_color="#00bf63", width=11, height=46)
        num_selec_label2.place(relx=0.5, rely=0.14, anchor="center")

        self.spin_button = CTkButton(self, text="Girar", command=self.start_spin)
        self.spin_button.place(relx=0.5, rely=0.5, anchor="center")

        self.bet_label = CTkLabel(self, text="bet", font=("Arial Black", 14))
        self.bet_label.place(x = 52, rely=0.865)

        self.bet_entry = CTkEntry(self)
        self.bet_entry.place(x = 50, rely=0.9)

        

        self.start_bet_menu()

    def start_bet_menu(self):
        pad = 5
        size = 50
        frame_width = size * 14 + 15 * pad
        frame_height = size * 5 + 6 * pad
        third_width = size * 4 + 3 * pad
        doble_width = size * 2 + pad
        color = self.root.cget("fg_color")
        font = ("Arial Black", 16)
        hover = "gray"
        black = "#373737"
        red = "#ff3131"
        self.bet_menu = CTkFrame(self, width=frame_width, height=frame_height, fg_color="transparent")
        self.bet_menu.place(relx=0.5, rely=0.75, anchor="center")
        
        number_button = CTkButton(self.bet_menu, text="0", width=size, height= size * 3 + 2 * pad, fg_color="#00bf63", hover_color=hover, font=font, command=lambda: self.bet_on_number([0]))
        number_button.place(x=5, y=5)
        
        
        first_row_button = CTkButton(self.bet_menu, text="2:1", width=size, height=size, fg_color=color,
                                      hover_color=hover, font=font, command=lambda: self.bet_on_number(self.first_row))
        second_row_button = CTkButton(self.bet_menu, text="2:1", width=size, height=size, fg_color=color
                                      , hover_color=hover, font=font, command=lambda: self.bet_on_number(self.second_row))
        third_row_button = CTkButton(self.bet_menu, text="2:1", width=size, height=size, fg_color=color,
                                      hover_color=hover, font=font, command=lambda: self.bet_on_number(self.third_row))
        firts_third_button = CTkButton(self.bet_menu, text="1 to 12", width= third_width, height=size, fg_color=color,
                                        hover_color=hover, font=font, command=lambda: self.bet_on_number(self.first_third))
        second_third_button = CTkButton(self.bet_menu, text="13 to 24", width= third_width, height=size, fg_color=color,
                                         hover_color=hover, font=font, command=lambda: self.bet_on_number(self.second_third))
        third_third_button = CTkButton(self.bet_menu, text="25 to 36", width= third_width, height=size, fg_color=color,
                                        hover_color=hover, font=font, command=lambda: self.bet_on_number(self.third_third))
        one_to_eighteen_button = CTkButton(self.bet_menu, text="1 to 18", width= doble_width, height=size,
                                            fg_color=color, hover_color=hover, font=font, command=lambda: self.bet_on_number(self.first_half))
        even_button = CTkButton(self.bet_menu, text="Even", width= doble_width, height=size, fg_color=color,
                                 hover_color=hover, font=font, command=lambda: self.bet_on_number(self.even))
        red_button = CTkButton(self.bet_menu, text="", width= doble_width, height=size, fg_color=red,
                                hover_color=hover, font=font, command=lambda: self.bet_on_number(self.red))
        black_button = CTkButton(self.bet_menu, text="", width= doble_width, height=size, fg_color=black,
                                  hover_color=hover, font=font, command=lambda: self.bet_on_number(self.black))
        odd_button = CTkButton(self.bet_menu, text="Odd", width= doble_width, height=size, fg_color=color,
                                hover_color=hover, font=font, command=lambda: self.bet_on_number(self.odd))
        nineteen_to_thirty_six_button = CTkButton(self.bet_menu, text="19 to 36", width= doble_width, height=size, fg_color=color,
                                                   hover_color=hover, font=font, command=lambda: self.bet_on_number(self.second_half))

        first_row_button.place(x = size * 13 + 14 * pad, y = 5)
        second_row_button.place(x = size * 13 + 14 * pad, y = size + pad * 2)
        third_row_button.place(x = size * 13 + 14 * pad, y = size * 2 + 3 * pad)
        firts_third_button.place(x = pad * 2 + size, y = size * 3 + 4 * pad)
        second_third_button.place(x = pad * 3 + size + third_width, y = size * 3 + 4 * pad)
        third_third_button.place(x = pad * 4 + size + third_width * 2, y = size * 3 + 4 * pad)
        one_to_eighteen_button.place(x = pad * 2 + size, y = size * 4 + 5 * pad)
        even_button.place(x = pad * 3 + size + doble_width, y = size * 4 + 5 * pad)
        red_button.place(x = pad * 4 + size + doble_width * 2, y = size * 4 + 5 * pad)
        black_button.place(x = pad * 5 + size + doble_width * 3, y = size * 4 + 5 * pad)
        odd_button.place(x = pad * 6 + size + doble_width * 4, y = size * 4 + 5 * pad)
        nineteen_to_thirty_six_button.place(x = pad * 7 + size + doble_width * 5, y = size * 4 + 5 * pad)

        for i, number in enumerate(self.num_order):
            x = 60 + ((i%12) * size) + (pad * (i%12))
            y = 5 + size * int(i/12) + pad * int(i/12)
            color = black if number in self.black else red
            number_button = CTkButton(self.bet_menu, text=str(number),  width=size, height=size, fg_color=color, hover_color=hover, font=font, command=lambda number=number: self.bet_on_number([number]))
            number_button.place(x= x, y= y)
 
    def bet_on_number(self, numbers):
        bet = int(self.bet_entry.get())/len(numbers) 
        for num in numbers:
            if num not in self.bets:
                self.bets[num] = 0  
            self.bets[num] += bet

        self.user.remove_money(int(self.bet_entry.get()))
        self.money_label.configure(text=f"Dinero: ${self.user.money}")

    def all_bets(self):
        total = 0
        for key in self.bets:
            total += self.bets[key]
        return total

  
    def start_spin(self):
        self.spin_button.configure(state="disabled")
        self.animate()

    def stop(self):
        self.spin_button.configure(state="normal")

        roulette_x = self.current_roulette()

        if roulette_x < 0 or roulette_x > 1280:
            if self.x == roulette_x:
                self.x2 = self.x + 7400
            else:
                self.x = self.x2 + 7400

        self.roulette_label1.place(x=self.x)
        self.roulette_label2.place(x=self.x2)

        dist = abs(roulette_x - 640)
        index = int(dist / 200)
        num = self.numbers[index].number

        won = 0 if num not in self.bets else self.bets[num] * 36

        self.user.add_money(won)
        self.money_label.configure(text=f"Dinero: ${self.user.money}")

        self.win_label = CTkLabel(self, text=f"win \n{won}", font=("Arial Black", 14))
        self.win_label.place(relx=0.9, rely=0.865, anchor="center")

        self.root.after(3000, self.win_label.destroy)

        self.bets = {}

    def current_roulette(self):
        if self.x > -6760 and self.x < 640:
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

        self.roulette_label1.place(x=self.x)
        self.roulette_label2.place(x=self.x2)
        self.root.after(15, self.animate, time, dx)
        
class Number:
    def __init__(self, number, color):
        self.number = number
        self.color = color

