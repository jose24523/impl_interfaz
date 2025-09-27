# figuras/pentagono.py
from interfaces.figura import Figura
import math

class Pentagono(Figura):
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 5 * self.lado

    def calcular_area(self) -> float:
        # Área pentágono regular = (5 * lado^2) / (4 * tan(pi/5))
        return (5 * self.lado ** 2) / (4 * math.tan(math.pi / 5))

    def obtener_nombre(self) -> str:
        return "Pentágono"
