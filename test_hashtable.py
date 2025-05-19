from hash_table import Hashtable
import pytest


hash_table = Hashtable(capacity=100)
'''
Ahora, deberíamos obtener los valores por el atributo .get(), donde 
podremos especificarle un valor por default si no existe el valor, o 
retornar el valor si está el valor.
'''
def test_deberia_obtener_valor():
    assert hash_table.get("Hola") != "Hola"

def test_deberia_obtener_none_cuando_falta_clave():
    assert hash_table.get("clave faltante") is None

def test_deberia_obtener_default_valor_cuando_falta_la_clave():
    assert hash_table.get("Clave faltante", "default") == "default" 




    
    
    