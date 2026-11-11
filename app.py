from gestion import SistemaAcademico


def mostrar_menu():
    print("\n=== SISTEMA DE GESTION ACADEMICA - INNOVATEC ===")
    print("1. Registrar estudiante")
    print("2. Agregar nota")
    print("3. Ver reporte")
    print("4. Salir")


def leer_nota():
    try:
        return float(input("Nota (0-20): "))
    except ValueError:
        raise ValueError("La nota debe ser un numero")


def main():
    sistema = SistemaAcademico()
    while True:
        mostrar_menu()
        try:
            opcion = input("Elige una opcion: ").strip()
            if opcion == "1":
                codigo = input("Codigo: ").strip()
                nombre = input("Nombre: ").strip()
                sistema.registrar_estudiante(codigo, nombre)
                print("Estudiante registrado.")
            elif opcion == "2":
                codigo = input("Codigo del estudiante: ").strip()
                nota = leer_nota()
                sistema.agregar_nota(codigo, nota)
                print("Nota agregada.")
            elif opcion == "3":
                estudiantes = sistema.listar()
                if not estudiantes:
                    print("No hay estudiantes registrados.")
                for e in estudiantes:
                    print(f"{e.codigo} | {e.nombre} | Notas: {e.notas} | "
                          f"Promedio: {e.promedio()} | {e.estado()}")
            elif opcion == "4":
                print("Hasta luego.")
                break
            else:
                print("Opcion invalida.")
        except ValueError as error:
            print("Error:", error)
        except EOFError:
            print("No hay entrada. En Docker usa: docker run -it")
            break


if __name__ == "__main__":
    main()