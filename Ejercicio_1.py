class Calculadora:

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b


def main():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        resultado = Calculadora.dividir(num1, num2)
        print("Resultado:", resultado)

    except ValueError as e:
        print("Error:", e)

    except Exception:
        print("Error: Debe ingresar solo números enteros.")

    finally:
        print("Proceso finalizado.")


if __name__ == "__main__":
    main()