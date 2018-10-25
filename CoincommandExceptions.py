import exceptions

class CoinCommandExceptions(exception):

    def connectionError(self):
        return "error no connection"

