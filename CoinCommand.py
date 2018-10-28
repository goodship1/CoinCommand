import click
import requests
import ast

@click.group()
def cli():
    pass





@cli.command()
@click.option('--currency',help = 'currency of coin')
@click.argument('coin')
def cp(coin,currency):
	"""gets coin price """
	click.echo(cp_Request_to_Url(coin,currency))




def cp_Request_to_Url(coin,price):

    """Makes request to  https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"""
    url="https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
    request_To_url = requests.get(url)
    return formatting_Unicode_currency(request_To_url.text,price)




def formatting_Unicode_currency(request,price):

    """formatting unicode currency formats the json data to get price"""
    unicode_Format = ast.literal_eval(request)
    euro = u'\u20ac'
    if(price == 'USD'):
		return '$'+str(unicode_Format[price])
    if(price =='EUR'):
		return euro+str(unicode_Format[price])
    #Todo add support to for £

def price_Helper():
	pass


@cli.command()
@click.argument('coin')
def mined(coin):
    """Mined gets the total coins mined"""
    click.echo(mined_Request_to_Url(coin))

def mined_Request_to_Url(coin):
    """Makes request to https://www.cryptocompare.com/api/data/coinsnapshot/?"""
    url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
    request_To_url = requests.get(url)
    return formatting_Unicode_mined(request_To_url.text)


def formatting_Unicode_mined(request):
    """formats the json request  data from coinsnapshot"""
    formatting_Mined_information = ast.literal_eval(request)
    return formatting_Mined_information['Data']['TotalCoinsMined']




@cli.command()
@click.argument('coin')
def algo(coin):
	""" gets the coin implementation algorithm"""
	click.echo(algo_Request_to_Url(coin))




def algo_Request_to_Url(coin):
    """Makes request to https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD"""
    url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
    request_To_Url =  requests.get(url)
    return formatting_Unicode_coinsnapshot(request_To_Url.text)




def formatting_Unicode_coinsnapshot(request):
    """formats request to data from coinsnapshot buts get algorithm data"""
    formatting_Of_coinsnapshot = ast.literal_eval(request)
    return formatting_Of_coinsnapshot['Data']['Algorithm']





@click.command()
@click.argument('language')
def news(language):
	click.echo(request_To_url(language))
	

def request_To_news(request,news):
	url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=%s'%news
	request_To_url = requests.get(url)
	return formatting_News_unicode(request_To_url.text)
	
	

def formatting_News_unicode(request):
	formatting_News_information = ast.literal_eval(request)
	return formatting_News_information



