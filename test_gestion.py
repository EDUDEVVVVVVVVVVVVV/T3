import pytest
from gestion import Estudiante, SistemaAcademico


def test_promedio():
    e = Estudiante("U001", "Ana")
    e.agregar_nota(10)
    e.agregar_nota(20)
    assert e.promedio() == 15


def test_sin_notas():
    assert Estudiante("U001", "Ana").estado() == "Sin notas"


def test_aprobado():
    e = Estudiante("U001", "Ana")
    e.agregar_nota(15)
    assert e.estado() == "Aprobado"


def test_desaprobado():
    e = Estudiante("U001", "Ana")
    e.agregar_nota(8)
    assert e.estado() == "Desaprobado"


def test_nota_invalida():
    e = Estudiante("U001", "Ana")
    with pytest.raises(ValueError):
        e.agregar_nota(25)


def test_registrar_y_agregar_nota():
    s = SistemaAcademico()
    s.registrar_estudiante("U001", "Ana")
    s.agregar_nota("U001", 16)
    assert s.estudiantes["U001"].notas == [16]


def test_codigo_duplicado():
    s = SistemaAcademico()
    s.registrar_estudiante("U001", "Ana")
    with pytest.raises(ValueError):
        s.registrar_estudiante("U001", "Luis")


def test_estudiante_inexistente():
    s = SistemaAcademico()
    with pytest.raises(ValueError):
        s.agregar_nota("U999", 15)