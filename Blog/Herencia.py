#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Herencia.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
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
