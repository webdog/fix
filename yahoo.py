#!/usr/bin/python
import json
from sys import argv
import requests

class getQuote:
	def __init__(self, symbol):
		self.symbol = symbol
	def requestQuote(self):
		req_url = "http://finance.yahoo.com/webservice/v1/symbols/%s/quote?format=json" % self.symbol
		req = requests.get(req_url)
		rc  = int(req.status_code)
		if rc == 200:
			info = json.loads(req.text)
			path =  info['list']['resources'][0]['resource']['fields']
			price = path['price']
			symbol = path['symbol']
			volume = path['volume']
			return "symbol | price     | volume\n"+symbol+"   | "+price+" | "+volume

		else:
			print rc

if __name__ == "__main__":
	get = getQuote(argv[1])
	quote = get.requestQuote()
	print quote
