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
    En el archivo TDD.py explico como hay que desmenuzar un poco la función test
    para que sea más legible y claro los pasos de prueba. en este caso lo podemos
    hacer de esta forma:
    '''
    # assert Hashtable(capacity=3).values == [None, None, None]

    '''
    Pero una forma más estructurada y más legible es utilizando el método de prueba
    (Give-When-Then) (Dado-Cuando-Entonces) que lo vimos en el archivo TDD.py
    '''
    # Give
    lista_valores = [None, None, None]
    tabla_hash = Hashtable(capacity=3)

    # When 
    valores_tabla_hash = tabla_hash.values 

    # Then
    assert valores_tabla_hash == lista_valores 
