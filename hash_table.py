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
        Agregando un guion bajo al atributo .pairs, habermos que el usuario no
        pueda manipular la lista interna pero nosotros queremos que el usuario
        pueda ver pero sin manipular nada, para ello crearemos el método pairs
        '''
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
        '''
        Para imitar aun más el método dict.items(), podríamos no incluir los 
        espacios en blanco, en este caso, la copia nos retornaria los pares 
        de valores y lo espacios en blanco que serían None's.
        Ya no deberiamos crear una lista con el método .copy() ya que la 
        list comprehension ya la crea y retorna
        '''
        return [pair for pair in self._pairs if pair]

