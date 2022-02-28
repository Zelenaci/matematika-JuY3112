from os.path import basename, splitext
import tkinter as tk
import random
# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Počítání pro ZŠ"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
    def generuj(self):
        self.funkce = random.choice([self.plus, self.minus, self.krat, self.deleno])
        self.funkce()
                             
    def plus():
        #generuje čísla pro operaci sčítání
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text="+")

    def minus(self):
        #generuje čísla pro operaci odčítání
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 99)
        if self.cisloA > self.cisloB or self.cisloA == self.cisloB:
            self.vysledek = self.cisloA - self.cisloB
        else:
            self.vysledek = self.cisloB - self.cisloA     
        self.lbl.config(text="-")    

    def krat(self):
        #generuje čísla pro operaci odčítaní
        self.cisloA = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text="*")
            
    def deleno():
        #generuje čísla pro operaco dělení
        self.cisloB = random.randint(1.9)
        self.vysledek = random.randint(1, 9)
        self.cisloA = self.cislo * self.vysledek
        self.lbl.config(text="/")    
    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()