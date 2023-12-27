# Interface segregation principle

"""
Create interfaces of fine grane that it be especific of the costumer.
The costumers not should be obligated to depend of interfaces that not
use.
This principle take care of disvantages of implements bigger interfaces.

To ilustrate this completly. to go with a classic example because is it
very significative and easely comprensible.
"""

# =====================================	#
#				Classic example			#
# =====================================	#

class IShape:
	""" Class doc """
	
	def draw (self):
		""" Class initialiser """
		raise NotImplementedError
		
class Circle (IShape):
		""" Function doc """
		def draw (self):
			""" Function doc """
			pass
	
class Square(IShape):
	""" Class doc """
	
	def draw (self):
		""" Class initialiser """
		pass
		
class Rectangle(IShape):
	""" Class doc """
	
	def draw (self):
		""" Class initialiser """
		pass
		
"""
Other big trick is that in our entreprise logic, a single class can 
implement many interfaces if this is necesary. thus, can provide an 
unique implementation for all common methods between interfaces.
The segregated interfaces also we will obligate to think in our code
more from point of view of costumer, which will lead to a loosy coupling
and easy test. Thus, we has been enhanced our code for our costumers,
also we has been more easier to understanding, testing and implements
"""
