import click
import requests

@click.group()
def cli():
    pass

@cli.command()
@click.option('--price' , help = 'gets price of coin')
@click.argument('coin') 
def cp(coin,price):
	"""gets coin price in usd as default"""
	formatting_List = []
	if(price != 'USD') or(price != 'EUR'):
		#get exhange rate
		pass
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
	request_To_Url = requests.get(url)
	request_To_Url_Format = request_To_Url.text
	request_To_Url_Format = request_To_Url_Format.split(price)

def formattingRequest():
	pass
	
	
