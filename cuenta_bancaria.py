class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print("Depósito realizado.")
        print("Saldo actual:", self.saldo)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro realizado.")
            print("Saldo actual:", self.saldo)
        else:
            print("Fondos insuficientes.")


# Programa principal
if __name__ == "__main__":
    cuenta = CuentaBancaria("123456", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)
