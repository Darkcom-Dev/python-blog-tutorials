"""
# Colapso de jerarquia

## Problema
Tienes una jerarquía de clases en la que una subclase es prácticamente igual que su superclase.

## Solución
Combina la subclase y la superclase.

## Por qué refactorizar
Tu programa ha crecido con el tiempo y una subclase y una superclase se 
han vuelto prácticamente iguales. Se eliminó una característica de una subclase, 
se movió un método a la superclase... y ahora tienes dos clases que se parecen mucho.

## Beneficios
Se reduce la complejidad del programa. Menos clases significan menos cosas que 
recordar y menos piezas móviles frágiles en las que preocuparse durante futuros 
cambios de código.

Es más fácil navegar por tu código cuando los métodos están definidos en una sola clase. 
No tienes que revisar toda la jerarquía para encontrar un método en particular.

## Cuándo no usar
¿La jerarquía de clases que estás refactorizando tiene más de una subclase? Si es así, 
después de que se complete la refactorización, las subclases restantes deben 
convertirse en herederas de la clase en la que se colapsó la jerarquía.

Pero ten en cuenta que esto puede llevar a violaciones del principio 
de sustitución de Liskov. 

Por ejemplo, si tu programa emula redes de transporte de la ciudad 
y accidentalmente colapsas la superclase Transport en la subclase Car, 
entonces la clase Plane puede convertirse en heredera de Car. ¡Ups!

## Cómo refactorizar
Selecciona qué clase es más fácil de eliminar: la superclase o su subclase.

Utiliza Pull Up Field y Pull Up Method si decides deshacerte de la subclase. 
Si eliges eliminar la superclase, utiliza Push Down Field y Push Down Method.

Reemplaza todos los usos de la clase que estás eliminando con la clase a la 
que se van a migrar los campos y métodos. A menudo, esto será el código para crear clases, 
la tipificación de variables y parámetros, y la documentación en los comentarios de código.

Elimina la clase vacía.
"""

"""
¡Claro! Aquí te muestro un ejemplo sencillo de cómo aplicar el refactoring "Collapse Hierarchy" en Python:

Antes:

"""
class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        return "Meow!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return "Woof!"

class Poodle(Dog):
    def __init__(self, name):
        super().__init__(name, "Poodle")

    def bark(self):
        return "Yip!"


"""Después:"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Cat:
    def __init__(self, name, color):
        self.animal = Animal(name)
        self.color = color

    def meow(self):
        return "Meow!"

    def get_name(self):
        return self.animal.get_name()

class Dog:
    def __init__(self, name, breed):
        self.animal = Animal(name)
        self.breed = breed

    def bark(self):
        return "Woof!"

    def get_name(self):
        return self.animal.get_name()

class Poodle(Dog):
    def __init__(self, name):
        super().__init__(name, "Poodle")

    def bark(self):
        return "Yip!"

"""
En este ejemplo, 
antes teníamos una jerarquía de clases Animal -> Cat, Animal -> Dog -> Poodle. 
Después de aplicar "Collapse Hierarchy", hemos eliminado la clase Animal y 
hemos reemplazado sus referencias en Cat y Dog con un objeto de Animal 
que se crea en el constructor. Esto simplifica la jerarquía de clases 
y reduce la complejidad del código.
"""