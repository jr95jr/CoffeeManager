# tests/test_cliente.py
import pytest
from app.cliente import ClienteRepository

def test_crear_y_listar_clientes():
    repo = ClienteRepository()
    c1 = repo.crear("Juan Perez", telefono="777-111")
    c2 = repo.crear("María")
    lista = repo.listar()
    assert len(lista) == 2
    assert lista[0].nombre == "Juan Perez"
    assert repo.obtener(c1.id).telefono == "777-111"
