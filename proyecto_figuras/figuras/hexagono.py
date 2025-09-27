# figuras/hexagono.py
from interfaces.figura import Figura
import math

class Hexagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 6 * self.lado

    def calcular_area(self) -> float:
        # Área hexágono regular = (3 * sqrt(3) * lado^2) / 2
        return (3 * math.sqrt(3) * self.lado ** 2) / 2

    def obtener_nombre(self) -> str:
        return "Hexágono"
