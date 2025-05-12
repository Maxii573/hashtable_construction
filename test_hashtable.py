from hash_table import Hashtable
import pytest


'''
Vamos a utilizar el decorador .fixture para simplificar y no reescribir código.
en el archivo TDD.py está mejor explicado.
En este caso, entraríamos a la fase verde ya que los valores introducidos ya
los podremos obtener gracias al método especial __getitem__
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
