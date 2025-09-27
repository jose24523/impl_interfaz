# figuras/rombo.py
from interfaces.figura import Figura

class Rombo(Figura):
    def __init__(self, diagonal_mayor: float, diagonal_menor: float):
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser valores positivos")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        lado = ((self.diagonal_mayor / 2) ** 2 + (self.diagonal_menor / 2) ** 2) ** 0.5
        return 4 * lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self) -> str:
        return "Rombo"
