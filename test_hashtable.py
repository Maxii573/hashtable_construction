from hash_table import Hashtable
import pytest

def test_actualizar_valor():
    '''
    Ya que ya está implementado el actualizar un valor, vamos a ver diferentes 
    casos y si la tabla no disminuye la longitud, como ya está implementado y está
    bien, estaremos en la fase verde
    '''
    hash_table = Hashtable(capacity=100)
    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"
    assert hash_table["hola"] == "hallo"

    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100







   