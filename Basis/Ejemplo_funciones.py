#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejemploFunciones.py
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

def sumar(*sumandos):
	return sum(sumandos)

def main(args):
	resultado = sumar(10,5)
	print(resultado)
	resultado = sumar(10,5,21,34,12)
	print(resultado)
	resultado = sumar()
	print(resultado)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
