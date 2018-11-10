import requests
import ast


"""some modifactions to coinCommand to allow an easier way to test cli"""



def cp(coin,currency):
	"""gets coin price """
	try:
		return cp_Request_to_Url(coin,currency)
	except Exception as err:
		return "coin or currency doesnt exist"




def cp_Request_to_Url(coin,price):
	url="https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_to_Url = requests.get(url)
	return formatting_Unicode_currency(request_To_url.text,price)




def formatting_Unicode_Currency(request,price):
	unicode_Format = ast.literal_eval(request)
	euro = u'\u20ac'
	if(price == 'USD'):
		return '$'+str(unicode_Format[price])
	if(price =='EUR'):
		return euro+str(unicode_Format[price])



def mined(coin):
	try:
		return mined_Request_To_Url(coin)
	except Exception as err:
		return coin_Doesnt_Exist()



def mined_Request_To_Url(coin):
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
	request_To_Url = requests.get(url)
	return formatting_Unicode_Mined(request_To_Url.text)


def formatting_Unicode_Mined(request):
	formatting_Mined_Information = ast.literal_eval(request)
	return formatting_Mined_Information['Data']['TotalCoinsMined']





def algo(coin):
	""" gets the coin implementation algorithm"""
	try:
		return algo_Request_To_Url(coin)
	except Exception as err:
		return(coin_Doesnt_Exist())


def algo_Request_To_Url(coin):
		url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
		request_To_Url =  requests.get(url)
		return formatting_Unicode_CoinSnapShot(request_To_Url.text)

def formatting_Unicode_CoinSnapShot(request):
	formatting_Of_CoinSnapShot = ast.literal_eval(request)
	return formatting_Of_CoinSnapShot['Data']['Algorithm']

def get_News():
	return request_To_news

def request_to_News():
	url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
	request_To_url = requests.get(url)
	return  formatting_Unicode_news(request_To_url.text)
	

def formatting_Unicode_news(request):
	formatting_News_unicode = ast.literal_eval(request)
	return formatting_News_unicode


