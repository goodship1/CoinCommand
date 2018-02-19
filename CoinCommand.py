import click
import requests
import ast
import tabulate
@click.group()
def cli():
    pass

@cli.command()
@click.option('--currency' ,help = 'Gets price of coin')
@click.argument('coin') 
def cp(coin,price):
	"""gets coin price """
	click.echo(cp_Request_To_Url(coin,price))
	
	


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


@cli.command()
@click.argument('coin')
def mined(coin):
	click.echo(mined_Request_To_Url(coin))
	

def left(coin):
	pass

def left_Request_To_Url(coin):
	pass


def mined_Request_To_Url(coin):
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
	request_To_Url = requests.get(url)
	return formattingUnicodeMined(request_To_Url.text)
	

def formattingUnicodeMined(request):
	formattingMinedInformation = ast.literal_eval(request)
	return formattingMinedInformation['Data']['TotalCoinsMined']
	

@cli.command()
@click.argument('address')
def addrBtc(address):
	address_Query(address)
	
	


def address_Query(addr):
	url = 'https://blockchain.info/rawaddr/%s'%addr
	request_To_Url = requests.get(url)
	



@cli.command()
@click.argument('coin')
def algo(coin):
	""" gets the coin implementation algorithm"""
	algo_request_To_Url(coin)
	click.echo(algo_request_To_Url(coin))
	


def algo_request_To_Url(coin):
		url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
		request_To_Url =  requests.get(url)
		return formattingUnicodeCoinSnapShot(request_To_Url.text)
		



def formattingUnicodeCoinSnapShot(request):
	formatting_of_coinSnap_Shot = ast.literal_eval(request)
	return formatting_of_coinSnap_Shot['Data']['Algorithm']
