# gemaakt door Edim Zilkic
import random
import tkinter as tk
from tkinter import messagebox


class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Menu")
        self.rolled = False
        self.te_raden_getal = random.randint(1, 100)
        self.woord_getal = random.randint(0,1)
        self.fout = 5

        self.getallen_rader_box_knop = tk.Button(self.master, text="Getallen rader", command=self.getallen_rader_box)
        self.getallen_rader_box_knop.pack()

        self.dobbelsteen_box_knop = tk.Button(self.master, text="Dobbelsteen", command=self.dobbelsteen_box)
        self.dobbelsteen_box_knop.pack()

        self.galgje_box_knop = tk.Button(self.master, text="Galgje", command=self.galgje_box)
        self.galgje_box_knop.pack()

    def dobbelsteen_box(self):
        self.box = tk.Toplevel(self.master)  # Use Toplevel for a separate window
        self.box.title("Dobbelsteen")  # Set title for new box
        self.box.withdraw()   
        self.dobbel_bericht = tk.Label(self.box, text="Klik op Dobbelen om te rollen")
        self.dobbel_bericht.pack()

        self.knop_dobbelsteen = tk.Button(self.box, text="Dobbelen", width=10, command=self.worpen)
        self.knop_dobbelsteen.pack()

        self.close_new_box_button = tk.Button(self.box, text="Sluiten", command=self.close_new_box)
        self.close_new_box_button.pack()

        self.box.deiconify()

    def close_new_box(self):
        self.rolled = False
        self.box.withdraw()  

    def close_galgje_box(self):
        self.woord_getal = random.randint(0,1)
        self.box.withdraw()  

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
        self.getal_box = tk.Toplevel(self.master)  # Use Toplevel for a separate window
        self.getal_box.title("Getallen rader")  # Set title for new box
        self.getal_box.withdraw()   
        self.raad_bericht = tk.Label(self.getal_box, text=f"Raad een getal tussen de 1-100")
        self.raad_bericht.pack()

        self.poging = tk.Entry(self.getal_box)
        self.poging.bind("<Return>", self.pogingen)
        self.poging.pack()

        self.check = tk.Button(self.getal_box, text="raden", command=self.pogingen)
        self.check.pack()


        self.getal_box.deiconify()

    def pogingen(self):
        try:
            gok = int(self.poging.get())

            if gok == self.te_raden_getal:
                self.bericht = tk.Label(self.getal_box, text="Gefeliciteerd! Je hebt het getal geraden!")
            elif gok < self.te_raden_getal:
                self.bericht = tk.Label(self.getal_box, text="Te laag! Probeer opnieuw.")
            else:
                self.bericht = tk.Label(self.getal_box, text="Te hoog! Probeer opnieuw.")

            self.bericht.pack()
            self.poging.delete(0, tk.END) 

        except ValueError:
            self.bericht = tk.Label(self.getal_box, text="Ongeldige invoer. Voer een geheel getal in.")
            self.bericht.pack()

    def galgje_box(self):
        self.box = tk.Toplevel(self.master)  # Use Toplevel for a separate window
        self.box.title("Galgje")  # Set title for new box
        self.box.withdraw()   
        self.raad_bericht = tk.Label(self.box, text=f"Type een letter om het woord te raden je hebt 5 levens")
        self.raad_bericht.pack()

        self.poging = tk.Entry(self.box)
        self.poging.bind("<Return>", self.galgje_pogingen)
        self.poging.pack()

        self.check = tk.Button(self.box, text="raden", command=self.galgje_pogingen)
        self.check.pack()

        self.box.deiconify()

    def galgje_pogingen(self):
        try:
            self.gok = str(self.poging.get()).lower()
            self.lijst = ["apple","banana","peer"]
            self.woord = str(self.lijst[self.woord_getal])
            if self.gok.isalpha():
                self.lettererin = False
            else:
                raise Exception(e)

            if self.gok in self.woord:
                self.lettererin = True
            
            if self.fout == 0:
                self.bericht = tk.Label(self.box, text="Je hebt verloren, open de box opnieuw om door te gaan!")
                self.bericht.pack()
                self.close_galgje_box_button = tk.Button(self.box, text="Sluiten", command=self.close_galgje_box)
                self.close_galgje_box_button.pack()
            elif self.gok == self.woord:
                self.bericht = tk.Label(self.box, text="Goed geraden!!")
                self.bericht.pack()
                self.close_galgje_box_button = tk.Button(self.box, text="Sluiten", command=self.close_galgje_box)
                self.close_galgje_box_button.pack()
            elif self.lettererin == False:
                self.bericht = tk.Label(self.box, text="fout probeer opnieuw!")
                self.bericht.pack()
                self.fout -= 1
            elif self.lettererin == True:
                self.bericht = tk.Label(self.box, text="goed geraden een letter goed!")
                self.bericht.pack()

        except Exception as e:
            self.exception_bericht = tk.Label(self.galgje_box, text="Ongeldige invoer, probeer opnieuw")
            self.exception_bericht.pack()
        
if __name__ == "__main__":
    master = tk.Tk()
    app = MainApp(master)
    master.mainloop()
