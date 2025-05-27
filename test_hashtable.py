from hash_table import Hashtable
import pytest
@pytest.fixture
def tabla_hash():
    '''
    Ahora, lo que vamos a hacer es refactorizar. En nuestra tabla hash, solo vamos
    a poder manipular valores en una lista, no se guardan las claves, en los 
    diccionarios en python, podremos iterar sobre sus claves, valores o pares de 
    clave y valor llamados artículos (pairs), pero nuestra tabla hash no tiene
    esta capacidad de guardar las claves para iterar o manipular sobre artículos.
    '''
    tabla = Hashtable(capacity=30)
    tabla["Nombre"] = "Maxi"
    tabla["Edad"] = 19
    tabla["Pais"] = "Argentina"
    tabla["Acceso"] = True
    return tabla

def test_tabla(tabla_hash):
    assert ("Nombre", "Maxi") in tabla_hash
    assert ("Edad", 19) in tabla_hash
    assert ("Pais", "Argentina") in tabla_hash
    assert ("Acceso", "True") in tabla_hash

   