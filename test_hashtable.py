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
    una tabla hash debe contener una secuencia de valores, por ahora esta 
    secuencia será de tamaño fijo establecido en la creación de la tabla hash.
    Pytest dará rojo ya que el objeto no tiene el atributo size
    '''
    assert Hashtable(size=100) is not None