import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Programa principal
if __name__ == "__main__":
    circulo = Circulo(5)
    print("Área:", circulo.calcular_area())
    print("Perímetro:", circulo.calcular_perimetro())
