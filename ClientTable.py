from Client import Client
from Errors import DoubleJeopardyError, DNEError

class ClientTable:
	def __init__(self, clients = []):
		self.__clients = []
		for client in clients:
			self.__clients.append(client)

	def add_client(self, user, password, other = {}):
		if self.has_client(user):
			raise DoubleJeopardyError()
		self.__clients.append(Client(user, password, other))

	def rm_client(self, user, password):
		for client in self.__clients:
			if client.verify(user, password):
				self.__clients.remove(client)
				return None
		raise DNEError()

	def get_client(self, user, password):
		for client in self.__clients:
			if client.verify(user, password):
				return client
		raise DNEError()

	def has_client(self, client_name):
		for client in self.__clients:
			if client.user == client_name:
				return True
		return False

	def add_acc(self, user, password, acc_name):
		client = self.get_client(user, password)
		client.addAcc(acc_name)
