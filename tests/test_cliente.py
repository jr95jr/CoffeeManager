import pytest
from app.cliente import ClienteRepository

@pytest.fixture
def repo():
    return ClienteRepository()

def test_agregar_cliente(repo):
    cliente = repo.agregar_cliente("Test User", "test@example.com", "000", "Direccion Test")
    assert cliente.id is not None
    assert cliente.nombre == "Test User"
