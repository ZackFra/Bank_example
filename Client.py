from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount
from Account import Account, AccType
from Errors import NonAccError, AccDoubleJeopardyError

class Client:

	# user : string
	# password : string
	# other : hash of accounts
	def __init__(self, user, password, other = {}):
		self.__savings = SavingsAccount()
		self.__checking = CheckingAccount()
		self.__other = other
		self.user = user
		self.__pass = password
	
	def inquire(self, acc_name):
		if acc_name == "savings":
			return self.__savings.inquire()
		elif acc_name == "checking":
			return self.__checking.inquire()
		elif acc_name in self.__other:
			return self.__other[acc_name].inquire()
		else:
			raise NonAccError()



	def withdraw(self, acc_name, amt):
		if acc_name == "savings":
			self.__savings.withdraw(amt)
		elif acc_name == "checking":
			self.__checking.withdraw(amt)
		elif acc_name in self.__other:
			self.__other[acc_name].withdraw(amt)
		else: 
			raise NonAccError()

	def deposit(self, acc_name, amt):
		print(acc_name)
		print(acc_name == "savings")
		if acc_name == "savings":
			self.__savings.deposit(amt)
		elif acc_name == "checking":
			self.__checking.deposit(amt)
		elif acc_name in self.__other:
			self.__other[acc_name].deposit(amt)
		else: 
			raise NonAccError()

	def transfer(self, fromAcc, toAcc, amt):
		if self.hasAcc(fromAcc) and self.hasAcc(toAcc):
			self.getAcc(fromAcc).transfer(self.getAcc(toAcc), amt)
			print("Done.")
		else: raise NonAccError()


	def changeUsername(self, newName):
		self.__user = newName

	def changePassword(self, newPass):
		self.__pass = newPass

	def isClient(self, user, password):
		return user == self.__user and password == self.__pass

	def hasAcc(self, acc_name):
		return acc_name == "savings" or acc_name == "checking" or acc_name in self.__other

	def otherAccounts(self):
		names = []
		for name in self.__other:
			names.append(name)
		return names

	def getAcc(self, acc_name):
		if self.hasAcc(acc_name):
			if acc_name == "savings":
				return self.__savings
			if acc_name == "checking":
				return self.__checking
			else:
				return self.__other[acc_name]
		raise NonAccError()

	def verify(self, user, password):
		return self.user == user and self.__pass == password

	def addAcc(self, acc_name, balance = 0.0):
		if not self.hasAcc(acc_name):
			print(self.__other)
			self.__other[acc_name] = (Account(AccType.OTHER, acc_name, balance))
		else:
			raise AccDoubleJeopardyError()