import click
import requests
import ast

@click.group()
def cli():
    pass
    
    

def coin_Doesnt_Exist():
	return "Coin Doesnt Exist"

@cli.command()
@click.option('--currency',help = 'currency of coin')
@click.argument('coin') 
def cp(coin,currency):
	"""gets coin price """
	try:
		click.echo(cp_Request_To_Url(coin,currency))
	except Exception as err:
		print("Coin or Currency Doesnt Exist")
	



def cp_Request_To_Url(coin,price):
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_To_Url = requests.get(url)
	return formatting_Unicode_Currency(request_To_Url.text,price)

	
	
	
def formatting_Unicode_Currency(request,price):
	unicode_Format = ast.literal_eval(request)
	euro = u'\u20ac'
	if(price == 'USD'):
		return '$'+str(unicode_Format[price])
	if(price =='EUR'):
		return euro+str(unicode_Format[price])


@cli.command()
@click.argument('coin')
def mined(coin):
	try:
		click.echo(mined_Request_To_Url(coin))
	except Exception as err:
		print(coin_Doesnt_Exist())


def mined_Request_To_Url(coin):
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
	request_To_Url = requests.get(url)
	return formatting_Unicode_Mined(request_To_Url.text)
	

def formatting_Unicode_Mined(request):
	formatting_Mined_Information = ast.literal_eval(request)
	return formatting_Mined_Information['Data']['TotalCoinsMined']




@cli.command()
@click.argument('coin')
def algo(coin):
	""" gets the coin implementation algorithm"""
	try:
		click.echo(algo_request_To_Url(coin))
	except Exception as err:
		print(coin_Doesnt_Exist())
	


def algo_request_To_Url(coin):
		url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
		request_To_Url =  requests.get(url)
		return formatting_Unicode_CoinSnapShot(request_To_Url.text)
		



def formatting_Unicode_CoinSnapShot(request):
	formatting_Of_CoinSnap_Shot = ast.literal_eval(request)
	return formatting_Of_CoinSnap_Shot['Data']['Algorithm']
