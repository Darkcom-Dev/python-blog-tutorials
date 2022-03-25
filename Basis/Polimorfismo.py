#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Polimorfismo.py
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
Polimorfismo: varias formas en tiempo de ejecucion.

Esa definicion no dice nada, por lo que puedo entender es que se puede 
acceder a variables de varias formas, aunque estas no esten en las 
clases hijas.
Y es una cualidad que se puede aprovechar solo en la herencia
'''

class Empleado:
	def __init__(self, nombre, sueldo):
		self.nombre = nombre
		self.sueldo = sueldo
		
	def __str__(self):
		return f'Empleado: [nombre: {self.nombre}, sueldo: {self.sueldo}]'
	'''El método mostrar detalles solo es perteneciente a la clase padre
		sin embargo puede ser accedido desde la clase hija como si le 
		perteneciera.
	'''
	def mostrar_detalles(self):
		return self.__str__()
		
class Gerente(Empleado):
	def __init__(self, nombre, sueldo, departamento):
		super().__init__(nombre, sueldo)
		self.departamento = departamento
		
	def __str__(self):
		return f'Gerente[departamento: {self.departamento}], {super().__str__()}'
		
	# def mostrar_detalles
	'''No es necesario un método mostrar detalles, poque seria exactamente
		igual a la del padre, seria como sobre escribir lo mismo.
	'''

def mostrar_detalles(objeto):
	print(type(objeto))
	print(objeto.mostrar_detalles())
	'''
	Se recomienda en python que los métodos sean lo mas genericas posibles
	por la naturaleza dinamica de python, por eso no se recomienda
	la funcion "isinstance()"
	
	Is Instance compara si el objeto es del tipo de una clase.(reflexivo)
	'''
	if isinstance(objeto, Gerente):
		print(objeto.departamento)

def main(args):
	empleado = Empleado('Juan', 5000)
	mostrar_detalles(empleado)
	gerente = Gerente('Karla', 12000, 'Sistemas')
	mostrar_detalles(gerente)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
