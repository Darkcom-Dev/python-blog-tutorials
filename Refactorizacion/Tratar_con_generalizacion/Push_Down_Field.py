
"""
# Push Down Field:

## Problema
¿Se utiliza un campo solo en algunas subclases?

## Solución
Mueve el campo a esas subclases.

Push Down Field - Antes
Push Down Field - Después

## ¿Por qué refactorizar?
Aunque se planeó utilizar un campo de manera universal para todas las clases, 
en realidad se utiliza solo en algunas subclases. Esta situación puede ocurrir 
cuando las características planificadas no se concretan, por ejemplo.

Esto también puede ocurrir debido a la extracción (o eliminación) 
de parte de la funcionalidad de las jerarquías de clases.

## Beneficios
Mejora la coherencia interna de la clase. Un campo se encuentra donde realmente se utiliza.

Al mover a varias subclases simultáneamente, se pueden desarrollar los campos 
de forma independiente. Esto crea duplicación de código, por lo que se deben 
empujar los campos solo cuando realmente se pretende utilizar los campos de diferentes formas.

## Cómo refactorizar
Declara un campo en todas las subclases necesarias.

Elimina el campo de la superclase.
"""

"""
Claro, aquí te muestro un ejemplo en Python de cómo aplicar la técnica de Push Down Field:

Supongamos que tenemos una clase llamada `Animal` que tiene dos subclases llamadas `Gato` 
y `Perro`. La clase `Animal` tiene un atributo llamado `especie` que es común a todas 
las subclases, pero la subclase `Perro` también tiene un atributo adicional llamado `raza`. 
Queremos aplicar la técnica de Push Down Field para mover el atributo `raza` de 
la subclase `Perro` a la clase `Animal`.

Aquí está el código inicial:

"""
class Animal:
    def __init__(self, especie):
        self.especie = especie

class Gato(Animal):
    def __init__(self, especie, nombre):
        super().__init__(especie)
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, especie, nombre, raza):
        super().__init__(especie)
        self.nombre = nombre
        self.raza = raza

"""
Para aplicar la técnica de Push Down Field, seguimos estos pasos:

1. Creamos un atributo `raza` en la clase `Animal` y eliminamos el atributo 
correspondiente en la subclase `Perro`.

2. Actualizamos el constructor de la subclase `Perro` para que utilice el 
constructor de la superclase y elimine la inicialización del atributo `raza`.

3. Actualizamos el constructor de la subclase `Gato` para que utilice el 
constructor de la superclase sin cambios.

Aquí está el código actualizado con la técnica de Push Down Field aplicada:
"""

class Animal:
    def __init__(self, especie, raza=None):
        self.especie = especie
        self.raza = raza

class Gato(Animal):
    def __init__(self, especie, nombre):
        super().__init__(especie)

class Perro(Animal):
    def __init__(self, especie, nombre):
        super().__init__(especie)
        self.nombre = nombre


"""
Ahora el atributo `raza` se ha movido de la subclase `Perro` a la superclase 
`Animal`, lo que simplifica el diseño y reduce la duplicación de código.
"""
