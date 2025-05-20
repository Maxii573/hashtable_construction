from hash_table import Hashtable
import pytest


'''

'''
@pytest.fixture
def tabla_hash():
    hash_table = Hashtable(capacity=100)
    hash_table["Hola"] = "hello"
    return hash_table

def test_deberia_eliminar_par_clave_valor(tabla_hash):
    '''
    Esto estaría en la fase verde, pero el método especial que hemos agregado
    estaría reduciendo la lista, y como vimos anteriomente, esto no queremos.
    Así que nuevamente estaremos en la fase roja.
    '''
    assert "Hola" in tabla_hash
    assert "hello" in tabla_hash.values

    del tabla_hash["Hola"]

    assert "Hola" not in tabla_hash
    assert "hello" not in tabla_hash.values

    assert len(tabla_hash) == 100







    
    
    