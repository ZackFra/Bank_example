class NoFundsError(Exception):
	def __init__(self):
		self.expression = "NoFunds"
		self.message = "Insufficient funds for this transaction"

class NoFundsSysError(Exception):
	def __init__(self):
		self.expression = "NoFundsSys"
		self.message = "Insufficient funds for this transaction"

class NonAccError(Exception):
	def __init__(self):
		self.expression = "NonAccError"
		self.message = "This account does not exist"

class DoubleJeopardyError(Exception):
	def __init__(self):
		self.expression = "Double Jeopardy"
		self.message = "Attempting to add client to system twice"

class AccDoubleJeopardyError(Exception):
	def __init__(self):
		self.expression = "Account Double Jeopardy"
		self.message = "Attempting to add duplicate account"

class DNEError(Exception):
	def __init__(self):
		self.expression = "DNE"
		self.message = "Client does not exist"