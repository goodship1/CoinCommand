import click
import requests
import ast
@click.group()
def cli():
    pass

@cli.command()
@click.option('--price'  help = 'Gets price of coin')
@click.argument('coin') 
def cp(coin,price):
	"""gets coin price """
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_To_Url = requests.get(url)
	click.echo(formattingUnicodeCurrency(request_To_Url.text,price))


@cli.command()
@click.option('--total'	,help = "Gets total number of transactions of coin in a 24 hour window")
def transactions(coin):
	pass


def transaction_UniCode_Formatting(coin):
	pass

def getting_currency_rates():
	"""adding great british pounds to cp funcution"""
	pass

@cli.command()
@click.option('--total',help = 'Total coins mined')
@click.option('--diff',help = 'Gets the mining diffiuclty')
def mined(coin):
	pass

@cli.command()
@click.option('--info' ,help  = "Gets information of address of transactions")
@click.arguement('coin')
@click.argument('address')
def addr(coin,address):
	"""only works for BTC and ETH"""
	pass


def address_Query(addr):
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
