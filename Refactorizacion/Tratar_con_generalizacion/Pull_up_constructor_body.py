"""
# Pull Up Constructor Body

## Problema
Tus subclases tienen constructores con código que es en su mayoría idéntico.

## Solución
Crea un constructor en la superclase y mueve el código que es igual en las subclases a él. 
Llama al constructor de la superclase en los constructores de las subclases.


class Manager extends Employee {
  public Manager(String name, String id, int grade) {
    this.name = name;
    this.id = id;
    this.grade = grade;
  }
  // ...
}
class Manager extends Employee {
  public Manager(String name, String id, int grade) {
    super(name, id);
    this.grade = grade;
  }
  // ...
}

## ¿Por qué refactorizar?
¿Cómo es diferente esta técnica de refactorización de "Pull Up Method"?

En Java, las subclases no pueden heredar un constructor, por lo que no 
se puede simplemente aplicar "Pull Up Method" al constructor de la subclase 
y eliminarlo después de eliminar todo el código del constructor a la superclase. 

Además de crear un constructor en la superclase, es necesario tener constructores 
en las subclases con una simple delegación al constructor de la superclase.

En C++ y Java (si no llamaste explícitamente al constructor de la superclase), 
el constructor de la superclase se llama automáticamente antes del constructor 
de la subclase, lo que hace necesario mover el código común solo desde el 
comienzo de los constructores de las subclases (ya que no podrás llamar al 
constructor de la superclase desde un lugar arbitrario en un constructor de la subclase).

En la mayoría de los lenguajes de programación, un constructor de una subclase 
puede tener su propia lista de parámetros diferente de los parámetros de la superclase. 
Por lo tanto, debes crear un constructor de superclase solo con los parámetros 
que realmente necesita.

## Cómo refactorizar
- Crea un constructor en la superclase.

- Extrae el código común desde el principio del constructor de cada subclase 
hacia el constructor de la superclase. 

Antes de hacerlo, intenta mover tanto código común como 
sea posible al principio del constructor.

- Coloca la llamada al constructor de la superclase en la primera línea 
de los constructores de las subclases.
"""
"""
Aquí hay un ejemplo en Python de Pull Up Constructor Body:

Antes del refactoring:

"""
class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.color = None
        self.fuel = None
        self.engine_running = False
        self.lights_on = False
        self.speed = 0

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, sunroof):
        self.num_doors = num_doors
        self.sunroof = sunroof
        super().__init__(make, model, year, weight)

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, num_axles, cargo_capacity):
        self.num_axles = num_axles
        self.cargo_capacity = cargo_capacity
        super().__init__(make, model, year, weight)


"""Después del refactoring:"""


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.color = None
        self.fuel = None
        self.engine_running = False
        self.lights_on = False
        self.speed = 0

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, sunroof):
        self.num_doors = num_doors
        self.sunroof = sunroof
        super().__init__(make, model, year, weight)

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, num_axles, cargo_capacity):
        self.num_axles = num_axles
        self.cargo_capacity = cargo_capacity
        super().__init__(make, model, year, weight)


"""
En este ejemplo, se puede ver que el constructor de la clase `Vehicle` 
inicializa varios atributos comunes a todos los vehículos. 
Después de aplicar el refactoring Pull Up Constructor Body, 
estos atributos se inicializan en la superclase, y las subclases solo necesitan 
inicializar los atributos específicos de cada subclase. 

Esto evita la duplicación de código y hace que el código sea más fácil de mantener.
"""
