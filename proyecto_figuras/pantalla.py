#Aqui desarrollara la implementacion de las clases de figuras
#En una interfaz grafica en tkinter

import math
import tkinter as tk
from tkinter import ttk, messagebox

class Figura:
    def calcular_perimetro(self): pass
    def calcular_area(self): pass

class Circulo(Figura):
    def __init__(self, radio): 
        if radio<=0: raise ValueError("Radio debe ser positivo")
        self.r = radio
    def calcular_perimetro(self): return 2*math.pi*self.r
    def calcular_area(self): return math.pi*self.r**2

class Cuadrado(Figura):
    def __init__(self, lado):
        if lado<=0: raise ValueError("Lado debe ser positivo")
        self.l = lado
    def calcular_perimetro(self): return 4*self.l
    def calcular_area(self): return self.l**2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        if base<=0 or altura<=0: raise ValueError("Valores positivos")
        self.b, self.a = base, altura
    def calcular_perimetro(self): return 2*(self.b+self.a)
    def calcular_area(self): return self.b*self.a

class Triangulo(Figura):
    def __init__(self, lado):
        if lado<=0: raise ValueError("Lado positivo")
        self.l = lado
    def calcular_perimetro(self): return 3*self.l
    def calcular_area(self): return (math.sqrt(3)/4)*self.l**2

FIGURAS = {
    "Círculo": (Circulo, ["Radio"]),
    "Cuadrado": (Cuadrado, ["Lado"]),
    "Rectángulo": (Rectangulo, ["Base", "Altura"]),
    "Triángulo": (Triangulo, ["Lado"]),
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Figuras")
        self.geometry("400x400")
        self.figura = tk.StringVar(value="Círculo")

        ttk.Label(self, text="Seleccione figura:").pack(pady=5)
        self.combo = ttk.Combobox(self, values=list(FIGURAS.keys()), textvariable=self.figura, state="readonly")
        self.combo.pack()
        self.combo.bind("<<ComboboxSelected>>", self.actualizar_campos)

        self.campos_frame = ttk.Frame(self)
        self.campos_frame.pack(pady=15, fill="x")

        self.btn = ttk.Button(self, text="Calcular", command=self.calcular)
        self.btn.pack(pady=10)

        self.lbl_perimetro = ttk.Label(self, text="")
        self.lbl_perimetro.pack()
        self.lbl_area = ttk.Label(self, text="")
        self.lbl_area.pack()

        self.entradas = []
        self.actualizar_campos()

    def actualizar_campos(self, event=None):
        for w in self.campos_frame.winfo_children(): w.destroy()
        self.entradas.clear()
        params = FIGURAS[self.figura.get()][1]
        for p in params:
            f = ttk.Frame(self.campos_frame)
            f.pack(fill="x", pady=3)
            ttk.Label(f, text=f"{p}:").pack(side="left", padx=5)
            e = ttk.Entry(f)
            e.pack(side="right", fill="x", expand=True, padx=5)
            self.entradas.append(e)
        self.lbl_perimetro.config(text="")
        self.lbl_area.config(text="")

    def calcular(self):
        try:
            vals = [float(e.get()) for e in self.entradas]
            if any(v<=0 for v in vals): raise ValueError
            clase, _ = FIGURAS[self.figura.get()]
            fig = clase(*vals)
            p = fig.calcular_perimetro()
            a = fig.calcular_area()
            self.lbl_perimetro.config(text=f"Perímetro: {p:.2f}")
            self.lbl_area.config(text=f"Área: {a:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos positivos")

if __name__ == "__main__":
    App().mainloop()
