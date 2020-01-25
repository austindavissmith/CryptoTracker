import requests
from requests import Session
import json
import datetime
import dateutil.parser

class functions: 

	price_list = ["HTTPS://api.coinbase.com/v2/prices/BTC-USD/spot", "HTTPS://api.coinbase.com/v2/prices/ETH-USD/spot", 
			"HTTPS://api.coinbase.com/v2/prices/LTC-USD/spot", "HTTPS://api.coinbase.com/v2/prices/XLM-USD/spot"]
	

	def print_data(data): #Takes in the pricing data returned from api and prints to console
		currency = data["data"]["base"] #Parses all the data into certain variables
		price = data["data"]["amount"]
		type = data['data']['currency']
		print(f"Currency : {currency}  Price: {type} {price}") #the 'f' makes this a format string so we can use curly braces{} to input variables to the string

	def get_time(self): #Gets the current time from the API
		try:
			t = requests.get("https://api.coinbase.com/v2/time").json()
			curr_time = t['data']['iso']
			curr_time1 = dateutil.parser.parse(curr_time)
			return curr_time1
		except requests.exceptions.ConnectionError:
			return "Connection Refused"

	def get_local_time(self): #Gets local time from user machine
		current_t = datetime.datetime.now()
		t = current_t.strftime("%A, %B %d, %Y %I:%M:%S %p \n(Prices Updated Every 10 Seconds)")
		return t
		
	def get_price(self, price_list, i): #returns Price of desired crypto
		try:
			crypto = requests.get(price_list[i]).json()
			price = crypto["data"]["amount"]
			return price
		except requests.exceptions.ConnectionError:
			return "Connection Refused"
	
	def get_conversion(self, entryText, combo_box1, combo_box2, entry): # Converts cyrpto to desired currency    
		try:
			web_addr = f"https://api.coinbase.com/v2/prices/{combo_box1}-{combo_box2}/spot"
			crypto = requests.get(web_addr).json()
			conv = crypto['data']['amount']
			new_amount = float(entryText) * float(conv)
			string_box = round(new_amount, 2) # Append result to two decimal places
			entry.set(string_box)
		except ValueError:
			entry.set("Enter number of Crypto")
	
	def get_last24hr_price(self, crypto):
		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
		parameters = {'symbol': crypto}
		headers = {'Accepts': 'application/json',
  			'X-CMC_PRO_API_KEY': '144a6774-f7a2-4b3b-b26f-a922368c869c'}
		session = Session()
		session.headers.update(headers)

		try:
			response = session.get(url, params=parameters)
			data = json.loads(response.text)
			p_24_hr = data['data'][crypto]['quote']['USD']['percent_change_24h']
			appended_p_24_hr = round(p_24_hr, 2)
			return appended_p_24_hr
		except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
	

