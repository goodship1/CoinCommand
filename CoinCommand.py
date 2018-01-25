import click
import requests
import ast
@click.group()
def cli():
    pass

@cli.command()
@click.option('--price' , help = 'gets price of coin')
@click.argument('coin') 
def cp(coin,price):
	"""gets coin price in usd as default"""
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_To_Url = requests.get(url)
	click.echo(formattingUnicodeCurrency(request_To_Url.text,price))
	


def formattingUnicodeCurrency(request,price):
	unicode_format = ast.literal_eval(request)
	eur = u'\u20ac'
	if(price == 'USD'):
		return '$'+str(unicode_format[price])
	if(price =='EUR'):
		return eur+str(unicode_format[price])



