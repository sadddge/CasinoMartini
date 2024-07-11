from customtkinter import *
from blackjack import Blackjack
from crash import Crash
from mines import Mines
from coinflip import Coinflip
from roulette import Roullete
from PIL import Image
from dados import Dados



class User:
    def __init__(self):
        self.money = 1000000

    def add_money(self, amount):
        self.money += amount

    def remove_money(self, amount):
        self.money -= amount

root = CTk()
user = User()

def save_game(name):
    file = open("data.txt", "a")
    money = round(user.money, 2)
    line = f"{name}: ${money}\n"
    file.write(line)

def exit_game():
    dialog = CTkInputDialog(title="Salir", text="Ingrese su nombre para guardar el puntaje")
    name = dialog.get_input()
    if name != "":
        save_game(name)
    root.destroy()

def puntajes():
    puntajes = CTkToplevel(root)
    puntajes.title("Puntajes")
    puntajes.geometry("300x300")
    puntajes.resizable(False, False)

    frame = CTkScrollableFrame(puntajes)
    frame.pack(fill="both", expand=True)

    with open("data.txt", "r") as file:
        for line in file:
            label = CTkLabel(frame, text=line)
            label.pack()
    

def cambiar_juego(juego):
    clear_screen()
    match juego:
        case "Ruleta":
            Roullete(root, user, start_screen)
        case "Blackjack":
            Blackjack(root, user, start_screen)
        case "Coinflip":
            Coinflip(root, user, start_screen)
        case "Dados":
            Dados(root, user, start_screen)
        case "Crash":
            Crash(root, user, start_screen)
        case "Mines":
            Mines(root, user, start_screen)

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def start_screen():

    clear_screen()
    frame = CTkFrame(root)
    frame.pack(fill="both", expand=True)

    money = round(user.money, 2)
    money_label = CTkLabel(frame, text=f"Dinero: ${money}", font=("Arial Black", 14))
    money_label.place(relx=0.9, rely=0.1, anchor="center")

    exit_button = CTkButton(frame, text="Salir", font=("Arial Black", 14), command=exit_game)
    exit_button.place(relx=0.1, rely=0.1, anchor="center")

    puntajes_button = CTkButton(frame, text="Puntajes", font=("Arial Black", 14), command=puntajes)
    puntajes_button.place(relx=0.1, rely=0.2, anchor="center")

    title = CTkLabel(frame, text="Casino", font=("Arial black", 30))
    title.place(relx=0.5, rely=0.1, anchor="center")

    roul_image = Image.open("resources/roul_logo.webp")
    roul_ctki = CTkImage(light_image=roul_image, size=(280, 120))
    roul_button = CTkButton(frame, image=roul_ctki, text="Ruleta", font=("Arial Black", 14), fg_color="transparent", hover_color="gray", command=lambda: cambiar_juego("Ruleta"))
    roul_button.place(relx=0.2, rely=0.35, anchor="center")

    black_image = Image.open("resources/blackjack_logo.webp")
    black_ctki = CTkImage(light_image=black_image, size=(280, 120))
    black_button = CTkButton(frame, image=black_ctki, text="Blackjack", font=("Arial Black", 14), fg_color="transparent", hover_color="gray", command=lambda: cambiar_juego("Blackjack"))
    black_button.place(relx=0.5, rely=0.35, anchor="center")

    coin_image = Image.open("resources/coinflip_logo.webp")
    coin_ctki = CTkImage(light_image=coin_image, size=(280, 120))
    coin_button = CTkButton(frame, image=coin_ctki, text="Coinflip", font=("Arial Black", 14), fg_color="transparent", hover_color="gray", command=lambda: cambiar_juego("Coinflip"))
    coin_button.place(relx=0.8, rely=0.35, anchor="center")

    dice_image = Image.open("resources/dice_logo.webp")
    dice_ctki = CTkImage(light_image=dice_image, size=(280, 120))
    dice_button = CTkButton(frame, image=dice_ctki, text="Dados", font=("Arial Black", 14), fg_color="transparent", hover_color="gray", command=lambda: cambiar_juego("Dados"))
    dice_button.place(relx=0.2, rely=0.65, anchor="center")


    crash_image = Image.open("resources/crash_logo.webp")
    crash_ctki = CTkImage(light_image=crash_image, size=(280, 120))
    crash_button = CTkButton(frame, image=crash_ctki, text="Crash", font=("Arial Black", 14), fg_color="transparent", hover_color="gray", command=lambda: cambiar_juego("Crash"))
    crash_button.place(relx=0.5, rely=0.65, anchor="center")

    mines_image = Image.open("resources/mines_logo.webp")
    mines_ctki = CTkImage(light_image=mines_image, size=(280, 120))
    mines_button = CTkButton(frame, image=mines_ctki, text="Mines", font=("Arial Black", 14), fg_color="transparent", hover_color="gray", command=lambda: cambiar_juego("Mines"))
    mines_button.place(relx=0.8, rely=0.65, anchor="center")






def main():
    root.title("Casino Martini")
    root.geometry("1280x720")
    root.resizable(False, False)

    start_screen()

    root.mainloop()

if __name__ == "__main__":
    main()