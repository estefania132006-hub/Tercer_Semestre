class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año de publicación:", self.anio_publicacion)


# Programa principal
if __name__ == "__main__":
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro.mostrar_informacion()
