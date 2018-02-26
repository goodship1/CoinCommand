import pytest
import CoinCommandTest

coin = 'BTC'
currency = 'USD'


def test_Algo_Return_Correct_Value():
    assert CoinCommandTest.algo(coin) == "SHA256" 


def test_Cp_Correct_Currency_Return():
    cp_return = CoinCommand.cp(coin,currency)

def test_Mined():
    pass

def test_Social():
    pass

def test_change():
	pass
