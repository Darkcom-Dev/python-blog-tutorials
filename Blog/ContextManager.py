#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ContextManager - and with.py
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

class ManejoRecursos:
	'''
	Esta es una clase personalizada el contexto de archivos.
	el bloque with hace esto sin que nos demos cuenta.
	esta clase es un simple ejemplo de como podemos sacarle algo de jugo.
	
	'''
	def __init__(self, nombre):
		self.nombre = nombre
		
	def __enter__(self):
		'''
		Cuando se usa la palabra reservada with, se llama automaticamente
		al metodo __enter__ de la clase object
		'''
		print('Abriendo el recurso'.center(50,'-'))
		self.nombre = open(self.nombre, 'r', encoding = 'utf8')
		return self.nombre

	def __exit__(self, tipo_excepcion, valor_excepcion, trazo_error):
		'''
		Cuando termina el bloque with, automaticamente se llama al
		metodo __exit__ de la clase object
		'''
		print('Cerrando el recurso'.center(50, '-'))
		if self.nombre:
			self.nombre.close()
		

def main(args):
	'''
	with es una manera simplificada de usar:
	
	try:
		archivo = open('pruebas.txt','r')
	except Exception as e:
		print(e)
	finally:
		archivo.close()
	
	'''
	with ManejoRecursos('pruebas.txt') as archivo:
		print(archivo.read())
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
