from hash_table import Hashtable
import pytest


'''
Pero que pasaría si queremos obtener un valor por una clave que no se utilizo antes?
este no tendría un valor, podriamos utilizar el objeto en blanco antes visto
pero esta no es una buena opción, podríamos replicar un diccionario en Python, 
que levanta una excepción KeyError 
'''
@pytest.fixture
def tabla():
    tabla_hash = Hashtable(capacity=3)
    tabla_hash["Ciudad"] = "Buenos Aires"
    tabla_hash["País"] = "Argentina"
    tabla_hash["Transporte"] = True
    return tabla_hash

def test_tabla(tabla):
    assert tabla["Ciudad"] == "Buenos Aires"
    assert tabla["País"] == "Argentina"
    assert tabla["Transporte"] == True

    