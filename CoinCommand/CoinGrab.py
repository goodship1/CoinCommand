import requests
import json 

class CoinGrabInformation(object):
	
	"""class which gets coin information such as volume , price
	algorithm information difficulty rate etc"""
	
	def __init__(self,coin,currency="GDP"):
		self.coin = coin
		self.volume = None
		self.change = None
		self.currency = currency
	
	def get_Coin_Information(self):
		pass
		
	
