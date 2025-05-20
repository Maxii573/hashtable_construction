from hash_table import Hashtable
import pytest

@pytest.fixture
def tabla_hash():
    hash_table = Hashtable(capacity=100)
    hash_table["Hola"] = "hello"
    return hash_table

def test_deberia_eliminar_par_clave_valor(tabla_hash):
    '''
    Ya estaríamos en la fase verde por que implementamos en la tabla que se pueda
    eliminar pares de claves-valor utilizando la función integrada del
    '''
    assert "Hola" in tabla_hash
    assert "hello" in tabla_hash.values

    del tabla_hash["Hola"]

    assert "Hola" not in tabla_hash
    assert "hello" not in tabla_hash.values

    assert len(tabla_hash) == 100






   