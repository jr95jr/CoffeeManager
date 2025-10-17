import pytest
from app.cliente import ClienteRepository

@pytest.fixture
def repo():
    return ClienteRepository()

def test_crear_cliente_valido(repo):
    cliente = repo.crear("Juan Perez", "juan@example.com", "777-111", "Calle Falsa 123")
    assert cliente.id is not None
    assert cliente.nombre == "Juan Perez"

def test_crear_cliente_duplicado(repo):
    repo.crear("Maria", "maria@example.com")
    cliente2 = repo.crear("Maria", "maria@example.com")  # duplicado
    assert cliente2 is None

def test_listar_clientes(repo):
    repo.crear("Carlos", "carlos@example.com")
    clientes = repo.listar()
    assert len(clientes) >= 1

def test_obtener_cliente(repo):
    cliente = repo.crear("Ana", "ana@example.com")
    encontrado = repo.obtener(cliente.id)
    assert encontrado.nombre == "Ana"
