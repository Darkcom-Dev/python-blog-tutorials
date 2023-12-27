
'''
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
'''

class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas
	def __str__(self):
		return f'Vehiculo[Color: {self.color}, Ruedas: {self.ruedas}]'

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
	def __str__(self):
		return f'Coche[Velocidad: {self.velocidad}, {super().__str__()}]'

class Bicicleta(Vehiculo):
	def __init__(self,color, ruedas, tipo):
		super().__init__(color, ruedas)
		self.tipo = tipo
	def __str__(self):
		return f'Bicicleta[Tipo: {self.tipo}, {super().__str__()}]'


def main(args):
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
