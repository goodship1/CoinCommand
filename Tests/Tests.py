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
    assert CoinCommandTest.algo(coin) == "SHA256" 


def test_Cp_Dollar_Return_Format():
	"""Test to show the correct Currency Format of $ """
	cp_return = str(CoinCommandTest.cp(coin,dollar))
	assert cp_return[0] == dollar_Sign
 

def test_Cp_Euro_Return_Format():
	cp_return = CoinCommandTest.cp(coin,euro)
	assert cp_return[0]!=dollar_Sign


def test_Mined_Return_Float():
	"""test to make sure mined returns the correct data type"""
	assert type(CoinCommandTest.mined(btc)) == float
	

def test_FormattingUnicodeCurrency():
	pass


def test_ FormattingUnicodeMined():
	pass
	


