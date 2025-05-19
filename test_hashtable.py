from hash_table import Hashtable
import pytest


hash_table = Hashtable(capacity=100)
'''
Esto nos dará fase roja, ya que no está implementado el buscar elementos
por el método .get()
'''
def test_deberia_obtener_valor():
    assert hash_table.get("Hola") != "Hola"

def test_deberia_obtener_none_cuando_falta_clave():
    assert hash_table.get("clave faltante") is None

def test_deberia_obtener_default_valor_cuando_falta_la_clave():
    assert hash_table.get("Clave faltante", "default") == "default" 




    
    
    