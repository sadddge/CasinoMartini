from customtkinter import *

frame = None
root = CTk()

def cambiar_juego(juego):
    match juego:
        case "Ruleta":
            pass
        case "Blackjack":
            pass
        case "Carrera de caballos":
            pass
        case "Coinflip":
            pass
        case "Dados":
            pass
        case "High or Low":
            pass
        case "Crash":
            pass
        case "Mines":
            pass


def start_screen():
    frame = CTkFrame(root)
    frame.pack(fill="both", expand=True)

    ruleta = CTkButton(frame, text="Ruleta", command= cambiar_juego("Ruleta"))
    ruleta.pack(side="top")
    


def main():
    
    root.title("Custom Tkinter")
    root.geometry("1280x720")
    root.resizable(False, False)

    start_screen(root)

    back = CTkButton(frame, text="Back", command=lambda: start_screen(root))
    back.pack(side="bottom")

    root.mainloop()

if __name__ == "__main__":
    main()