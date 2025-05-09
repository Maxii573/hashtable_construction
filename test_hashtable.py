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
    Se cambia de atributo a capacity.
    '''
    assert Hashtable(capacity=100) is not None

def test_view_capacity():
    '''
    Ahora, vamos a hacer que la función len() pueda funcionar en nuestra tabla hash.
    Este nos dará rojo ya que el objeto no tiene un len integrado.
    '''
    assert len(Hashtable(capacity=100)) == 100
