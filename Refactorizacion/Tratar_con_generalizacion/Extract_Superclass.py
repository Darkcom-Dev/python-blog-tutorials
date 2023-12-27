"""
# Extract Superclass:

# Problema
Tienes dos clases con campos y métodos comunes.

# Solución
Crea una superclase compartida para ellas y mueve todos los campos y métodos idénticos a ella.

# Por qué refactorizar
Un tipo de duplicación de código ocurre cuando dos clases realizan tareas 
similares de la misma manera, o realizan tareas similares de manera diferente. 
Los objetos ofrecen un mecanismo incorporado para simplificar tales situaciones a 
través de la herencia. 

Pero a menudo esta similitud pasa desapercibida hasta que se crean las clases, 
lo que requiere crear una estructura de herencia posteriormente.

## Beneficios
Deduplicación de código. Los campos y métodos comunes ahora "viven" en un solo lugar.

## Cuando no usar
No se puede aplicar esta técnica a clases que ya tienen una superclase.

## Cómo refactorizar
Crea una superclase abstracta.

Utiliza las técnicas Pull Up Field, Pull Up Method y Pull Up Constructor Body 
para mover la funcionalidad común a una superclase. Comienza con los campos, 
ya que además de los campos comunes, 
deberás mover los campos que se usan en los métodos comunes.

Busca lugares en el código cliente donde el uso de las subclases pueda ser 
reemplazado por tu nueva clase (como en las declaraciones de tipo).
"""

"""
Por supuesto, aquí tienes un ejemplo en Python de cómo utilizar la técnica 
Extract Superclass para refactorizar una clase que comparte atributos y 
métodos con otra clase:

Supongamos que tenemos dos clases, `Dog` y `Cat`, que tienen atributos y 
métodos comunes, como `name`, `age`, `eat()`, `sleep()`, y `make_sound()`. 
Aquí está el código original:

"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
    def make_sound(self):
        print("Woof!")
        

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
    def make_sound(self):
        print("Meow!")


"""
Podemos ver que estas dos clases tienen atributos y métodos comunes. 
Para evitar la duplicación de código y mejorar la legibilidad del código, 
podemos extraer una superclase llamada `Animal` que contenga los atributos 
y métodos compartidos. Aquí está el código refactorizado:

"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

"""
En este nuevo código, hemos creado una nueva clase llamada `Animal` que contiene 
los atributos y métodos comunes. 

Luego, hemos modificado las clases `Dog` y `Cat` para heredar de `Animal` 
utilizando la sintaxis `class Subclass(Superclass)`. 

Finalmente, hemos eliminado los atributos y métodos duplicados en `Dog` y `Cat`.

Ahora, si queremos crear una nueva clase `Bird` que tenga los mismos atributos 
y métodos que `Dog` y `Cat`, podemos simplemente heredar de `Animal` y 
definir el método `make_sound()` para que haga el sonido de un pájaro:
"""

class Bird(Animal):
    def make_sound(self):
        print("Chirp!")


"""
De esta manera, hemos utilizado la técnica Extract Superclass para simplificar 
nuestro código y hacerlo más legible y fácil de mantener.
"""
