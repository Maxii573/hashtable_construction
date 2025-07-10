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

def test_no_deberia_contener_valor_none_cuando_se_crea(tabla_hash):
    '''
    Estaremos en la fase verde por que ya está implementado .value
    '''
    assert None not in Hashtable(capacity=100).values