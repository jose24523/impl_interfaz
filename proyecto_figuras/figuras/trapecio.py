# figuras/trapecio.py
from interfaces.figura import Figura

class Trapecio(Figura):
    def __init__(self, base_mayor: float, base_menor: float, lado1: float, lado2: float, altura: float):
        if base_mayor <= 0 or base_menor <= 0 or lado1 <= 0 or lado2 <= 0 or altura <= 0:
            raise ValueError("Todas las dimensiones deben ser valores positivos")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

    def calcular_area(self) -> float:
        # Área trapecio = ((base mayor + base menor) / 2) * altura
        return ((self.base_mayor + self.base_menor) / 2) * self.altura

    def obtener_nombre(self) -> str:
        return "Trapecio"
