import requests
import json

 
chatInput = ""
#resp = requests.get('http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols=MSFT&appkey=5kb2erymmv7s5ne6ksqkxt2v')
resp = requests.get('http://edgaronline.api.mashery.com/v2/corefinancials/qtr?primarysymbols=MSFT&numperiods=1&appkey=5kb2erymmv7s5ne6ksqkxt2v')
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
fieldToSearch = "grossprofit"
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


debt = debt ratio / liability ratio
(totalLongterm + Short)present - (totalLongterm + Short)past / past = debt ratio
(totalliabilities) present - (totalliabilities)present 
