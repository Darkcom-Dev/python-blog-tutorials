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
En Python no existe un tipo de dato "interface" como tal, 
pero se puede simular una interfaz a través de una clase abstracta.

Para crear una interfaz en Python, primero necesitas importar el módulo abc 
(Abstract Base Classes). Luego, define una clase que herede de ABC. En esta clase, 
agrega uno o más métodos abstractos usando el decorador @abstractmethod. 
Los métodos abstractos no tienen cuerpo, simplemente incluyen la definición de la firma del método.

Aquí hay un ejemplo de cómo crear una interfaz para una clase de Animal:
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def eat(self, food):
        pass

"""
En este ejemplo, Animal es una interfaz con dos métodos abstractos: speak y eat. 
Cualquier clase que herede de Animal debe implementar estos dos métodos. 
Para implementar los métodos abstractos, debes crear una subclase que herede de la interfaz 
y definir los métodos abstractos.

Por ejemplo, aquí hay una clase Dog que implementa los métodos de Animal:
"""

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def eat(self, food):
        if food == "dog food":
            return "Yummy!"
        else:
            return "I don't like this food."

"""
En este ejemplo, Dog es una subclase de Animal que implementa los métodos abstractos speak y 
eat. La implementación de estos métodos es específica para la clase Dog.

Con esta estructura, puedes definir y utilizar interfaces en Python. 
Las interfaces son útiles para definir contratos de programación que deben seguirse 
por cualquier clase que implemente la interfaz.
"""