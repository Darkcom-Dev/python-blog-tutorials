#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

"""
Polimorfismo con herencia:

Otra forma de implementar el polimorfismo en Python es mediante la herencia. 
Podemos crear una clase base que define un conjunto de métodos comunes, 
y luego crear subclases que hereden estos métodos y los sobrescriban con una implementación 
específica de la clase.

Por ejemplo, podemos crear una clase Shape que tenga un método area, y luego crear subclases 
como Rectangle y Circle que implementen su propio cálculo de área:
"""

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)

"""
En este ejemplo, las subclases Rectangle y Circle heredan el método area de la clase Shape 
y lo sobrescriben con una implementación específica de la clase. 
Luego, podemos crear objetos de estas subclases y tratarlos como si
"""