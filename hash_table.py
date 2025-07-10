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
        self._pairs = capacity * [None]

    def __len__(self):
        return len(self._pairs)
        
    def __setitem__(self, key, value):
        self._pairs[self._index(key)] = (key, value)

    def __getitem__(self, key):
        pairs = self._pairs[self._index(key)]
        if pairs is None:
            raise KeyError(key)
        else:
            return pairs[1]

    def __contains__(self, key):
        try:
            self[key]
        except:
            return False
        else: 
            return True

    def __delitem__(self, key):
        if key in self:
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def get(self, key, default=None):
        try:
            self[key]
        except KeyError:
            return default
        
    def _index(self, key):
        indice = hash(key) % len(self)
        return indice

    @property
    def pairs(self):
        return [pair for pair in self._pairs if pair]

    @property
    def values(self):
        '''
        Esta función nos dará una lista de los valores que tiene la tabla hash,
        es igual a la función pairs, salvo que esta en vez de iterar sobre 
        la lista de elementos de la tabla hash, va a iterar sobre la función
        pairs, que este será una lista de tuplas de los elementos sin los None
        y de esas tuplas vamos a obtener el segundo valor que serán los valores.
        Esta función también tendrá @property así solo se pueda ver una copia 
        de los valores.
        '''
        return [value[1] for value in self.pairs]