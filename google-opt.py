#!/usr/bin/python
import demjson
from sys import argv
import requests

#Retrieves bid/ask price for contract/expiration/call or put

class getQuote:
	def __init__(self, symbol):
		self.symbol = symbol
	def requestQuote(self):
		req_url = "http://www.google.com/finance/option_chain?q=%s&output=json" % self.symbol
		req = requests.get(req_url)
		rc  = int(req.status_code)
		call_put = raw_input("Please select 'C' for Call, or 'P' for Put\n>")
		strike = raw_input("Please enter the strike: E.g. 55.00\n>")
		expiration = raw_input("Please enter the expiration: E.g. Jul 11, 2014\n>")
		if rc == 200:
			info = demjson.decode(req.text)
			calls =  info['calls']
			puts = info['puts']
			if call_put == "C":
				for contracts in calls:
					for items in contracts:
						if contracts['expiry'] == expiration and contracts['strike'] == strike:
							return "Ask Price: "+contracts['a']+"\n"+"Bid Price: "+contracts['b']
			elif call_put == "P":
				for contracts in calls:
					for items in contracts:
						if contracts['expiry'] == expiration  and contracts['strike'] == strike:
							return "Ask Price: "+contracts['a']+"\n"+"Bid Price: "+contracts['b']
			else:
				print "Invalid selection."
				exit()

		else:
			print rc

if __name__ == "__main__":
	get = getQuote(argv[1])
	quote = get.requestQuote()
	print quote
