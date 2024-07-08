from customtkinter import *
from crash import Crash


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
    frame.place(relwidth=1, relheight=1)

    ruleta = CTkButton(frame, text="Ruleta", command = lambda: cambiar_juego("Ruleta"))
    ruleta.place(relx=0.5, rely=0.3, anchor="center")

    blackjack = CTkButton(frame, text="Blackjack", command = lambda: cambiar_juego("Blackjack"))
    blackjack.place(relx=0.5, rely=0.4, anchor="center")

    carrera = CTkButton(frame, text="Carrera de caballos", command = lambda: cambiar_juego("Carrera de caballos"))
    carrera.place(relx=0.5, rely=0.5, anchor="center")

    coinflip = CTkButton(frame, text="Coinflip", command = lambda: cambiar_juego("Coinflip"))
    coinflip.place(relx=0.5, rely=0.6, anchor="center")

    dados = CTkButton(frame, text="Dados", command = lambda: cambiar_juego("Dados"))
    dados.place(relx=0.5, rely=0.7, anchor="center")

    highlow = CTkButton(frame, text="High or Low", command = lambda: cambiar_juego("High or Low"))
    highlow.place(relx=0.5, rely=0.8, anchor="center")

    crash = CTkButton(frame, text="Crash", command = lambda: cambiar_juego("Crash"))
    crash.place(relx=0.5, rely=0.9, anchor="center")

    mines = CTkButton(frame, text="Mines", command = lambda: cambiar_juego("Mines"))
    mines.place(relx=0.5, rely=1, anchor="center")
    
    


def main():
    global frame, root
    root.title("Custom Tkinter")
    root.geometry("1280x720")
    root.resizable(False, False)

    start_screen()

    root.mainloop()

if __name__ == "__main__":
    main()