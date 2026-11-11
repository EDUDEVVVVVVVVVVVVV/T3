class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        if nota < 0 or nota > 20:
            raise ValueError("La nota debe estar entre 0 y 20")
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return round(sum(self.notas) / len(self.notas), 2)

    def estado(self):
        if not self.notas:
            return "Sin notas"
        return "Aprobado" if self.promedio() >= 13 else "Desaprobado"


class SistemaAcademico:
    def __init__(self):
        self.estudiantes = {}

    def registrar_estudiante(self, codigo, nombre):
        if codigo in self.estudiantes:
            raise ValueError("El codigo ya existe")
        self.estudiantes[codigo] = Estudiante(codigo, nombre)

    def agregar_nota(self, codigo, nota):
        if codigo not in self.estudiantes:
            raise ValueError("Estudiante no encontrado")
        self.estudiantes[codigo].agregar_nota(nota)

    def listar(self):
        return list(self.estudiantes.values())