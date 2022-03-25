#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Clases_POO.py
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

class Persona:
	
	# Esta es una variable de clase, para declararla, solo basta que esté fuera de cualquier metodo
	# Las variables de clase pueden ser accedidas desde la misma clase o desde las instancias de objetos.
	
	variable_clase = "Variable de clase"

	# Un metodo estatico nunca podra acceder directamente a una variable de clase.
	# Un metodo estatico NUNCA podra acceder a una variable de instancia.
	@staticmethod
	def metodo_estatico():
		print(f'Accediendo desde el metodo estatico: {Persona.variable_clase}')

	# Un metodo de clase puede acceder a una variable de clase sin problema
	# Un metodo de clase NUNCA podrá acceder a una variable de instancia.
	@classmethod
	def metodo_clase(cls):
		print(f'Accediendo desde el metodo de clase: {cls.variable_clase}')

	def __init__(self,nombre,apellido,edad):
		self.__nombre = nombre
		self.__apellido = apellido
		self.__edad = edad
		
	# Getters
	@property
	def nombre(self):
		return self.__nombre
	
	@property
	def apellido(self):
		return self.__apellido
		
	@property
	def edad(self):
		return self.__edad
	
	# Setters
	
	@nombre.setter
	def nombre(self,nombre):
		self.__nombre = nombre
		
	@apellido.setter
	def apellido(self,apellido):
		self.__apellido = apellido
		
	@edad.setter
	def edad(self, edad):
		self.__edad = edad
	
	def mostrar(self):
		print(f'Nombre: {self.__nombre} Apellido: {self.__apellido} Edad: {self.__edad}')

def main(args):
	cliente1 = Persona('Juan','Perez',28)
	cliente1.mostrar()
	cliente1.nombre = 'Juan Camilo'
	cliente1.mostrar()
	print(cliente1.nombre)

	print(f'Accediendo desde la clase: {Persona.variable_clase}')
	print(f'Accediendo desde el objeto: {cliente1.variable_clase}')
	Persona.metodo_estatico()
	Persona.metodo_clase()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
