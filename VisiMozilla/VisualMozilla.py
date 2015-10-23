import requests
import json

url= 'https://input.mozilla.org/api/v1/feedback?happy=0&date_delta=1d'

my_list=[["product","count"]];

def postrequestsFirefox(data):

	responseFF = requests.get(url, params=data)
	dataFF = json.loads(responseFF.content)
	product1 = ['Firefox']
	product1.append(dataFF['count'])
	print product1
	my_list.append(product1)
	# for item in dataFF['results']:
	# 	print item['product']

def postrequestsFirefoxForAndroid(data):

	responseFFA = requests.get(url,params=data)
	dataFFA = json.loads(responseFFA.content)
	product2 = ['Firefox For Android']
	product2.append(dataFFA['count'])
	print product2
	my_list.append(product2)
	# for item in dataFFA['results']:
	# 	print item['product']


def postrequestsFirefoxOS(data):

	responseFOS = requests.get(url,params=data)
	dataFOS  = json.loads(responseFOS.content)
	product3 = ['Firefox OS']
	product3.append(dataFOS['count'])
	print product3
	my_list.append(product3)
	# for item in dataFOS['results']:
	# 	print item['product']


def postrequestsFirefoxForiOS(data):

	responseIOS = requests.get(url,params=data)
	dataIOS = json.loads(responseIOS.content)
	product4 = ['iOS']
	if dataIOS['count']>0:
		product4.append(dataIOS['count'])
		print product4
		my_list.append(product4)
	# for item in dataIOS['results']:
	# 	print item['product']
