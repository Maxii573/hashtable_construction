from hash_table import Hashtable
import pytest

def test_deberia_buscar_la_clave():
    '''
    Ahora podremos verificar si un valor está en la tabla y estaremos en la 
    fase verde.
    '''
    hash_table = Hashtable(capacity=100)

    hash_table["Nombre"] = "Ana"

    assert "Ana" in hash_table.values
    assert "Edad" not in hash_table
    
    