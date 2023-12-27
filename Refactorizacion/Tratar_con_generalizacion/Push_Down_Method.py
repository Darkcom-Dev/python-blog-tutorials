"""
# Push Down Method

## Problema
¿Se implementa un comportamiento en una superclase que es utilizado solo por una 
(o pocas) subclases?

## Solución
Mueva este comportamiento a las subclases.

Push Down Method - Antes
Push Down Method - Después

## Por qué refactorizar
Al principio, se pretendía que cierto método fuera universal para todas las clases, 
pero en realidad solo se utiliza en una subclase. 
Esta situación puede ocurrir cuando las funciones planificadas no se materializan.

Estas situaciones también pueden ocurrir después de la extracción parcial 
(o eliminación) de funcionalidades de una jerarquía de clases, 
dejando un método que solo se usa en una subclase.

Si ve que un método es necesario para más de una subclase, pero no todas, 
puede ser útil crear una subclase intermedia y mover el método a ella. 
Esto permite evitar la duplicación de código que resultaría de empujar 
un método hacia todas las subclases.

## Beneficios
Mejora la coherencia de la clase. Un método se encuentra donde se espera verlo.

## Cómo refactorizar
- Declare el método en una subclase y copie su código de la superclase.

- Elimine el método de la superclase.

- Encuentre todos los lugares donde se utiliza el método y verifique que 
se llame desde la subclase necesaria.
"""
"""
¡Claro! Aquí tienes un ejemplo en Python de Push Down Method:

Supongamos que tienes una clase `Vehicle` que tiene dos subclases `Car` y `Truck`. Ambas subclases tienen un método `drive`, pero el método `drive` es diferente para cada subclase. En este caso, el método `drive` debe ser empujado hacia abajo a las subclases, ya que no se usa en la superclase `Vehicle`.

Antes de refactorizar:

"""
class Vehicle:
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def drive(self):
        print("Driving car...")
        
class Truck(Vehicle):
    def drive(self):
        print("Driving truck...")


"""
Después de aplicar Push Down Method, la clase `Vehicle` ya no tendrá el método `drive`, 
y este método será movido a cada subclase correspondiente:
"""


class Vehicle:
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def drive(self):
        print("Driving car...")
        
class Truck(Vehicle):
    def drive(self):
        print("Driving truck...")



"""
Es importante asegurarse de que no se estén utilizando los métodos en la clase base 
antes de aplicar Push Down Method, ya que podría conducir a errores.
"""
