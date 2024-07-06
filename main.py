from customtkinter import *
from coinflip import Coinflip


root = CTk()
frame = None

def cambiar_juego(juego):
    global frame
    clear_screen()
    match juego:
        case "Ruleta":
            pass
        case "Blackjack":
            pass
        case "Carrera de caballos":
            pass
        case "Coinflip":
            Coinflip(root, start_screen)
        case "Dados":
            pass
        case "High or Low":
            pass
        case "Crash":
            pass
        case "Mines":
            pass

def clear_screen():
    global frame
    if frame:
        for widget in frame.winfo_children():
            widget.destroy()

def start_screen():
    global frame
    clear_screen()
    frame = CTkFrame(root)
    frame.place(relwidth=1, relheight=1)

    ruleta = CTkButton(frame, text="Ruleta", command = lambda: cambiar_juego("Ruleta"))
    ruleta.place(relx=0.5, rely=0.3, anchor="center")

    blackjack = CTkButton(frame, text="Blackjack", command = lambda: cambiar_juego("Blackjack"))
    blackjack.place(relx=0.5, rely=0.4, anchor="center")

    coinflip = CTkButton(frame, text="Coinflip", command = lambda: cambiar_juego("Coinflip"))
    coinflip.place(relx=0.5, rely=0.5, anchor="center")
    
    


def main():
    global frame, root
    root.title("Custom Tkinter")
    root.geometry("1280x720")
    root.resizable(False, False)

    start_screen()

    root.mainloop()

if __name__ == "__main__":
    main()