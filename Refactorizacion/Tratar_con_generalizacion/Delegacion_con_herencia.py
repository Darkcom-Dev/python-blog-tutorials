"""
# Reemplazar Delegación con Herencia

## Problema
Una clase contiene muchos métodos simples que delegan todos los métodos de otra clase.

## Solución
Hacer que la clase sea una clase heredera delegada, 
lo que hace innecesarios los métodos de delegación.

Reemplazar Delegación con Herencia - Antes
Reemplazar Delegación con Herencia - Después

## Por qué Refactorizar
La delegación es un enfoque más flexible que la herencia, ya que permite cambiar 
cómo se implementa la delegación y colocar otras clases allí también. 

No obstante, la delegación deja de ser beneficiosa si delegas acciones 
a solo una clase y a todos sus métodos públicos.

En tal caso, si reemplazas la delegación con la herencia, limpias la clase 
de una gran cantidad de métodos de delegación y te ahorras tener que crearlos 
para cada nuevo método de clase delegado.

## Beneficios
Reduce la longitud del código. Todos estos métodos de delegación ya no son necesarios.

## Cuándo no usar
No use esta técnica si la clase contiene delegación solo a una parte de los 
métodos públicos de la clase delegada. 
Al hacerlo, violaría el principio de sustitución de Liskov.

Esta técnica solo se puede usar si la clase aún no tiene padres.

## Cómo Refactorizar
Haz que la clase sea una subclase de la clase delegada.

Coloca el objeto actual en un campo que contenga una referencia al objeto delegado.

Elimina los métodos con simple delegación uno por uno. Si sus nombres eran diferentes, usa Renombrar Método para darles a todos los métodos un solo nombre.

Reemplaza todas las referencias al campo delegado con referencias al objeto actual.

Elimina el campo delegado.
"""
"""
¡Por supuesto! Aquí te muestro un ejemplo en Python de cómo reemplazar la delegación con herencia:

Antes de la refactorización:

"""
class Printer:
    def __init__(self):
        self.print_engine = PrintEngine()

    def print(self, text):
        self.print_engine.print(text)

class PrintEngine:
    def print(self, text):
        print(text)

printer = Printer()
printer.print("Hello, world!")
"""

Después de la refactorización:

"""
class Printer(PrintEngine):
    pass

class PrintEngine:
    def print(self, text):
        print(text)

printer = Printer()
printer.print("Hello, world!")

"""

En este ejemplo, la clase `Printer` delega la tarea de imprimir en la clase `PrintEngine`. 
Pero como la clase `Printer` solo tiene un método que delega la llamada a la clase `PrintEngine`, 
es más fácil y más limpio simplemente hacer que la clase `Printer` herede de la clase `PrintEngine` 
y use su método `print` directamente. De esta manera, podemos eliminar el método `print` 
de la clase `Printer` y todo el código de delegación asociado.
"""