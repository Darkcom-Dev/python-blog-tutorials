"""
The software entities (classes, modules, functions) must be open for
extension, not for modification.

Imagine that have a store and you give a discount of 20% to your 
favorite clients using this class:
when you decide offer a double disscount a the VIP clients. 
You can modify the class like this.
"""

# ============================================= #
# 				BAD EXAMPLE						#
# ============================================= #

class Discount:
	""" Class doc """
	
	def __init__ (self, costumer, price):
		""" Class initialiser """
		self.costumer = costumer
		self.price = price
	def give_discount (self):
		""" Function doc """
		if self.costumer == 'fav':
			return self.price * 0.2
		if self.costumer == 'vip':
			return self.price * 0.4
			
# ============================================= #
#				Solution						#
# ============================================= #

"""
This does not comply with OCP principles. The OCP forbiden
If we want give a new discount percent to a different type of costumer,
you see that add a new logic.
For that follow the OCP principles, add a new class that will extends
the discount. In this new class, implements your new behaviour
"""
			
class Discount:
	""" Class doc """
	
	def __init__ (self, costumer, price):
		""" Class initialiser """
		self.costumer = costumer
		self.price = price
	def get_discount (self):
		""" Function doc """
		return self.price * 0.2
class VIPDiscount(Discount):
	""" Class doc """
	
	def get_discount (self):
		""" Class initialiser """
		return super().get_discount() * 2
		
"""
If you decide an 80% percent of discount for VIP costumers, it should 
be like that
"""

class SuperVIPDiscount(VIPDiscount):
	""" Class doc """
	
	def get_discount (self):
		""" Class initialiser """
		return super().get_discount() * 2
