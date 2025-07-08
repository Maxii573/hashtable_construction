from hash_table import Hashtable
import pytest

@pytest.fixture
def tabla_hash():
    tabla = Hashtable(capacity=100)
    tabla["Nombre"] = "Maxi"
    tabla["Edad"] = 19
    tabla["Pais"] = "Argentina"
    tabla["Acceso"] = True
    return tabla

def test_deberia_retornar_una_copia_de_los_pares(tabla_hash):
    '''
    En esta sección vamos a proteger nuestros datos. En la práctica, los métodos 
    de acceso nunca deberian filtrar su implementación interna al usuario
    ya que este puede alterar intencionalmente o voluntariamente. 
    En este caso,.pairs donde tiene todos los elementos,
    se expone como un atributo público.
    Para que esto no suceda deberíamos darle al usuario una copia defensiva para
    proteger atributos mutables de modificaciones externas.
    Claramanete estamos en la fase roja por que no se esta haciendo una copia 
    de pairs, se le está dando la implementación interna directamente.
    '''
    assert tabla_hash.pairs is not tabla_hash.pairs