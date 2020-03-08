
from Interface import Interface
from ClientTable import ClientTable
from Errors import DNEError, NoFundsError, NonAccError, NoFundsSysError, AccDoubleJeopardyError
from System import System

class TESTInterface(Interface):
	def __init__(self, clientTable = ClientTable(), system = System(0.00)):
		self.__clientTable = clientTable
		self.__system = system

	# raises DNEError if account doesn't exist
	def inquire(self, client):
		which = input("For which account?:")
		balance = client.inquire(which)
		print("Balance = ${}".format(balance))

	# raises
	# NoFundsSysError if system has insufficient funds
	# ValueError if amt can't be parsed
	# NonAccError if acc doesn't exist in client
	def withdraw(self, client):
		amt = input("How much?:")
		amt = float(amt)
		amt = round(amt, 2)

		which = input("For which account?:")
		self.__system.withdraw(amt)
		client.withdraw(which, amt)

	# raises
	# ValueError if input is off
	# DNEError if account does not exist
	def deposit(self, client):
		amt = input("How much?")
		amt = float(amt)

		which = input("For which account?:")
		client.deposit(which, amt)
		self.__system.deposit(amt)

	# raises
	# Value Error if can't parse value
	# NoFundError if there are no funds in fromAcc
	# NonAccError if one of the accounts doesn't exist
	def transfer(self, client):

		amt = input("How much?")
		amt = float(amt)

		fromAcc = input("From which account?:")
		toAcc = input("To which account?")
		client.transfer(fromAcc, toAcc, amt)


	def list(self, client):
		print("savings")
		print("checking")
		otherAccs = client.otherAccounts()
		for name in otherAccs:
			print(name)

	# Raises
	# AccDoubleJeopardyError if acc_name already exists
	def addAcc(self, client):
		acc_name = input("Under what name?:").strip()
		client.addAcc(acc_name)


	def run(self):

		while True:
			user = input("User Name >>")
			password = input("Password >>")

			try:
				client = self.__clientTable.get_client(user, password)
				print("Hello {}!".format(client.user))
				break
			except DNEError:
				print("Invalid Username or Password")


		while True:
			print("------------")
			print("Options: ")
			print("1) Inquire")
			print("2) Withdraw")
			print("3) Deposit")
			print("4) Transfer") 
			print("5) List Accounts")
			print("6) Add Account")
			print("q) Quit")
			print("------------")
			selection = input(">>").strip()

			# Inquire
			if selection == "1":
				try: self.inquire(client)
				except DNEError:
					print("Invalid Selection")
				except NonAccError:
					print("Invalid Selection")


			# Withdraw
			elif selection == "2":
				try: self.withdraw(client)
				except NoFundsSysError:
					print("Insufficient Funds in System")
				except NoFundsError:
					print("Insufficient Funds in Account")
				except NonAccError:
					print("Nonexistent Account")

			# Deposit
			elif selection == "3":
				try: self.deposit(client)
				except ValueError:
					print("Invalid Input. Resetting.")
				except NonAccError:
					print("Nonexistent Account")


			# Transfer
			elif selection == "4":
				try: self.transfer(client)
				except ValueError:
					print("Invalid Input. Resetting")
				except NoFundsError:
					print("Insufficient Funds. Resetting.")
				except NonAccError:
					print("Invalid Account Name. Resetting.")

			# List Accounts
			elif selection == "5":
				self.list(client)

			# Add Account
			elif selection =="6":
				try: self.addAcc(client)
				except AccDoubleJeopardyError:
					print("Account already exists")


			elif selection == "q":
				break

			else:
				print("Invalid Selection. Resetting.")

# Test run
if __name__ == '__main__':
	sys = System(1000)
	ct = ClientTable()
	ct.add_client("JimmyJenk", "BillyBob")
	ct.add_client("Zack", "Yikes")
	ct.add_client("Jay", "Swag")
	interface = TESTInterface(ct, sys)
	interface.run()