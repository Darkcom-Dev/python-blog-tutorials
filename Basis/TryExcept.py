#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TryExcept.py
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

class EqualNumberException(Exception):
	
	def __init__(self, mensaje):
		self.message = mensaje

def main(args):
	# https://www.w3schools.com/python/python_ref_exceptions.asp
	# ImportError = Fallo de importacion.
	# IndexError = un indice de una lista no existe.
	# NameError = una variable desconocida es utilizada.
	# SyntaxError = El codigo no puede ser analizado correctamente.
	# TypeError = El tipo de dato no corresponde.
	# ValueError = El tipo de dato es correcto, pero el valor es incorrecto.
	# ZeroDivisionError = Division por cero.
	# OSError = Error del sistema operativo.
	
	try:
		x = int(input("Ingrese un numero: "))
		print(x,"Es un numero entero")
		y = 12
		
		if x == y:
			raise EqualNumberException('Identicos')

	except ZeroDivisionError as zde:
		print(f"tipo: {type(zde)}, error: {zde}")
	except (ValueError,TypeError) as vte:
		print(f"tipo: {type(vte)}, error: {vte}")
	except NameError as ne:
		print(f"tipo: {type(ne)}, error: {ne}")
	except Exception as e:
		print(f'tipo: {type(e)}, error: {e}')
	else:
		print("No arrojo ninguna excepcion")
	finally:
		print(12/x)
		print("Esta linea se ejecuta si o si", "el valor de x es:",x)
		print('Continuamos'.center(30,'-'))
		
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
