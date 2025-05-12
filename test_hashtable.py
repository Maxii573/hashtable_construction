from hash_table import Hashtable
import pytest


'''
En este ejemplo, se le dará varios elementos de pares clave-valor, ya que la 
la tabla hash no tiene implementado un recolector de elementos, este nos dará
error y entraremos en la fase roja
'''
@pytest.fixture
def hash_table():
    sample_data = Hashtable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True