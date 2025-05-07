from hash_table import Hashtable

'''
En este archivo, vamos a testear utilizando pytest cada afunción que agregemos
a la clase Hashtable en el archivo "hash_table.py".
Esto estará sincronizado con git, para que se pueda ver mejor el historial
de la evolución de la clase Hashtable
Repositorio donde estará las versiones:
https://github.com/Maxii573/hashtable_construction
'''

def test_hash():
    '''
    Probaremos si el objeto no está vacío.
    Pytest dará verde ya que el objeto está inicializado 
    '''
    assert Hashtable is not None