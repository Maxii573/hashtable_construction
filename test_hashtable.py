from hash_table import Hashtable


def test_deberia_insertar_valores_none():
    '''
    Ahora podremos insertar valores None sin que se mezclen con las ranuras vacías
    '''
    hash_table = Hashtable(capacity=100)
    hash_table["Key"] = None
    assert None in hash_table.values