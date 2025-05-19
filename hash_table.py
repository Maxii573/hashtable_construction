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
BLANK = object()

class Hashtable():
    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    def __len__(self):
        return len(self.values)
    
    def __setitem__(self, key, value):
        indice = hash(key) % len(self)
        self.values[indice] = value

    def __getitem__(self, key):
        '''
        Verificarémos si el valor es el mismo valor por defecto que tiene la
        tabla hash, utilizaremos el operador is en vez de ==, ya que vamos a 
        comparar sus identidades en vez de los valores.
        Si está todo okey, este retornará el valor dado.
        '''
        indice = hash(key) % len(self)
        if self.values[indice] is BLANK:
            raise KeyError(key)
        return self.values[indice]
