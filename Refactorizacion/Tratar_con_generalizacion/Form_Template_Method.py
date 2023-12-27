
"""
# Form Template Method

## Problema
Tus subclases implementan algoritmos que contienen pasos similares en el mismo orden.

## Solución
Mueve la estructura del algoritmo y los pasos idénticos a una superclase y 
deja la implementación de los pasos diferentes en las subclases.

## Por qué refactorizar
Las subclases se desarrollan en paralelo, a veces por diferentes personas, 
lo que lleva a la duplicación de código, errores y dificultades en el 
mantenimiento del código, ya que cada cambio debe realizarse en todas las subclases.

## Beneficios
La duplicación de código no siempre se refiere a casos de simple copiar y pegar. 
A menudo, la duplicación ocurre a un nivel superior, como cuando tienes un 
método para ordenar números y un método para ordenar colecciones de objetos 
que solo se diferencian por la comparación de elementos. 

Crear un método de plantilla elimina esta duplicación fusionando los pasos 
de algoritmo compartidos en una superclase y 
dejando solo las diferencias en las subclases.

La formación de un método de plantilla es un ejemplo del principio Abierto/Cerrado en acción. 
Cuando aparece una nueva versión del algoritmo, solo necesitas crear una nueva subclase; 
no se requieren cambios en el código existente.

## Cómo refactorizar
Divide los algoritmos en las subclases en sus partes constituyentes 
descritas en métodos separados. Extract Method puede ayudar con esto.

Los métodos resultantes que son idénticos para todas las subclases se 
pueden mover a una superclase a través de Pull Up Method.

A los métodos no similares se les pueden dar nombres consistentes a través de Rename Method.

Mueve las firmas de los métodos no similares a una superclase como métodos 
abstractos mediante Pull Up Method. Deja sus implementaciones en las subclases.

Y finalmente, mueve el método principal del algoritmo a la superclase. 
Ahora debería funcionar con los pasos del método descritos en la superclase, 
tanto reales como abstractos.
"""

"""
Sí, aquí tienes un ejemplo en Python que ilustra cómo se puede aplicar el 
patrón Form Template Method:

Antes:

"""
class BaseClass:
    def process(self):
        self.step1()
        self.step2()
        self.step3()

class SubClass1(BaseClass):
    def step1(self):
        print("Subclass 1, Step 1")

    def step2(self):
        print("Subclass 1, Step 2")

    def step3(self):
        print("Subclass 1, Step 3")


class SubClass2(BaseClass):
    def step1(self):
        print("Subclass 2, Step 1")

    def step2(self):
        print("Subclass 2, Step 2")

    def step3(self):
        print("Subclass 2, Step 3")

"""Después:"""

class BaseClass:
    def process(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        raise NotImplementedError()

    def step2(self):
        raise NotImplementedError()

    def step3(self):
        raise NotImplementedError()


class SubClass1(BaseClass):
    def step1(self):
        print("Subclass 1, Step 1")

    def step2(self):
        print("Subclass 1, Step 2")

    def step3(self):
        print("Subclass 1, Step 3")


class SubClass2(BaseClass):
    def step1(self):
        print("Subclass 2, Step 1")

    def step2(self):
        print("Subclass 2, Step 2")

    def step3(self):
        print("Subclass 2, Step 3")

"""
En este ejemplo, la clase BaseClass define el método process, 
que llama a los métodos step1, step2 y step3. 

En la implementación original, estas funciones se definen en cada subclase. 

En la implementación refactorizada, se definen como métodos abstractos en la clase BaseClass. 

Cada subclase implementa los métodos step1, step2 y step3 según sea necesario. 

Como resultado, la lógica compartida se ha extraído a la clase BaseClass, 
lo que reduce la duplicación de código y facilita el mantenimiento del código.
"""