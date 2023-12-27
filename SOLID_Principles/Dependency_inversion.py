# Reversal dependancy

"""
The dependency must be in abstractions, not in concretions.
The modules of high level must be not depend of low level modules.
So much the low level classes like high level classes should depend
of the same abstractions.
The abstractions not should depend of the details.
The details should depend of abstractions
"""

class Connector():
	""" Class doc """
	def connect (self):
		""" Function doc """
		pass

class AuthenticationForUser():
	def __init__ (self, connector: Connector):
		""" Function doc """
		self.connection = connector.connect()
		
	def authenticate (self, credentials):
		""" Function doc """
		pass
		
	def is_authenticated (self):
		""" Function doc """
		pass
	
	def last_login (self):
		""" Function doc """
		pass
		
class AnonymousAuth(AuthenticationForUser):
	pass
		
class GithubAuth(AuthenticationForUser):
	""" Class doc """
	
	def last_login (self):
		""" Class initialiser """
		pass
		
class FacebookAuth(AuthenticationForUser):
	""" Class doc """
	pass
	
class Permissions():
	def __init__(self, auth: AuthenticationForUser):
		self.auth = auth
		
	def has_permissions (_):
		""" Function doc """
		pass
	
class IsLoggedInPermissions (Permissions):
	""" Class doc """
	
	def last_login ():
		""" Class initialiser """
		pass
		
"""
Arrive a point in the software development in that our applications is composed in a big part for modules.
When this happens, we must clarify the things using dependency inyection.
High level components depending of the low level components to work.
To create a especific behaviour, can use inheritance or interface tecniques

"""
