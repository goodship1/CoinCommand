import pytest
import CoinCommandTest
import requests 

incorrect = "aadaed"
btc = 'BTC'
xvg = 'XVG'
dollar = 'USD'
euro_Sign = u'\u20ac'
euro = 'EUR'
dollar_Sign = '$'


def test_Algo_return_Correct_value():
    assert CoinCommandTest.algo(btc) == "SHA256" 


def test_Cp_dollar_Return():
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(btc,dollar)
	request = requests.get(url)
	cp_Return = str(CoinCommandTest.formatting_Unicode_Currency(request.text,dollar))
	assert cp_Return[0] == dollar_Sign
	
	
	
def test_Cp_Euro_Return():
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(btc,"EUR")
	request = requests.get(url)
	cp_Return = str(CoinCommandTest.formatting_Unicode_Currency(request.text,"EUR"))
	assert cp_Return[0]!=dollar_Sign
	

def test_of_Coin_NotPresent():
	call_To_Cp = CoinCommandTest.cp(incorrect,dollar)
	assert(call_To_Cp) == "coin or currency doesnt exist"
	
	

def test_mined_Return_float():
	"""test to make sure mined returns the correct data type"""
	assert type(CoinCommandTest.mined(btc)) == float
	

def test_Formatting_unicode_Currency():
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(btc,dollar)
	request_To_Url = requests.get(url)
	return_Currency = CoinCommandTest.formatting_Unicode_Currency(request_To_Url.text,"USD")
	assert(type(return_Currency)) == str


def test_Formatting_unicode_Mined():
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%btc
	request_To_Url = requests.get(url)
	



def test_Algo_Incorrect_Coin():
	algo_return  =  CoinCommandTest.algo(incorrect)
	error = CoinCommandTest.coin_Doesnt_Exist()
	assert(algo_return) == 	error
	
	
def test_mined_Incorrect_coin():
	mined_Return = CoinCommandTest.mined(incorrect)
	error = CoinCommandTest.coin_Doesnt_Exist()
	assert(mined_Return) == error
	
	
def test_Formatting_unicode_Coinsnapshot():
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%btc
	request_To_Url = requests.get(url)
	return_CoinSnapShot = CoinCommandTest.formatting_Unicode_CoinSnapShot(request_To_Url.text)
	assert(type(return_CoinSnapShot)) == str

def test_news():
	url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
	return_News = CoinCommandTest.news()
	assert(return_News)==CoinCommand.formatting_Unicode_news(url)

def test_Unicode_formatting():
	url = 'https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
	request_To_url = request.get(url)
	return_Unicode_formatting_News
	return_Unicode_news = CoinCommandTest.formatting_Unicode_news(request_to_url)
	assert(type(return_Unicode_news)) == str
