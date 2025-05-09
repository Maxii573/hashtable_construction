# Construcción de un prototipo de tabla hash con TDD
'''
En esta sección, vamos a crear una tabla hash independientemente de los diccionarios
de Python. Vamos a implementar un diccionario con lo aprendido y imitando sus
características más importantes.

Las implementaciones básicas que hemos hecho anteriomente y estas tablas hash que 
vamos a implementar desde 0, no tienen un uso practico, como en lo laboral estos 
nunca se van a implementar ya que los diccionarios que trae Python son más
eficientes a la hora de implementar en temas de tiempo (No reinventamos la rueda),
Los diccionarios de Python ya están optimizados y probados con miles de casos reales 
y disminuyen las posibilidades de errores.

¿Cuando se utilizan?
Se utilizan en casos muy particulares, como sistemas embebidos o de bajo nivel, 
donde se necesita controlar cada milímetro de memoria o rendimiento como en C,
Hashing con requisitos criptográficos personalizados, optimización que las 
implementaciones estándar no permiten.

¿Para que aprendo entonces?
Aprendemos más que nada para saber como se comportan internamente las tablas hash
y así, saber cuando se utilizan.
También en entrevistas técnicas nos pueden preguntar como funcionan las tablas hash 
'''

# Propiedades de la implemetación de la tabla hash propia
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
    def __init__(self):
        '''
        Faltará el atributo size que lo utilizará en la función test_hash()
        '''
        pass