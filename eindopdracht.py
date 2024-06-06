import random
import tkinter as tk
from tkinter import messagebox


class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Menu")
        self.rolled = False
        self.te_raden_getal = random.randint(1, 100)

        self.getallen_rader_box_knop = tk.Button(self.master, text="Getallen rader", command=self.getallen_rader_box)
        self.getallen_rader_box_knop.pack()

        self.dobbelsteen_box_knop = tk.Button(self.master, text="Dobbelsteen", command=self.box)
        self.dobbelsteen_box_knop.pack()

    def box(self):
        self.box = tk.Toplevel(self.master)  # Use Toplevel for a separate window
        self.box.title("Extra informatie")  # Set title for new box
        self.box.withdraw()  # Hide the new box initially

        self.dobbel_bericht = tk.Label(self.box, text="Klik op Dobbelen om te rollen")
        self.dobbel_bericht.pack()

        self.knop_dobbelsteen = tk.Button(self.box, text="Dobbelen", width=10, command=self.worpen)
        self.knop_dobbelsteen.pack()

        self.close_new_box_button = tk.Button(self.box, text="Sluiten", command=self.close_new_box)
        self.close_new_box_button.pack()

        self.box.deiconify()

    def close_new_box(self):
        self.box.withdraw()  # Hide the new box

    def worpen(self):
        if self.rolled:
            worp = random.randint(1,6)
            self.message_label.config(text=f"Je hebt een {worp} gegooid!")
        else:
            worp = random.randint(1,6)
            self.message_label = tk.Label(self.box, text=f"Je hebt een {worp} gegooid!")
            self.message_label.pack()
            self.rolled = True
    
    def getallen_rader_box(self):
        self.box = tk.Toplevel(self.master)  # Use Toplevel for a separate window
        self.box.title("Getallen rader")  # Set title for new box
        self.box.withdraw()  # Hide the new box initially

        self.poging = tk.Entry(self.box)
        self.poging.bind("<Return>", self.pogingen)
        self.poging.pack()

        self.check = tk.Button(self.box, text="raden", command=self.pogingen)
        self.check.pack()

        self.box.deiconify()

    def pogingen(self):
        try:
            # Get the user's guess as an integer
            gok = int(self.poging.get())

            # Check if the guess is correct
            if gok == self.te_raden_getal:
                # Display "Gefeliciteerd! Je hebt het getal geraden!"
                self.bericht = tk.Label(self.box, text="Gefeliciteerd! Je hebt het getal geraden!")
            elif gok < self.te_raden_getal:
                # Display "Te laag! Probeer opnieuw."
                self.bericht = tk.Label(self.box, text="Te laag! Probeer opnieuw.")
            else:
                # Display "Te hoog! Probeer opnieuw."
                self.bericht = tk.Label(self.box, text="Te hoog! Probeer opnieuw.")

            self.bericht.pack()
            self.poging.delete(0, tk.END)  # Clear the entry field after each guess

        except ValueError:  # Handle invalid input (non-integer)
            self.bericht = tk.Label(self.box, text="Ongeldige invoer. Voer een geheel getal in.")
            self.bericht.pack()

if __name__ == "__main__":
    master = tk.Tk()
    app = MainApp(master)
    master.mainloop()
