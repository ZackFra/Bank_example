from Account import Account, AccType

class SavingsAccount(Account):
	def __init__(self, balance = 0.00):
		super().__init__(AccType.SAVINGS, "savings", balance)