#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

Supongamos que se tiene una clase "Figura" con dos métodos: 
"calcular_area()" y "calcular_perimetro()". Luego, se crean dos clases hijas, 
"Rectangulo" y "Circulo", que heredan de "Figura" y sobreescriben los métodos 
"calcular_area()" y "calcular_perimetro()" con su propia fórmula para calcular 
el área y el perímetro. 

Por último, se crea una función "calcular()" que recibe un objeto de tipo "Figura" 
y llama a los métodos "calcular_area()" y "calcular_perimetro()" de manera polimórfica, 
sin importar si el objeto es de tipo "Rectangulo" o "Circulo". 

"""

class Figura:
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14 * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

def calcular(figura):
    print("El área es:", figura.calcular_area())
    print("El perímetro es:", figura.calcular_perimetro())

rectangulo = Rectangulo(10, 5)
circulo = Circulo(7)

calcular(rectangulo)
calcular(circulo)

"""
En este ejemplo, se crea una clase abstracta "Figura" con dos métodos abstractos 
"calcular_area()" y "calcular_perimetro()". Luego, se crean las clases hijas "Rectangulo" 
y "Circulo", que heredan de "Figura" y sobreescriben los métodos abstractos con su propia 
fórmula para calcular el área y el perímetro. 

Por último, se crea una función "calcular()" que recibe un objeto de tipo "Figura" y 
llama a los métodos "calcular_area()" y "calcular_perimetro()" de manera polimórfica, 
sin importar si el objeto es de tipo "Rectangulo" o "Circulo". 

Se crea un objeto "Rectangulo" y un objeto "Circulo" y se pasan como argumento a la 
función "calcular()", que llamará a los métodos correspondientes de manera polimórfica, 
imprimiendo el área y el perímetro de cada figura.
"""
