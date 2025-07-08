from hash_table import Hashtable
import pytest

@pytest.fixture
def tabla_hash():
    tabla = Hashtable(capacity=100)
    tabla["Nombre"] = "Maxi"
    tabla["Edad"] = 19
    tabla["Pais"] = "Argentina"
    tabla["Acceso"] = True
    return tabla

def test_deberia_retornar_una_copia_de_los_pares(tabla_hash):
    '''
    Ahora estaremos en la fase verde ya que este nos dará una copia de la lista interna
    '''
    assert tabla_hash.pairs is not tabla_hash.pairs