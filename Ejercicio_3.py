class EmailInvalidoException(Exception):
    pass


def main():
    try:
        nombre = input("Ingrese su nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        edad = int(input("Ingrese su edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")

        correo = input("Ingrese su correo electrónico: ")
        if "@" not in correo:
            raise EmailInvalidoException(
                "El correo electrónico no es válido."
            )

        print("Registro exitoso.")

    except ValueError as e:
        print("Error de validación:", e)

    except EmailInvalidoException as e:
        print("Error en el correo:", e)

    except Exception as e:
        print("Error inesperado:", e)

    finally:
        print("El proceso de registro ha finalizado.")


if __name__ == "__main__":
    main()