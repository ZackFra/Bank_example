from enum import Enum
from Errors import NoFundsError

class AccType(Enum):
	CHECKING = 1
	SAVINGS = 2
	OTHER = 3

class Account:
	def __init__(self, accType, name, balance = 0.00):
		self.__balance = balance
		self.__type = accType
		self.name = name

	def inquire(self):
		return self.__balance

	def deposit(self, amt):
		self.__balance = self.__balance + amt

	def withdraw(self, amt):
		if(self.__balance - amt < 0):
			raise NoFundsError()
		self.__balance = self.__balance - amt

	# transfer from self to other
	def transfer(self, other, amt):
		self.withdraw(amt)
		other.deposit(amt)

	def getType():
		return accType

