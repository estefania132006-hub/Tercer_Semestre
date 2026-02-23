class PasswordInvalidaException(Exception):
    pass


class ValidadorPassword:

    @staticmethod
    def validar(password):

        if len(password) < 8:
            raise PasswordInvalidaException(
                "La contraseña debe tener mínimo 8 caracteres."
            )

        if not any(c.isupper() for c in password):
            raise PasswordInvalidaException(
                "La contraseña debe contener al menos una letra mayúscula."
            )

        if not any(c.isdigit() for c in password):
            raise PasswordInvalidaException(
                "La contraseña debe contener al menos un número."
            )


def main():
    try:
        password = input("Ingrese una contraseña: ")

        ValidadorPassword.validar(password)
        print("Contraseña válida.")

    except PasswordInvalidaException as e:
        print("Error:", e)

    finally:
        print("Proceso finalizado.")


if __name__ == "__main__":
    main()