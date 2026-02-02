class Alumno:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre


class Nota:
    def __init__(self, codigo_alumno, aporte, valor):
        self.codigo_alumno = codigo_alumno
        self.aporte = aporte
        self.valor = valor


alumnos = []
notas = []


def menu():
    print("\nMENU PRINCIPAL")
    print("1. Alumnos")
    print("2. Calificaciones")
    print("3. Notas por Alumno")
    print("4. Notas por Aporte")
    print("5. Salir")


def registrar_alumno():
    codigo = input("Ingrese el codigo del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos.append(Alumno(codigo, nombre))
    print("Alumno registrado correctamente")


def registrar_nota():
    codigo = input("Ingrese el codigo del alumno: ")
    aporte = input("Ingrese el tipo de aporte: ")
    valor = float(input("Ingrese la nota: "))
    notas.append(Nota(codigo, aporte, valor))
    print("Nota registrada correctamente")


def notas_por_alumno():
    codigo = input("Ingrese el codigo del alumno: ")
    encontrado = False
    for nota in notas:
        if nota.codigo_alumno == codigo:
            print(nota.aporte, nota.valor)
            encontrado = True
    if not encontrado:
        print("No hay notas para este alumno")


def notas_por_aporte():
    aporte = input("Ingrese el tipo de aporte: ")
    encontrado = False
    for nota in notas:
        if nota.aporte.lower() == aporte.lower():
            print(nota.codigo_alumno, nota.valor)
            encontrado = True
    if not encontrado:
        print("No hay notas para este aporte")


while True:
    menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_alumno()
    elif opcion == "2":
        registrar_nota()
    elif opcion == "3":
        notas_por_alumno()
    elif opcion == "4":
        notas_por_aporte()
    elif opcion == "5":
        print("Programa finalizado")
        break
    else:
        print("Opcion invalida")
