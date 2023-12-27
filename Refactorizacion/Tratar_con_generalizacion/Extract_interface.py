"""
# Extract interface

## Problema
Múltiples clientes están utilizando la misma parte de la interfaz de una clase. 
Otro caso: parte de la interfaz en dos clases es la misma.

## Solución
Mueva esta porción idéntica a su propia interfaz.

## Por qué refactorizar
Las interfaces son muy apropiadas cuando las clases juegan roles especiales 
en diferentes situaciones. Utilice "Extract Interface" para indicar explícitamente 
qué papel desempeña.

Otro caso conveniente surge cuando necesita describir las operaciones que 
realiza una clase en su servidor. 

Si se planea permitir eventualmente el uso de servidores de múltiples tipos, 
todos los servidores deben implementar la interfaz.

## Bueno saber
Hay cierta similitud entre "Extract Superclass" y "Extract Interface".

La extracción de una interfaz permite aislar solo las interfaces comunes, 
no el código común. En otras palabras, si las clases contienen código duplicado, 
extraer la interfaz no lo ayudará a deduplicar.

De todos modos, este problema se puede mitigar aplicando "Extract Class" 
para mover el comportamiento que contiene la duplicación a un componente separado 
y delegando todo el trabajo a él. 
Si el comportamiento común es grande, siempre puede utilizar "Extract Superclass". 
Esto es incluso más fácil, por supuesto, pero recuerde que si toma este 
camino solo obtendrá una clase principal.

## Cómo refactorizar
- Cree una interfaz vacía.

- Declare las operaciones comunes en la interfaz.

- Declare las clases necesarias como implementadoras de la interfaz.

- Cambie las declaraciones de tipo en el código del cliente para usar la nueva interfaz.
"""

"""
Un ejemplo en Python de cómo se puede aplicar el refactoring Extract Interface:

Antes del refactoring:

"""
class Car:
    def start_engine(self):
        pass
    
    def accelerate(self):
        pass
    
    def brake(self):
        pass


class ElectricCar(Car):
    def start_engine(self):
        raise NotImplementedError("Electric cars don't have engines!")
    
    def accelerate(self):
        print("Speeding up with electric motor...")
    
    def brake(self):
        print("Slowing down with regenerative braking...")


"""Después del refactoring:"""


class Car:
    def start_engine(self):
        pass
    
    def accelerate(self):
        pass
    
    def brake(self):
        pass


class ElectricCarInterface:
    def accelerate(self):
        pass
    
    def brake(self):
        pass
    

class ElectricCar(Car, ElectricCarInterface):
    def start_engine(self):
        raise NotImplementedError("Electric cars don't have engines!")
    
    def accelerate(self):
        print("Speeding up with electric motor...")
    
    def brake(self):
        print("Slowing down with regenerative braking...")

"""
En este ejemplo, 
hemos creado una nueva interfaz llamada `ElectricCarInterface` que define los métodos 
`accelerate` y `brake`. 

Luego, hemos hecho que la clase `ElectricCar` implemente esta interfaz en lugar 
de heredar directamente de `Car`. 

Ahora, cualquier clase que quiera utilizar el comportamiento específico de 
los autos eléctricos puede implementar `ElectricCarInterface` en lugar de heredar 
de `ElectricCar`. 

Esto ayuda a reducir la dependencia de la jerarquía de clases y hace que el 
código sea más modular y fácil de mantener.
"""