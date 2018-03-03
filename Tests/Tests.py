import pytest
import CoinCommandTest
import requests 


btc = 'BTC'
xvg = 'XVG'
dollar = 'USD'
euro_Sign = u'\u20ac'
euro = 'EUR'
dollar_Sign = '$'

def test_Algo_Return_Correct_Value():
    assert CoinCommandTest.algo(btc) == "SHA256" 


def test_Cp_Dollar_Return_Format():
	"""Test to show the correct Currency Format of $ """
	cp_return = str(CoinCommandTest.cp(btc,dollar))
	assert cp_return[0] == dollar_Sign
 

def test_Cp_Euro_Return_Format():
	cp_return = CoinCommandTest.cp(btc,euro)
	assert cp_return[0]!=dollar_Sign


def test_of_Coin_NotPresent():
	pass
	

def test_Mined_Return_Float():
	"""test to make sure mined returns the correct data type"""
	assert type(CoinCommandTest.mined(btc)) == float
	

def test_FormattingUnicodeCurrency():
	url = "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s"%(btc,dollar)
	request_To_Url = requests.get(url)
	return_Currency = CoinCommandTest.formatting_Unicode_Currency(request_To_Url.text,"USD")
	assert(type(return_Currency)) == str


def test_FormattingUnicodeMined():
	url = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=%s&tsym=USD'%btc
	request_To_Url = requests.get(url)
	
	
	
	
def test_Formatting_Unicode_CoinSnapShot():
	pass

