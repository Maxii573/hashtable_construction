from hash_table import Hashtable
import pytest

@pytest.fixture
def tabla_hash():
    hash_table = Hashtable(capacity=100)
    hash_table["Hola"] = "hello"
    return hash_table

def test_deberia_levantar_key_error_al_eliminar(tabla_hash):
    '''
    Estaremos el fase roja, ya que daría error por la clave que no se encuentra
    '''
    with pytest.raises(KeyError) as exception_info:
        del tabla_hash["missing_key"]
    assert exception_info.value.args[0] == "missing_key"






   