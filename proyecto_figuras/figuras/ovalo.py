# figuras/ovalo.py
from interfaces.figura import Figura
import math

class Ovalo(Figura):
    def __init__(self, radio_mayor: float, radio_menor: float):
        if radio_mayor <= 0 or radio_menor <= 0:
            raise ValueError("Los radios deben ser valores positivos")
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor

    def calcular_perimetro(self) -> float:
        # P ≈ π [ 3(a + b) - sqrt{ (3a + b)(a + 3b) } ]
        a = self.radio_mayor
        b = self.radio_menor
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

    def calcular_area(self) -> float:
        # Área = π * a * b
        return math.pi * self.radio_mayor * self.radio_menor

    def obtener_nombre(self) -> str:
        return "Óvalo"
