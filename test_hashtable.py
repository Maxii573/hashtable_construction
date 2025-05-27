from hash_table import Hashtable
import pytest

@pytest.fixture
def tabla_hash():
    '''
    Ahora estaremos en la fase verde ya que los elementos se almacenarán en pares
    de clave-valor
    '''
    tabla = Hashtable(capacity=100)
    tabla["Nombre"] = "Maxi"
    tabla["Edad"] = 19
    tabla["Pais"] = "Argentina"
    tabla["Acceso"] = True
    return tabla

def test_tabla(tabla_hash):
    assert ("Nombre", "Maxi") in tabla_hash.pairs
    assert ("Edad", 19) in tabla_hash.pairs
    assert ("Pais", "Argentina") in tabla_hash.pairs
    assert ("Acceso", True) in tabla_hash.pairs

    assert len(tabla_hash) == 100

def test_no_deberia_contener_el_valor_none_cuando_se_crea():
    '''
    En esta prueba, vamos a verificar que cuando se crea tabla hash, este no tenga
    None predeterminado como valor en una tupla. Esto nos ayudará a prevenir el 
    problema de que el valor None de las ranuras vacías no se mezclen con el None 
    del usuario.
    '''
    hash_table = Hashtable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values

def test_deberia_eliminar_par_clave_valor(tabla_hash):
    assert "Nombre" in tabla_hash
    assert ("Nombre", "Maxi") in tabla_hash.pairs

    del tabla_hash["Nombre"]
    
    assert "Nombre" not in tabla_hash
    assert ("Nombre", "Maxi") not in tabla_hash.pairs
    assert len(tabla_hash) == 100
    