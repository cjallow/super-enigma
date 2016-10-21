#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

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
	dict["fieldToSearch"] = []
	for (a,b) in tags:
		if b == 'NN' or a =='gross':
			keywords.append(a)
		if b == 'NNP':
			dict["companyname"] = a
		if a == 'first' or a == 'second' or a == 'third' or a == 'fourth':
			dict["financialquarter"] = quarters[a]
			
	for a in keywords:
		dict["fieldToSearch"].append(a)

	if match:		
		for a in match:
			if "date" in dict:
				dict["date2"] = a
			else:
				dict["date"] = a 
				
	print (dict)
	return dict
	
	
	#if a =='debt':
	#		dict["fieldToSearch"] = a
	#	elif a =='growth':
	#		dict["fieldToSearch"] = a
	#	elif a =="profit":
	#		dict["fieldToSearch"] = a
	
	

def connectToEdgar(chatInput):
	chatInput = "What is the gross profit of AAPL"
	dict = parsetext(chatInput)
	company = dict["companyname"]
	#resp = requests.get('http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols=MSFT&appkey=5kb2erymmv7s5ne6ksqkxt2v')
	resp = requests.get('http://edgaronline.api.mashery.com/v2/corefinancials/qtr?primarysymbols=' + company +  '&numperiods=1&appkey=5kb2erymmv7s5ne6ksqkxt2v')
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

	DictConv = {'profit': 'grossprofit'}

	 
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
	for n in fieldToSearch:
        #if n == "debt"
		for row in rows:
			if (n in DictConv) and (row["field"] == DictConv[n]):
				print(row["value"])
				return (str(row["value"]))



	#url = 'http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols=MSFT&appkey=5kb2erymmv7s5ne6ksqkxt2v'
	#data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
	#response = requests.get(url, data=data)


	#debt = debt ratio / liability ratio
	#(totalLongterm + Short)present - (totalLongterm + Short)past / past = debt ratio
	#(totalliabilities) present - (totalliabilities)present 





	
# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None



def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    #while True:
    #    socketio.sleep(10)
	#count += 1
	#socketio.emit('my_response',
	#			  {'data': 'Server generated event', 'count': count},
	#			  namespace='/test')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': "Me:                     " + message['data'], 'count': session['receive_count']},
         broadcast=True)
    response = connectToEdgar(message)
    emit('my_response',
         {'data': "Crystal Ball: " + str(response), 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close_room', namespace='/test')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my_room_event', namespace='/test')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)
