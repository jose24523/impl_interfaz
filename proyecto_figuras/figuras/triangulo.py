# figuras/triangulo.py
from interfaces.figura import Figura

class Triangulo(Figura):
    def __init__(self, base: float, altura: float, lado1: float, lado2: float, lado3: float):
        if base <= 0 or altura <= 0 or lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            raise ValueError("Las dimenciones deben ser valores posiivos")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def obtener_nombre(self):
        return "Triangulo"
    