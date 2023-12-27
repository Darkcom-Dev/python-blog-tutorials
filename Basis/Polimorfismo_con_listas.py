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
Otro ejemplo de polimorfismo en Python puede ser cuando se trabaja con listas de diferentes 
tipos de objetos y se quiere realizar una operación en común en cada uno de ellos. 

Por ejemplo, supongamos que se tiene una lista con diferentes tipos de animales 
y se desea imprimir el sonido que hace cada uno de ellos. Se puede utilizar polimorfismo 
para llamar al método "hacer_sonido()" en cada uno de los objetos de la lista, 
sin importar el tipo de animal que sea:
"""

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muu")

lista_animales = [Perro(), Gato(), Vaca()]

for animal in lista_animales:
    animal.hacer_sonido()

"""
En este ejemplo, se crea una clase abstracta "Animal" con el método abstracto "hacer_sonido()". 
Luego, se crean las clases "Perro", "Gato" y "Vaca", que heredan de la clase "Animal" 
y sobreescriben el método "hacer_sonido()" con su propio sonido característico. 

Finalmente, se crea una lista con diferentes tipos de animales y se itera sobre ella, 
llamando al método "hacer_sonido()" en cada uno de ellos. Gracias al polimorfismo, 
se puede llamar al mismo método en cada objeto de la lista, aunque sean de diferentes clases, 
y cada uno responderá de manera diferente, imprimiendo su propio sonido característico.
"""
