from Account import Account, AccType

class CheckingAccount (Account):
	def __init__(self, balance = 0.0):
		super().__init__(AccType.CHECKING, "checking", balance)