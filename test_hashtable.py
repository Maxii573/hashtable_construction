from hash_table import Hashtable
import pytest


'''
Pero que pasaría si queremos obtener un valor por una clave que no se utilizo antes?
este no tendría un valor, podriamos utilizar el objeto en blanco antes visto
pero esta no es una buena opción, podríamos replicar un diccionario en Python, 
que levanta una excepción KeyError 
'''

def test_deberia_buscar_la_clave():
    '''
    Para buscar valores por claves, teniamos que utilizar el atributo .values, 
    si o si, pero ahora, vamos a implementar que se pueda buscar el valor
    por el operador in y sin ingresar al atributo .values.
    Utilizando este operador, vamos a buscarlo pero este nos tendría que retornar
    un booleano.
    Estaremos claramente en la fase roja ya que no está implementado el acceder
    a los valores con el operador in.
    '''
    hash_table = Hashtable(capacity=100)

    hash_table["Nombre"] = "Ana"

    assert "Ana" in hash_table.values
    assert "Edad" not in hash_table
    
    