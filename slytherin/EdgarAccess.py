import requests
import json

import nltk
from nltk import word_tokenize, pos_tag
import string
import re

keywords = [];
query = ["cik","companyname","entityid","primaryexchange",
"marketoperator","markettier","primarysymbol","siccode","sicdescription"
,"usdconversionrate","restated","receiveddate","preliminary","periodlengthcode","periodlength"
,"periodenddate","original","formtype","fiscalyear","fiscalquarter","dcn","currencycode",
"crosscalculated","audited","amended","changeincurrentassets","changeincurrentliabilities"
,"changeininventories","dividendspaid","effectofexchangerateoncash","capitalexpenditures"
,"cashfromfinancingactivities","cashfrominvestingactivities","cashfromoperatingactivities"
,"cfdepreciationamortization","changeinaccountsreceivable","investmentchangesnet","netchangeincash"
,"totaladjustments","ebit","costofrevenue","grossprofit","incomebeforetaxes","netincome"
,"netincomeapplicabletocommon","researchdevelopmentexpense","totalrevenue","sellinggeneraladministrativeexpenses"
,"commonstock","cashandcashequivalents","cashcashequivalentsandshortterminvestments","goodwill"
,"intangibleassets","inventoriesnet","otherassets","othercurrentassets","othercurrentliabilities"
,"otherliabilities","propertyplantequipmentnet","retainedearnings","totalassets","totalcurrentassets"
,"totalcurrentliabilities","totalliabilities","totallongtermdebt","totalreceivablesnet","totalshorttermdebt"
,"totalstockholdersequity"]

quarters = {"first" : 1, "second" : 2, "third" : 3, "fourth":4}
dict = {}


# Get all the English alphabet letters and a space
valid_letters = string.ascii_letters  + string.digits + ' '

pattern = '[1-3][0-9]{3}'

#match = re.findall(r'(\d+/\d+/\d+)',text)

#stripped_text = ''.join([char if char in valid_letters else '' for char in text])
#tokens = word_tokenize(stripped_text)
#tags = pos_tag(tokens)

#for (a,b) in tags:
#	if b == 'NN' or b == 'NNP':
#		keywords.append(a)
#	if b == 'NNP':
#		dict["companyname"] = a
#	if a == 'first' or a == 'second' or a == 'third' or a == 'fourth':
#		dict["financialquarter"] = quarters[a]

#if match:		
#	for a in match:
		
#		dict["date"] = a
	
def parsetext(text):
	stripped_text = ''.join([char if char in valid_letters else '' for char in text])
	tokens = word_tokenize(stripped_text)
	tags = pos_tag(tokens)
	match = re.findall(pattern,text)

	for (a,b) in tags:
		if b == 'NN' or b == 'NNP':
			keywords.append(a)
		if b == 'NNP':
			dict["companyname"] = a
		if a == 'first' or a == 'second' or a == 'third' or a == 'fourth':
			dict["financialquarter"] = quarters[a]
		if a =='debt':
			dict["fieldToSearch"] = a
		elif a =='growth':
			dict["fieldToSearch"] = a
		elif a =="profit":
			dict["fieldToSearch"] = a

	if match:		
		for a in match:
			if "date" in dict:
				dict["date2"] = a
			else:
				dict["date"] = a 
				
	
			
	return dict
	


chatInput = "What is the grossprofit of Apple"
dict = parsetext(chatInput)
company = dict["companyname"]
#resp = requests.get('http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols=MSFT&appkey=5kb2erymmv7s5ne6ksqkxt2v')
resp = requests.get('http://edgaronline.api.mashery.com/v2/corefinancials/qtr?companyname=' + company +  '&numperiods=1&appkey=5kb2erymmv7s5ne6ksqkxt2v')
#resp = requests.get('http://edgaronline.api.mashery.com/v2/companies?companynames=*micro*&limit=10&offset=10&sortby=companyName%20asc&appkey=5kb2erymmv7s5ne6ksqkxt2v')
#5kb2erymmv7s5ne6ksqkxt2v
#resp = requests.get('http://edgaronline.api.mashery.com/v2/insiders/summary?fields=issueid,insiderformtype,numTransactions,sumnumTransactions&filter=sumnumTransactions%20gt%201%20AND%20issueid%20eq%20467297&appkey=5kb2erymmv7s5ne6ksqkxt2v')
#if resp.status_code != 200:
    # This means something went wrong.
#    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#    print('{} {}'.format(todo_item['id'], todo_item['summary']))

#print('Created task. ID: {}'.format(resp.json()["grossprofit"]))
 #

fq = ""
d1 = ""
d2 = ""
if "financialquarter" in dict:
	fq = dict["financialquarter"]
fieldToSearch = dict["fieldToSearch"] #"grossprofit"
#debt ratio
#growth rate
#print((resp.json()["result"]["rows"][0]["values"][24]))
rows = (resp.json()["result"]["rows"][0]["values"])
for row in rows:
	if row["field"] == fieldToSearch:
		print(row["value"])



#url = 'http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols=MSFT&appkey=5kb2erymmv7s5ne6ksqkxt2v'
#data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
#response = requests.get(url, data=data)


#debt = debt ratio / liability ratio
#(totalLongterm + Short)present - (totalLongterm + Short)past / past = debt ratio
#(totalliabilities) present - (totalliabilities)present 
