class Account:
	""" An account has a balance and a holder

	>>> a = Account('John')
	>>> a.deposit(100)
	100
	>>> a.withdraw(90)
	10
	>>> a.withdraw(90)
	'Insufficient funds'
	>>> a.balance
	10
	"""

	#(3) deposit = 666

	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
		#(2) self.deposit = 9999

	def deposit(self, amount):
		""" Add amount to balance """
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		"""Subtract amount from balance if funds are available """
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance