from datetime import datetime

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def calcular_antiguedad(self):
        anio_actual = datetime.now().year
        return anio_actual - self.anio


# Programa principal
if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Corolla", 2015)
    print("Antigüedad del vehículo:", vehiculo.calcular_antiguedad(), "años")
