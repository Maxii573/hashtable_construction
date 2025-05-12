from hash_table import Hashtable

def test_hash():
    assert Hashtable(capacity=100) is not None

def test_no_deberia_contener_valores_none():
    '''
    Este entraría en la fase roja, ya que las ranuras vacías estan conformadas
    por el valor None
    '''
    assert None not in Hashtable(capacity=100).values