# Clase Order
class Order:
    def __init__(self, order_number, items, prep_time):
        self.order_number = order_number
        self.items = items
        self.prep_time = prep_time

    def __str__(self):
        return f"Pedido #{self.order_number} | Ítems: {self.items} | Tiempo estimado: {self.prep_time} min"


# Clase RestaurantOrderSystem
class RestaurantOrderSystem:
    def __init__(self, limit=5):
        self.preparing_orders = []  # Pila (Stack)
        self.completed_orders = []  # Lista historial
        self.limit = limit

    # Recibir nuevo pedido
    def add_order(self, order):
        if len(self.preparing_orders) >= self.limit:
            print("No se pueden recibir más pedidos. Límite alcanzado.")
        else:
            self.preparing_orders.append(order)
            print(f"Pedido #{order.order_number} agregado a preparación.")

    # Completar pedido
    def complete_order(self):
        if not self.preparing_orders:
            print("No hay pedidos en preparación para completar.")
        else:
            order = self.preparing_orders.pop()
            self.completed_orders.append(order)
            print(f"Pedido #{order.order_number} completado.")

    # Mostrar pedidos en preparación (orden tipo pila: último primero)
    def show_preparing_orders(self):
        if not self.preparing_orders:
            print("No hay pedidos en preparación.")
        else:
            print("\nPedidos en preparación (último recibido primero):")
            for order in reversed(self.preparing_orders):
                print(order)

    # Mostrar historial
    def show_completed_orders(self):
        if not self.completed_orders:
            print("No hay pedidos completados.")
        else:
            print("\nHistorial de pedidos completados:")
            for order in self.completed_orders:
                print(order)


# Menú interactivo
def menu():
    system = RestaurantOrderSystem(limit=5)
    order_counter = 1

    while True:
        print("\n===== SISTEMA DE PEDIDOS =====")
        print("1. Ingresar nuevo pedido")
        print("2. Completar pedido más reciente")
        print("3. Ver pedidos en preparación")
        print("4. Ver historial de pedidos completados")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            items = input("Ingrese los ítems del pedido: ")

            try:
                prep_time = int(input("Ingrese el tiempo estimado de preparación (minutos): "))
                new_order = Order(order_counter, items, prep_time)
                system.add_order(new_order)
                order_counter += 1
            except ValueError:
                print("El tiempo debe ser un número entero.")

        elif option == "2":
            system.complete_order()

        elif option == "3":
            system.show_preparing_orders()

        elif option == "4":
            system.show_completed_orders()

        elif option == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
