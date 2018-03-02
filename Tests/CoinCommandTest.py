import requests
import ast


"""some modifactions to coinCommand to allow an easier way to test cli"""

def cp(coin,currency):
	"""gets coin price """
	return cp_Request_To_Url(coin,currency)
	
	
def change(coin):
	pass


def cp_Request_To_Url(coin,price):
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_To_Url = requests.get(url)
	return formattingUnicodeCurrency(request_To_Url.text,price)

	
	
	
def formatting_Unicode_Currency(request,price):
	unicode_Format = ast.literal_eval(request)
	euro = u'\u20ac'
	if(price == 'USD'):
		return '$'+str(unicode_Format[price])
	if(price =='EUR'):
		return euro+str(unicode_Format[price])



def mined(coin):
	return mined_Request_To_Url(coin)
	



def mined_Request_To_Url(coin):
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
	request_To_Url = requests.get(url)
	return formatting_Unicode_Mined(request_To_Url.text)
	

def formatting_Unicode_Mined(request):
	formatting_Mined_Information = ast.literal_eval(request)
	return formatting_Mined_Information['Data']['TotalCoinsMined']
	
def social(coin,news_Outlet):
	pass




def algo(coin):
	""" gets the coin implementation algorithm"""
	algo_request_To_Url(coin)
	return algo_request_To_Url(coin)
	


def algo_Request_To_Url(coin):
		url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
		request_To_Url =  requests.get(url)
		return formatting_Unicode_CoinSnapShot(request_To_Url.text)
		



def formatting_Unicode_CoinSnapShot(request):
	formatting_Of_coinSnap_Shot = ast.literal_eval(request)
	return formatting_Of_CoinSnap_Shot['Data']['Algorithm']
