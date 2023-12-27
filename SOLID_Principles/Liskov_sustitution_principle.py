"""
The main idea behind of Liskov sustitution principle is that, for any
class, a costumer should be use any of the subtypes of indistinguishable 
manner, without even noticing, and therefore, without engage desired 
behaviour in execution time. its mean that the costumers has been isolated and 
unware the changes in the class hierarchy.


more formely:

to be q(x) a demonstrable property over x objects of type T. Then q(y)
should be demonstrable for y objects of type S is a subtype of T

In simple terms, mean that a subclass, child or especializad of the object
or class must be suitable for your father or superclass
"""

# =============================================	#
# 					BAD EXAMPLE					#
# =============================================	#

class User(): #???? por que hay parentesis si no hay herencia?
	""" Class doc """
	
	def __init__ (self, color, board):
		""" Class initialiser """
		create_pieces()
		self.color = color
		self.board = board
		
	def move (self, piece: Piece, position):
		""" Function doc """
		piece.move(position)
		chessmate_check()
		#------------------------------------
	board = ChessBoard()
	user_white = User('white', board)
	user_black = User('black', board)
	pieces = user_white.pieces()
	horse = helper.getHorse(user_white, 1)
	user.move(horse)
	
"""
The LSP (Liskov Sustitution) is fundamental for a good software design
OOP because enphatize one of its main features: the polimorphism. it is 
about to create correct hierarchies for that derivated classes of a base
has been polimorphics about of the main class, with respect to the methods
in your interface.

Also is interesting noticing how this principle is related to the previous:
If we try to extend from a class with a another new class that is its 
incompatible, its will fail, the smart contract with costumer will be broken 
and its like result, witch extension, its will be not posible.

to Tink carefully in the news classes of the form that suggest LSP, we be 
help to extend the hierarchy correctly. Then we should say that LSP help to OCP



https://ichi.pro/es/principios-solid-explicados-en-python-con-ejemplos-56291217871103
"""
