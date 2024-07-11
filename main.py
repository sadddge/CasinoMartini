from customtkinter import *
from blackjack import Blackjack
from crash import Crash

from coinflip import Coinflip

from dados import Dados

root = CTk()
frame = None

def cambiar_juego(juego):
    global frame
    clear_screen()
    match juego:
        case "Ruleta":
            Ruleta(root, start_screen)
        case "Blackjack":
            Blackjack(root, start_screen)
        case "Carrera de caballos":
            Carrera(root, start_screen)
        case "Coinflip":
            Coinflip(root, start_screen)
        case "Dados":
            Dados(root, start_screen)
        case "High or Low":
            HighLow(root, start_screen)
        case "Crash":
            Crash(root, start_screen)
        case "Mines":
            Mines(root, start_screen)

def clear_screen():
    global frame
    if frame:
        for widget in frame.winfo_children():
            widget.destroy()

def start_screen():
    global frame
    clear_screen()
    frame = CTkFrame(root)
    frame.pack(fill="both", expand=True)

    ruleta = CTkButton(frame, text="Ruleta", command= cambiar_juego("Ruleta"))
    ruleta.pack(side="top")
    


def main():
    global frame, root
    root.title("Custom Tkinter")
    root.geometry("1280x720")
    root.resizable(False, False)

    start_screen()

    root.mainloop()

if __name__ == "__main__":
    main()