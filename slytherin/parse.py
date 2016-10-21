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
	