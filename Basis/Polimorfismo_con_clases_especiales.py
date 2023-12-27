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
El polimorfismo es un concepto de programación orientada a objetos que se refiere 
a la capacidad de los objetos de diferentes clases para ser tratados como si fueran del mismo 
tipo de objeto. 

En Python, el polimorfismo se puede implementar de varias maneras, 
como por ejemplo mediante la herencia y los métodos especiales de Python.

Aquí hay algunos ejemplos de polimorfismo en Python:

Polimorfismo con métodos especiales de Python
Los métodos especiales de Python, también conocidos como "métodos mágicos", 
permiten a las clases definir comportamientos específicos al ser utilizadas en 
operaciones predefinidas de Python, como la suma (+), la comparación (==), 
la indexación ([]), entre otras. 

Esto hace posible que los objetos de diferentes clases puedan ser tratados de la misma manera.

Por ejemplo, podemos crear una clase Animal que tenga un método especial __str__ 
que permita imprimir una representación de texto del objeto. Luego, 
podemos crear subclases de Animal como Dog y Cat, que también implementen el método __str__:
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"I am an animal named {self.name}."


class Dog(Animal):
    def __str__(self):
        return f"I am a dog named {self.name}."


class Cat(Animal):
    def __str__(self):
        return f"I am a cat named {self.name}."
"""
En este ejemplo, las subclases de Animal sobrescriben el método __str__ 
para imprimir una descripción específica de la clase.

Luego, podemos crear objetos de estas clases y tratarlos como si fueran del mismo tipo de objeto:
"""

animals = [Animal("Bob"), Dog("Fido"), Cat("Whiskers")]

for animal in animals:
    print(animal)

"""
En este ejemplo, animals es una lista que contiene objetos de diferentes clases. 
Sin embargo, al recorrer la lista y llamar al método __str__ de cada objeto, 
Python utiliza la versión correspondiente de la subclase para imprimir una descripción 
específica de cada objeto.
"""