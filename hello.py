import tkinter as tk
from tkinter import messagebox
 
class BTWCalculator:
    def bereken_btw(self, bedrag):
        try:
            bedrag = float(bedrag)
            btw_percentage = 0.21  
            btw_bedrag = bedrag * btw_percentage
            totaal_bedrag = bedrag + btw_bedrag
            return bedrag, btw_bedrag, totaal_bedrag
        except ValueError:
            return None, None, None
 
class ReistijdCalculator:
    def bereken_reistijd(self, afstand, snelheid):
        try:
            afstand = float(afstand)
            snelheid = float(snelheid)
            reistijd = afstand / snelheid
            return reistijd
        except ValueError:
            return None
 
class VierkantCalculator:
    def bereken_vierkant(self, lengte, breedte):
        try:
            lengte = float(lengte)
            breedte = float(breedte)
            omtrek = 2 * (lengte + breedte)
            oppervlakte = lengte * breedte
            return omtrek, oppervlakte
        except ValueError:
            return None, None
 
class CirkelCalculator:
    def bereken_cirkel(self, diameter):
        try:
            diameter = float(diameter)
            straal = diameter / 2
            omtrek = 2 * 3.14 * straal
            oppervlakte = 3.14 * straal ** 2
            return omtrek, oppervlakte
        except ValueError:
            return None, None
 
class ValutaOmrekenen:
    def __init__(self):
        self.wisselkoersen = {"EURUSD": 1.2, "USDGBP": 0.8}
 
    def omrekenen(self, bedrag, van_valuta, naar_valuta):
        try:
            bedrag = float(bedrag)
            wisselkoers = self.wisselkoersen.get(van_valuta + naar_valuta)
            if wisselkoers:
                omgerekend_bedrag = bedrag * wisselkoers
                return omgerekend_bedrag
            else:
                return None
        except ValueError:
            return None
 
class BTWCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("BTW Calculator")
 
        self.label = tk.Label(master, text="Voer het bedrag in:")
        self.label.pack()
 
        self.bedrag_entry = tk.Entry(master)
        self.bedrag_entry.pack()
 
        self.bereken_button = tk.Button(master, text="Bereken BTW", command=self.bereken_btw)
        self.bereken_button.pack()
 
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
 
        self.calculator = BTWCalculator()
 
    def bereken_btw(self):
        bedrag = self.bedrag_entry.get()
        bedrag, btw, totaal = self.calculator.bereken_btw(bedrag)
        if bedrag is not None:
            self.resultaat_label.config(text=f"Bedrag: {bedrag}\nBTW: {btw}\nTotaal: {totaal}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer een geldig bedrag in.")
 
class ReistijdCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Reistijd Calculator")
 
        self.afstand_label = tk.Label(master, text="Voer de afstand in (km):")
        self.afstand_label.pack()
 
        self.afstand_entry = tk.Entry(master)
        self.afstand_entry.pack()
 
        self.snelheid_label = tk.Label(master, text="Voer de snelheid in (km/u):")
        self.snelheid_label.pack()
 
        self.snelheid_entry = tk.Entry(master)
        self.snelheid_entry.pack()
 
        self.bereken_button = tk.Button(master, text="Bereken Reistijd", command=self.bereken_reistijd)
        self.bereken_button.pack()
 
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
 
        self.calculator = ReistijdCalculator()
 
    def bereken_reistijd(self):
        afstand = self.afstand_entry.get()
        snelheid = self.snelheid_entry.get()
        reistijd = self.calculator.bereken_reistijd(afstand, snelheid)
        if reistijd is not None:
            self.resultaat_label.config(text=f"Geschatte reistijd: {reistijd:.2f} uur")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer geldige afstand en snelheid in.")
 
class VierkantCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Vierkant Calculator")
 
        self.lengte_label = tk.Label(master, text="Voer de lengte van het vierkant in:")
        self.lengte_label.pack()
 
        self.lengte_entry = tk.Entry(master)
        self.lengte_entry.pack()
 
        self.breedte_label = tk.Label(master, text="Voer de breedte van het vierkant in:")
        self.breedte_label.pack()
 
        self.breedte_entry = tk.Entry(master)
        self.breedte_entry.pack()
 
        self.bereken_button = tk.Button(master, text="Bereken Vierkant", command=self.bereken_vierkant)
        self.bereken_button.pack()
 
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
 
        self.calculator = VierkantCalculator()
 
    def bereken_vierkant(self):
        lengte = self.lengte_entry.get()
        breedte = self.breedte_entry.get()
        omtrek, oppervlakte = self.calculator.bereken_vierkant(lengte, breedte)
        if omtrek is not None:
            self.resultaat_label.config(text=f"Omtrek: {omtrek}\nOppervlakte: {oppervlakte}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer geldige lengte en breedte in.")
 
class CirkelCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Cirkel Calculator")
 
        self.diameter_label = tk.Label(master, text="Voer de diameter van de cirkel in:")
        self.diameter_label.pack()
 
        self.diameter_entry = tk.Entry(master)
        self.diameter_entry.pack()
 
        self.bereken_button = tk.Button(master, text="Bereken Cirkel", command=self.bereken_cirkel)
        self.bereken_button.pack()
 
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
 
        self.calculator = CirkelCalculator()
 
    def bereken_cirkel(self):
        diameter = self.diameter_entry.get()
        omtrek, oppervlakte = self.calculator.bereken_cirkel(diameter)
        if omtrek is not None:
            self.resultaat_label.config(text=f"Omtrek: {omtrek:.2f}\nOppervlakte: {oppervlakte:.2f}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Voer een geldige diameter in.")
 
class ValutaOmrekenenApp:
    def __init__(self, master):
        self.master = master
        master.title("Valuta Omrekenen")
 
        self.bedrag_label = tk.Label(master, text="Voer het bedrag in:")
        self.bedrag_label.pack()
 
        self.bedrag_entry = tk.Entry(master)
        self.bedrag_entry.pack()
 
        self.van_valuta_label = tk.Label(master, text="Van valuta (bijv. EUR):")
        self.van_valuta_label.pack()
 
        self.van_valuta_entry = tk.Entry(master)
        self.van_valuta_entry.pack()
 
        self.naar_valuta_label = tk.Label(master, text="Naar valuta (bijv. USD):")
        self.naar_valuta_label.pack()
 
        self.naar_valuta_entry = tk.Entry(master)
        self.naar_valuta_entry.pack()
 
        self.bereken_button = tk.Button(master, text="Omrekenen", command=self.omrekenen)
        self.bereken_button.pack()
 
        self.resultaat_label = tk.Label(master, text="")
        self.resultaat_label.pack()
 
        self.calculator = ValutaOmrekenen()
 
    def omrekenen(self):
        bedrag = self.bedrag_entry.get()
        van_valuta = self.van_valuta_entry.get().upper()
        naar_valuta = self.naar_valuta_entry.get().upper()
        omgerekend_bedrag = self.calculator.omrekenen(bedrag, van_valuta, naar_valuta)
        if omgerekend_bedrag is not None:
            self.resultaat_label.config(text=f"Omgerekend bedrag: {omgerekend_bedrag:.2f} {naar_valuta}")
        else:
            messagebox.showerror("Fout", "Ongeldige invoer. Controleer de valutacodes.")
 
class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Functionaliteit Schermen")
 
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
 
        self.create_menu()
 
    def create_menu(self):
        functionaliteit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Functionaliteit", menu=functionaliteit_menu)
        functionaliteit_menu.add_command(label="BTW Calculator", command=self.open_btw_calculator)
        functionaliteit_menu.add_command(label="Reistijd Calculator", command=self.open_reistijd_calculator)
        functionaliteit_menu.add_command(label="Vierkant Calculator", command=self.open_vierkant_calculator)
        functionaliteit_menu.add_command(label="Cirkel Calculator", command=self.open_cirkel_calculator)
        functionaliteit_menu.add_command(label="Valuta Omrekenen", command=self.open_valuta_omrekenen)
 
    def open_btw_calculator(self):
        window = tk.Toplevel(self.master)
        app = BTWCalculatorApp(window)
 
    def open_reistijd_calculator(self):
        window = tk.Toplevel(self.master)
        app = ReistijdCalculatorApp(window)
 
    def open_vierkant_calculator(self):
        window = tk.Toplevel(self.master)
        app = VierkantCalculatorApp(window)
 
    def open_cirkel_calculator(self):
        window = tk.Toplevel(self.master)
        app = CirkelCalculatorApp(window)
 
    def open_valuta_omrekenen(self):
        window = tk.Toplevel(self.master)
        app = ValutaOmrekenenApp(window)
 
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()
 