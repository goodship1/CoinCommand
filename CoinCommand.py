import click
import requests
import ast
@click.group()
def cli():
    pass

@cli.command()
@click.option('--price'  help = 'gets price of coin')
@click.argument('coin') 
def cp(coin,price):
	"""gets coin price """
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_To_Url = requests.get(url)
	click.echo(formattingUnicodeCurrency(request_To_Url.text,price))
	


def getting_currency_rates():
	"""adding great british pounds to cp funcution"""
	pass

@cli.command()
@click.option('--total',help = 'total coins mined')
@click.option('--diff',help = 'gets the mining diffiuclty')
def mining(coin):
	pass

@cli.command()
def addr(address):
	pass

def formattingUnicodeCurrency(request,price):
	unicode_format = ast.literal_eval(request)
	eur = u'\u20ac'
	if(price == 'USD'):
		return '$'+str(unicode_format[price])
	if(price =='EUR'):
		return eur+str(unicode_format[price])

@cli.command()
@click.argument('coin')
def algo(coin):
	""" gets the coin implementation algorithm"""
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
	request_To_Url = requests.get(url)
	click.echo(formattingUnicodeAlgorithm(request_To_Url.text))
	

def formattingUnicodeAlgorithm(request):
	formatting_of_coinSnap_Shot = ast.literal_eval(request)
	return formatting_of_coinSnap_Shot['Data']['Algorithm']
