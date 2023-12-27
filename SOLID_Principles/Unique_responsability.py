# Below is given a class which has two responsabilities

'''
The principle of unique responsibility require that a class only have a job.
then, if a class contain more than one responsability, is link up.
Un change in a unique responsability offer like result the modification 
of responsability.
'''

### ==================================================###
# -			BAD EXAMPLE									#
### ==================================================###

class User:
	""" Has a user class that is responsable for both user properties, 
	how the users database.
	
	If the aplication change of manner that affect the administration 
	database functions.
	
	The classes that make use of the properties of user shall modify and
	recompile for new changes. Is like a dominoes effect, touch a piece
	and afect all the rest
	 """
	
	def __init__ (self, name: str):
		""" Class initialiser """
		self.name = name
		
	def get_name(self) -> str:
		pass
		
	def save (self, user: User):
		""" Function doc """
		pass

### ================================================= ###
# -					Solution							#
### ================================================= ###

"""
Then simply divide the class, we create other class that will handle the
responsability of save a user in a database
"""

class User:
	""" Class doc """
	
	def __init__ (self, name: str):
		""" Class initialiser """
		self.name = name
		
	def get_name (self):
		""" Function doc """
		pass
		
class UserDB:
	""" Class doc """
	
	def get_user (self, id) -> User:
		""" Class initialiser """
		pass
		
	def save (self, user: User):
		""" Function doc """
		pass
"""
A comun solution to this dilem is apply a Facade pattern.
For a intro a facade pattern see: 
The user class will be the facade for the management of user database and
user properties.
"""
