import random
import tkinter as tk
from tkinter import messagebox

class Dobbelsteen:
    def worpen(self, getal):
        getal = random.randint(1,6)
        return getal


class DobbelsteenApp:
    def __init__(self, master):
        self.master = master
        master.title("Dobbelsteen")

        self.gooien_button = tk.Button(master, text="Gooi een dobbelsteen", command=self.worpen)
        self.gooien_button.pack()

        self.resultaat_label = tk.Label(master, text="")

        self.dobbelsteen = Dobbelsteen()

    def worpen(self):
        self.resultaat_label.config(text=f"")
