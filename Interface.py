from ClientTable import ClientTable
from System import System

# Essentially an abstract class
class Interface:
	def __init__(self, clientTable = ClientTable(), system = System(0.00)):
		pass

	# Standard operations that must be performed

	def inquire(self, client):
		pass

	def withdraw(self, client):
		pass

	def deposit(self, client):
		pass

	def transfer(self, client):
		pass

	def list(self, client):
		pass

	def addAcc(self, client):
		pass

	def run(self):
		pass