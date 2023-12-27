"""
# Pull Up Field

## Problema
Dos clases tienen el mismo campo.

## Solución
Eliminar el campo de las subclases y moverlo a la superclase.

Pull Up Field - Antes
Pull Up Field - Después

## Por qué refactorizar
Las subclases crecieron y se desarrollaron por separado, lo que provocó la aparición 
de campos y métodos idénticos (o casi idénticos).

## Beneficios
Elimina la duplicación de campos en las subclases.

Facilita la posterior reubicación de métodos duplicados, si existen, 
de las subclases a una superclase.

## Cómo refactorizar
- Asegúrese de que los campos se utilicen para las mismas necesidades en las subclases.

- Si los campos tienen nombres diferentes, déles el mismo nombre y reemplace todas las 
referencias a los campos en el código existente.

- Cree un campo con el mismo nombre en la superclase. 
Tenga en cuenta que si los campos eran privados, el campo de la superclase debería ser protegido.

- Elimine los campos de las subclases.

- Es posible que desee considerar el uso de Encapsular Campo para el nuevo campo, 
para ocultarlo detrás de métodos de acceso.
"""

"""
Técnica de refactorización "Pull Up Field":

Antes de la refactorización:
"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = None

    def start_engine(self):
        raise NotImplementedError()

class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def start_engine(self):
        print("Engine started for car.")

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load_weight):
        super().__init__(brand, model, year)
        self.max_load_weight = max_load_weight

    def start_engine(self):
        print("Engine started for truck.")

"""
En este ejemplo, `Car` y `Truck` heredan de `Vehicle` y tienen campos específicos 
(`color` y `max_load_weight`, respectivamente). Sin embargo, la clase base (`Vehicle`) 
también tiene un campo `fuel_type`, que no es relevante para los vehículos `Car` y `Truck`.

Después de la refactorización, podemos mover el campo `fuel_type` a una clase base común, 
como se muestra a continuación:

Después de la refactorización:
"""
class Vehicle:
    def __init__(self, brand, model, year, fuel_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def start_engine(self):
        raise NotImplementedError()

class Car(Vehicle):
    def __init__(self, brand, model, year, color, fuel_type):
        super().__init__(brand, model, year, fuel_type)
        self.color = color

    def start_engine(self):
        print("Engine started for car.")

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load_weight, fuel_type):
        super().__init__(brand, model, year, fuel_type)
        self.max_load_weight = max_load_weight

    def start_engine(self):
        print("Engine started for truck.")


"""
Ahora `fuel_type` se ha movido de la clase `Vehicle` a una clase base común. 
Esto hace que las clases `Car` y `Truck` sean más específicas y evita la duplicación 
de campos irrelevantes.
"""
