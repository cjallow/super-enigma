import requests
import urllib.parse

encodedURL = 'http://edgaronline.api.mashery.com/v2/'
query = 'insiders/summary?fields=issueid,insiderformtype,numTransactions,sumnumTransactions&filter=sumnumTransactions%20gt%201%20AND%20issueid eq 467297&appkey=5kb2erymmv7s5ne6ksqkxt2v'
apiKey= '&appkey=5kb2erymmv7s5ne6ksqkxt2v'

query = urllib.parse.urlencode(query)

encodedURL = encodedURL +query+apiKey

chatInput = ""

print (encodedURL)
resp = requests.get(encodedURL)
#5kb2erymmv7s5ne6ksqkxt2v
#resp = requests.get('http://edgaronline.api.mashery.com/v2/insiders/summary?fields=issueid,insiderformtype,numTransactions,sumnumTransactions&filter=sumnumTransactions%20gt%201%20AND%20issueid eq 467297&appkey=5kb2erymmv7s5ne6ksqkxt2v')
#if resp.status_code != 200:
    # This means something went wrong.
#    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#    print('{} {}'.format(todo_item['id'], todo_item['summary']))

print (resp.json())
# what is the gross rate for compny x for year x

#["result"]["rows"]["values"][27]
#presentvalue pastvalue