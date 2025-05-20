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
    Ahora, vamos a definir la eliminación de pares claves y valor, obviamente
    nos estaremos en la fase roja ya que nos dará error por que no está implementado
    en la tabla que se pueda eliminar claves con del.
    Algo importante es en la cuando buscamos en el atributo .values, ya que no 
    tendremos que definir nada, por que Python lo hace automaticamente ya que 
    tabla_hash.values es una lista, y tabla_hash está aplicando sobre nuestro
    objeto personalizado y no una lista interna.
    '''
    assert "Hola" in tabla_hash
    assert "hello" in tabla_hash.values

    del tabla_hash["Hola"]

    assert "Hola" not in tabla_hash
    assert "hello" not in tabla_hash.values








    
    
    