# ===== CLASE LIBRO =====
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = "disponible"

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.estado})"


# ===== CLASE USUARIO =====
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.id = user_id
        self.libros_prestados = []


# ===== CLASE BIBLIOTECA =====
class Biblioteca:
    def __init__(self):
        self.libros = []     # ArrayList de libros
        self.usuarios = []   # ArrayList de usuarios

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, isbn, usuario_id):
        for libro in self.libros:
            if libro.isbn == isbn and libro.estado == "disponible":
                for usuario in self.usuarios:
                    if usuario.id == usuario_id:
                        libro.estado = "prestado"
                        usuario.libros_prestados.append(libro)
                        print("Libro prestado correctamente")
                        return
        print("No se pudo prestar el libro")

    def devolver_libro(self, isbn, usuario_id):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                for libro in usuario.libros_prestados:
                    if libro.isbn == isbn:
                        libro.estado = "disponible"
                        usuario.libros_prestados.remove(libro)
                        print("Libro devuelto")
                        return
        print("No se pudo devolver el libro")

    def mostrar_libros_usuario(self, usuario_id):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                for libro in usuario.libros_prestados:
                    print(libro)

    def listar_libros_disponibles(self):
        for libro in self.libros:
            if libro.estado == "disponible":
                print(libro)


# ===== PRUEBAS =====
biblio = Biblioteca()

libro1 = Libro("Cien años de soledad", "García Márquez", "123")
libro2 = Libro("1984", "George Orwell", "456")

usuario1 = Usuario("Ana", 1)

biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.registrar_usuario(usuario1)

biblio.prestar_libro("123", 1)

print("\nLibros prestados a Ana:")
biblio.mostrar_libros_usuario(1)

print("\nLibros disponibles:")
biblio.listar_libros_disponibles()
