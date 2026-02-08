# ===== CLASE CURSO =====
class Curso:
    def __init__(self, nombre, codigo, capacidad):
        self.nombre = nombre
        self.codigo = codigo
        self.capacidad = capacidad
        self.estudiantes = []  # ArrayList de estudiantes


# ===== CLASE ESTUDIANTE =====
class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.cursos = []  # ArrayList de cursos


# ===== CLASE UNIVERSIDAD =====
class Universidad:
    def __init__(self):
        self.cursos = []
        self.estudiantes = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def inscribir_estudiante(self, matricula, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                if len(curso.estudiantes) < curso.capacidad:
                    for est in self.estudiantes:
                        if est.matricula == matricula:
                            curso.estudiantes.append(est)
                            est.cursos.append(curso)
                            print("Estudiante inscrito correctamente")
                            return
                else:
                    print("Curso lleno")
                    return
        print("No se pudo inscribir")

    def dar_baja(self, matricula, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                for est in curso.estudiantes:
                    if est.matricula == matricula:
                        curso.estudiantes.remove(est)
                        est.cursos.remove(curso)
                        print("Estudiante dado de baja")
                        return
        print("No se pudo dar de baja")

    def mostrar_estudiantes_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                print(f"\nEstudiantes del curso {curso.nombre}:")
                for est in curso.estudiantes:
                    print(est.nombre)

    def mostrar_cursos_estudiante(self, matricula):
        for est in self.estudiantes:
            if est.matricula == matricula:
                print(f"\nCursos de {est.nombre}:")
                for curso in est.cursos:
                    print(curso.nombre)


# ===== PRUEBAS =====
uni = Universidad()

curso1 = Curso("Programación", "PRG101", 2)
curso2 = Curso("Base de Datos", "BD202", 1)

est1 = Estudiante("Carlos", "A01")
est2 = Estudiante("María", "A02")

uni.agregar_curso(curso1)
uni.agregar_curso(curso2)

uni.registrar_estudiante(est1)
uni.registrar_estudiante(est2)

uni.inscribir_estudiante("A01", "PRG101")
uni.inscribir_estudiante("A02", "PRG101")
uni.inscribir_estudiante("A02", "BD202")

uni.mostrar_estudiantes_curso("PRG101")
uni.mostrar_cursos_estudiante("A02")
