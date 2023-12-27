'''
En Python se puede eliminar cualquier variable u objeto, de hecho todos los
tipos de archivo comunies como int, str, float, list, etc son en realidad objetos.
'''

from abc import ABC, abstractmethod

class AbstractClass(ABC): # Abstract Base Class
	def __init__(self, C):
		if self.validate_attribute(C):
			self._c = C
		else:
			self._c = 0

	@property
	def c (self):
		return self._c

	@c.setter
	def c (self, C):
		if self.validate_attribute(C):
			self._c = C
		else:
			print(f"Error al validar: {C}")
			self._c = 0

	def validate_atribbute(self,attr):
		return True if 0 < attr < 100 else False

	@abstractmethod
	def calcular_area(self):
		'''
		Si una clase tiene un metodo abstracto, toda la clase se convierte en una clase abstracta.
		Una clase abstracta, no puede ser instanciada, por lo tanto no puede crear nuevos objetos a
		partir de el.
		'''
		pass


class TestClass(): # Es igual a TestClass(Object): porque todas las clases heredan de object.
	def __init__(self, A, B):
		self.a = A
		self.b = B


	def __del__(self):
		# Funcion especial que hereda de la clase Object
		print(f'fue eliminado A: {self.a}, B: {self.b}')

	def __str__(self):
		# Funcion especial que sobreescribe la informacion acerca de la clase.
		# Metodo heredado de object
		print(f'TestClass A: {self.a}, B: {self.b}')

print('Creacion de objetos'.center(50,'-')) # center, rellena caracteres a ambos lados del texto con un comodin, dejando el texto en el centro.
newObject = TestClass(12,24)
print(type(newObject)) # Imprime una direccion de memoria, si no tiene sobreescrita el metodo __str__
print(TestClass.mro()) # Method Resolution Order, devuelve el orden de como se ejecutan las herencias, util en herencia multiple.

print('Eliminacion de objetos'.center(50, '_'))
del newObject # Elimina todo tipo de objetos, incluso int, str, float, etc.
# Sin embargo no tenemos algo que nos diga si el objeto fue eliminado en tiempo de ejecucion.
# con el metodo __del__ de la clase, nos envia retroalimentacion del objeto cuando es eliminado.
