import random
import tkinter as tk
from tkinter import messagebox


class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Menu")

    def box(self):
        resultaat = self.Label( master, text="Well hello there")


    def worpen(self):
        worp = self.dobbelsteen.worpen()
        self.resultaat_label.config(text=f"Je hebt een {worp} gegooid!")


if __name__ == "__main__":
    master = tk.Tk()
    app = MainApp(master)
    master.mainloop()
