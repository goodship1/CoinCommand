import click
import requests
import ast
from beautifultable import BeautifulTable




@click.group()
def cli():
    pass



@cli.command()
@click.option('--currency',default = 'USD',help = 'currency of coin')
@click.argument('coin')
def cp(coin,currency):
	"""Gets coin price """
	click.echo(cp_request_to_url(coin,currency))
	

def cp_request_to_url(coin,currency):

    """Makes request to  https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"""
    url="https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(coin,currency)
    request_To_url = requests.get(url)
    return formatting_Unicode_currency(request_To_url.text,currency)




def formatting_Unicode_currency(request,price):

    """formatting unicode currency formats the json data to get price"""
    unicode_Format = ast.literal_eval(request)
    euro = u'\u20ac'
    if(price == 'USD'):
		return '$'+str(unicode_Format[price])
    if(price =='EUR'):
		return euro+str(unicode_Format[price])
    



@cli.command()
@click.argument('coin')
def mined(coin):
    """Mined gets the total coins mined"""
    click.echo(mined_request_to_url(coin))
		
def mined_request_to_url(coin):
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
	click.echo(algo_request_to_url(coin))
	



def algo_request_to_url(coin):
    """Makes request to https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD"""
    url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%coin
    request_To_Url =  requests.get(url)
    return formatting_Unicode_coinsnapshot(request_To_Url.text)




def formatting_Unicode_coinsnapshot(request):
    """formats request to data from coinsnapshot  gets algorithm data"""
    formatting_Of_coinsnapshot = ast.literal_eval(request)
    return formatting_Of_coinsnapshot['Data']['Algorithm']


@cli.command()
@click.argument('coin')
@click.option('--currency',default = 'USD',help = 'Gives the user snap of coin information')
def snapshot(coin,currency):
    """returns a snap shot of coin information"""
    coin_Snapshot_table = BeautifulTable()#creates a table
    coin_Snapshot_table.columns = ['Name','Price','Mined','Algorithm']
    coin_Price = cp_request_to_url(coin,currency)
    coin_Mined = mined_request_to_url(coin)
    coin_Algorithm = algo_request_to_url(coin)
    snap_shot_data = [coin,coin_Price,coin_Mined,coin_Algorithm]
    click.echo(snap_shot_data)


    


@cli.command()
@click.argument('language')
def news(language):
	"""gets current news articles about coins"""
	click.echo(request_To_news(language))
	


def request_To_news(language):
	url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=%s'%language
	request_To_url = requests.get(url)
	return formatting_News_unicode(request_To_url.text)
	
	

def formatting_News_unicode(request):
	formatting_News_information = ast.literal_eval(request)
	return formatting_News_information


