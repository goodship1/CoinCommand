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

	
	
	
def formattingUnicodeCurrency(request,price):
	unicode_format = ast.literal_eval(request)
	eur = u'\u20ac'
	if(price == 'USD'):
		return '$'+str(unicode_format[price])
	if(price =='EUR'):
		return eur+str(unicode_format[price])



def mined(coin):
	click.echo(mined_Request_To_Url(coin))
	



def mined_Request_To_Url(coin):
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
	request_To_Url = requests.get(url)
	return formattingUnicodeMined(request_To_Url.text)
	

def formattingUnicodeMined(request):
	formattingMinedInformation = ast.literal_eval(request)
	return formattingMinedInformation['Data']['TotalCoinsMined']
	
def social(coin,news_Outlet):
	pass




def algo(coin):
	""" gets the coin implementation algorithm"""
	algo_request_To_Url(coin)
	return algo_request_To_Url(coin)
	


def algo_request_To_Url(coin):
		url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
		request_To_Url =  requests.get(url)
		return formattingUnicodeCoinSnapShot(request_To_Url.text)
		



def formattingUnicodeCoinSnapShot(request):
	formatting_of_coinSnap_Shot = ast.literal_eval(request)
	return formatting_of_coinSnap_Shot['Data']['Algorithm']
