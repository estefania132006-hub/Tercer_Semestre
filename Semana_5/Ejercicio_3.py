# ===== CLASE TAREA =====
class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"   # pendiente | en progreso | completada
        self.asignado = None

    def __str__(self):
        return f"{self.titulo} - {self.estado}"


# ===== CLASE MIEMBRO =====
class Miembro:
    def __init__(self, nombre, miembro_id):
        self.nombre = nombre
        self.id = miembro_id
        self.tareas = []  # ArrayList de tareas


# ===== CLASE EQUIPO =====
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []  # ArrayList de miembros
        self.tareas = []    # ArrayList de tareas


# ===== GESTOR DE TAREAS =====
class GestorTareas:
    def __init__(self):
        self.equipos = []   # ArrayList de equipos

    def crear_equipo(self, equipo):
        self.equipos.append(equipo)

    def agregar_miembro(self, equipo, miembro):
        equipo.miembros.append(miembro)

    def crear_tarea(self, equipo, tarea):
        equipo.tareas.append(tarea)

    def asignar_tarea(self, equipo, tarea, miembro):
        if miembro in equipo.miembros:
            tarea.asignado = miembro
            miembro.tareas.append(tarea)
            print("Tarea asignada correctamente")
        else:
            print("El miembro no pertenece al equipo")

    def cambiar_estado(self, tarea, estado):
        tarea.estado = estado
        print(f"Estado cambiado a: {estado}")

    def mostrar_tareas_miembro(self, miembro):
        print(f"\nTareas de {miembro.nombre}:")
        for tarea in miembro.tareas:
            print(tarea)

    def tareas_pendientes_equipo(self, equipo):
        print(f"\nTareas pendientes del equipo {equipo.nombre}:")
        for tarea in equipo.tareas:
            if tarea.estado == "pendiente":
                print(tarea)


# ===== PRUEBAS =====
gestor = GestorTareas()

equipo1 = Equipo("Desarrollo Web")

miembro1 = Miembro("Luis", 1)
miembro2 = Miembro("Ana", 2)

gestor.crear_equipo(equipo1)
gestor.agregar_miembro(equipo1, miembro1)
gestor.agregar_miembro(equipo1, miembro2)

tarea1 = Tarea("Diseñar interfaz", "Crear diseño del sitio")
tarea2 = Tarea("Programar backend", "Lógica del servidor")

gestor.crear_tarea(equipo1, tarea1)
gestor.crear_tarea(equipo1, tarea2)

gestor.asignar_tarea(equipo1, tarea1, miembro1)
gestor.asignar_tarea(equipo1, tarea2, miembro2)

gestor.cambiar_estado(tarea1, "en progreso")

gestor.mostrar_tareas_miembro(miembro1)
gestor.tareas_pendientes_equipo(equipo1)
