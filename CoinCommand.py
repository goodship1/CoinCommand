import click
import requests
import ast

@click.group()
def cli():
    pass



def coin_Doesnt_exist():
	return "Coin Doesnt Exist"


def connection_Error():
    #error handling to handle http 400 status
    #todo implement error handling for 400 status
    return "no connection"

@cli.command()
@click.option('--currency',help = 'currency of coin')
@click.argument('coin')
def cp(coin,currency):
	"""gets coin price """
	try:
		click.echo(cp_Request_To_url(coin,currency))
	except Exception as err:
		print("Coin or Currency Doesnt Exist")




def cp_Request_to_Url(coin,price):

    """Makes request to  https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"""
    url="https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,price)
    request_to_Url = requests.get(url)
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


@cli.command()
@click.argument('coin')
def mined(coin):
    """Mined gets the total coins mined"""
    try:
	    click.echo(mined_Request_To_Url(coin))
    except Exception as err:
		print(coin_doesnt_Exist())


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
	try:
		click.echo(algo_request_to_Url(coin))
	except Exception as err:
		print(coin_Doesnt_exist())



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
@click.argument('socialmedia')
def get_Social():
	pass
    #todo allow the user to get social



def request_To_social():
     pass

@click.command()
@click.arguments(news)
def get_News():
	pass

def request_To_news():
	pass

def formatting_News_unicode():
	pass


def formatting_Social_unicode():
    pass
