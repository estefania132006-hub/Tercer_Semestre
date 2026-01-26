class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def calcular_aumento(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        print("Salario actualizado:", self.salario)


# Programa principal
if __name__ == "__main__":
    empleado = Empleado("Ana", 1200, "Recursos Humanos")
    empleado.calcular_aumento(10)
