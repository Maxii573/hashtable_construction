# Propiedades de la implementación de la tabla hash propia
'''
Ahora, vamos a ver los requisitos que tendrá nuestra implementación de una tabla hash,
estos requisitos serán las características principales de nuestra tabla hash.

Nuestra tabla hash nos dejará:
- Crear una tabla hash vacía
- Insertar un par clave-valor en la tabla hash
- Eliminar un par clave-valor de la tabla hash
- Encontrar un valor por clave en la tabla hash
- Actualizar el valor asociado a una clave existente
- Comprobar si la tabla hash tiene una clave dada

Nuestra tabla hash va a tener otras características no escenciales pero que son
útiles específicamente, deberiamos poder:

- Crear una tabla hash a partir de un diccionario Python
- Crear una copia superficial de una tabla hash existente
- Devuelve el valor predeterminado si no se encuentra la cave correspondiente
- Informa el número de pares clave-valor almacenados en la tabla hash
- Haz que la tabla hash sea iterable
- Haga que la tabla hash sea comparable utilizando el operador de prueba de igualdad
- Mostrar una representación textual de la tabla hash
'''
class Hashtable():
    def __init__(self, capacity):
        '''
        En primer lugar, podríamos cambiar el nombre de la variable .value a .pairs
        ya que vamos a trabajar sobre artículos en ves de los valores en si
        '''
        self.pairs = capacity * [None]

    def __len__(self):
        return len(self.pairs)
    
    def __setitem__(self, key, value):
        '''
        Ya que vamos a implementar articulos, vamos a guardar los nuevos elementos
        por una tupla donde tendrá el par clave-valor.
        Tendremos que tener en cuenta que incialmente la lista tendrá 2 tipos de
        datos, las tuplas donde estará el par clave-valor y un objeto que 
        representará una ranura vacía.
        Ya que los datos de entrada estarán aisladas en las tuplas, ya no tendremos
        que utilizar un objeto especial para indicar una ranura vacía, asi que podremos
        utilizar None sin problemas, por que no va a interferir con el dato del usuario.
        '''
        self.pairs[self._index(key)] = (key, value)

    def __getitem__(self, key):
        '''
        Necesitaremos refactorizar el método especial __getitem__, donde solamente
        va cambiar lo que va a retornar, ya que la variable pair, es un None o 
        una tupla, si este es una tupla va a retornar el segundo elemento de la tupla
        que será el valor. Sino, va a levantar un KeyError.
        '''
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair[1]
    
    def __contains__(self, key):
        try:
            self[key]
        except:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    
    def __delitem__(self, key):
        '''
        Tendremos que cambiar la implementación del método especial __delitem__,
        ya que la nueva implementación del método especial __setitem__, asignará
        una tupla, y __delitem__ va a crear una tupla con None, y es lo que no queremos
        Ahora, vamos a cambiar la forma de buscar el elemento, que este elemento será
        una tupla y esta tupla se le sobreescribirá por un None.
        '''
        if key in self:
            self.pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def _index(self, key):
        indice = hash(key) % len(self)
        return indice

