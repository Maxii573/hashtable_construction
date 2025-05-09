from hash_table import Hashtable

def test_hash():
    assert Hashtable(capacity=100) is not None

def test_view_capacity():
    '''
    Vamos a agregar pares de claves y valores como un diccionario común
    Obviamente estará en fase roja, ya que no está implementado el almacenar
    items
    '''
    # Give
    hash_table = Hashtable(capacity=100)

    # When 
    hash_table["Nombre"] = "Ana"
    hash_table["Edad"] = 32
    hash_table["Acceso"] = True 

    # Then

    assert "Ana" in hash_table.values
    assert 32 in hash_table.values
    assert True in hash_table.values