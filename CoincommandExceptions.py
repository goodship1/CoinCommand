import exceptions

class CoinCommandExceptions(exception):

    def connectionError(self):
        return "error no connection"
    
    def coinOrcurrencyDoesntexist(self):
		return "coin or corrency doesnt exist"
		

