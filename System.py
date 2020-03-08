from Errors import NoFundsSysError


# System is the real world system that our bank system is attached to
# This may be an ATM, or a whole bank, or something else.
# It keeps track of how much money that the underlying system has to dispense
class System:
	def __init__(self, total):
		self.__total = total

	def withdraw(self, amt):
		if self.__total - amt < 0:
			raise NoFundsSysError 
		self.__total = self.__total - amt

	def deposit(self, amt):
		self.__total = self.__total + amt