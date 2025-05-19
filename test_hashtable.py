from hash_table import Hashtable
import pytest


'''
Pero que pasaría si queremos obtener un valor por una clave que no se utilizo antes?
este no tendría un valor, podriamos utilizar el objeto en blanco antes visto
pero esta no es una buena opción, podríamos replicar un diccionario en Python, 
que levanta una excepción KeyError 
'''

def test_should_raise_error_on_missing_key():
    '''
    utilizaremos un marco de construcción especial para probar excepciones, donde
    usaremos la función raises del módulo pytest en un gestor de contexto que 
    espera un tipo específico de excepción.
    Esto dará verde ya que el error se levantó ya que no hay un valor encontrado
    en la tabla.
    '''
    hash_table = Hashtable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

    