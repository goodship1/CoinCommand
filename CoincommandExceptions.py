
class CoinCommandExceptions(Exception):
	pass
	

class CoinDoesntExist(CoinCommandExceptions):
	pass
	

class ConnectionError(CoinCommandExceptions):
	pass

