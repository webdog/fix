#!/usr/bin/python
import json
from sys import argv
import requests

#When running script from command line, pass an arg that is the symbol from which you want the price
#Script will query this data from yahoo, return in json format, and then parse accordingly
#Note: Script is executable, so you can create an alias in .bashrc for more efficiency:
#e.g. alias price=~/yahoo.py 
#>price AAPL

symbol = argv[1]

def get_quote(symbol):
	req_url = "http://finance.yahoo.com/webservice/v1/symbols/%s/quote?format=json" % symbol
	#print req_url
	req = requests.get(req_url)
	rc  = int(req.status_code)
	if rc == 200:
		info = json.loads(req.text)
		path =  info['list']['resources'][0]['resource']['fields']
		price = path['price']
		symbol = path['symbol']
		volume = path['volume']
		prodtype = path['type']
		print "symbol | price | volume"
		print symbol+" | "+price+" | "+volume

	else:
		print rc

get_quote(symbol)
