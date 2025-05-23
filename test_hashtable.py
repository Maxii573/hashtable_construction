from hash_table import Hashtable
import pytest

@pytest.fixture
def tabla_hash():
    hash_table = Hashtable(capacity=100)
    hash_table["Hola"] = "hello"
    return hash_table

def test_deberia_levantar_key_error_al_eliminar(tabla_hash):
    '''
    Como vimos anteriormente, para saber si un valor está almacenado, nos fijabamos
    en el atributo .values en vez de la tabla en si y este es una lista, así que 
    Python automáticamente lo hace hasta sin que esté implementado el operador in
    '''
    assert "Hola" in tabla_hash
    assert "hello" in tabla_hash.values
    






   