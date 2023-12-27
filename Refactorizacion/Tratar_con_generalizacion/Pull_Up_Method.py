"""
# Pull Up Method

## Problema
Tus subclases tienen métodos que realizan trabajos similares.

## Solución
Hacer que los métodos sean idénticos y luego moverlos a la superclase correspondiente.

Pull Up Method - Antes
Pull Up Method - Después

## Por qué refactorizar
Las subclases crecieron y se desarrollaron independientemente una de otra, 
lo que provocó la aparición de campos y métodos idénticos (o casi idénticos).

## Beneficios
Elimina el código duplicado. Si necesita hacer cambios en un método, 
es mejor hacerlo en un solo lugar que tener que buscar todas las copias del 
método en las subclases.

Esta técnica de refactorización también se puede utilizar si, por alguna razón, 
una subclase redefine un método de la superclase pero realiza el mismo trabajo esencialmente.

## Cómo refactorizar
Investigue los métodos similares en las superclases. Si no son idénticos, 
formátelos para que coincidan entre sí.

Si los métodos usan un conjunto diferente de parámetros, coloque los parámetros 
en la forma que desee ver en la superclase.

- Copia el método a la superclase. 

- Aquí puede encontrar que el código del método utiliza campos y métodos 
que existen solo en las subclases y, por lo tanto, no están disponibles en la superclase. 
Para resolver esto, puedes:

- Para campos: use Pull Up Field o Encapsular Campo para crear getters y setters 
en las subclases; luego declare estos getters de forma abstracta en la superclase.

- Para métodos: use Pull Up Method o declare métodos abstractos para ellos en la 
superclase (tenga en cuenta que su clase se volverá abstracta si no lo era anteriormente).

- Elimine los métodos de las subclases.

- Verifique los lugares donde se llama al método. En algunos lugares, 
puede reemplazar el uso de una subclase con la superclase.
"""

"""
Cómo aplicar la técnica de refactorización "Pull Up Method":

Antes de la refactorización:

"""
class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, meow_sound):
        super().__init__(name)
        self.meow_sound = meow_sound

    def make_sound(self):
        return self.meow_sound

class Dog(Animal):
    def __init__(self, name, bark_sound):
        super().__init__(name)
        self.bark_sound = bark_sound

    def make_sound(self):
        return self.bark_sound

"""
En este ejemplo, tenemos una clase base `Animal` y dos subclases `Cat` y 
`Dog` que heredan de ella. 

Cada una de las subclases tiene un método `make_sound` que devuelve un sonido 
específico para esa subclase.

Sin embargo, podemos notar que los métodos `make_sound` de `Cat` y `Dog` 
son muy similares y que podríamos extraerlos a la clase base `Animal`.

Después de la refactorización:
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return self.sound

class Cat(Animal):
    def __init__(self, name, meow_sound):
        super().__init__(name, meow_sound)

class Dog(Animal):
    def __init__(self, name, bark_sound):
        super().__init__(name, bark_sound)

"""
En este nuevo ejemplo, hemos extraído el método `make_sound` de las subclases 
`Cat` y `Dog` y lo hemos movido a la clase base `Animal`. Además, 
hemos agregado un nuevo parámetro `sound` al constructor de `Animal`, 
para que pueda ser inicializado con el sonido apropiado para cada subclase.

Ahora, la subclase `Cat` y `Dog` pueden heredar el método `make_sound` de su clase base, 
lo que nos permite eliminar la duplicación de código y simplificar la implementación 
de nuestras clases.
"""