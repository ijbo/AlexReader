from flask import Flask
from flask_ask import Ask, statement, question, session
import json ##interact with redit api
import requests ## interact with redit api
import time
import unidecode
import os, sys

app = Flask(__name__)
ask = Ask(app,"/")

@app.route('/')
def homepage():
    print ("Alex connect")
    return "hi there, how ya doing ?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, Would you like to know more about Turbo Charging ?'
    return question(welcome_message).reprompt("Can you please say Yes or NO")

#Yes
@ask.intent("YesIntent")
def Turbocharger():
    headlines_msg = 'Turbo Charging is a single charging platform for online and offline operations. ' \
                    'Innovative Turbo Charging technology delivers breakthrough performance for complex and real-time rating. ' \
                    'Massive scalability for demanding growth and services. ' \
                    'Its architecture is for mass distribution over low-cost servers'
    headlines_msg += 'Do you like to know more about turbo charging functionality , say Sure or no to exit'
    return question(headlines_msg).reprompt("please say sure to continue or no to exit")

#No
@ask.intent("NoIntent")
def no_intent():
    bye_text="I can also be configured to " \
             "1 Run production health check queries, " \
             "2 Monitor production for you , " \
             "3 Scan Errors in the logs " \
             "4 Fetch configurable data from Database" \
             "The tech genie is out of the bottle; you can't put it back in."
    return statement(bye_text)


@ask.intent("functionality")
def TC_functionality():
    functionality_text='It does the following    ' \
                       'Guiding to customer,  ' \
                       'Identify Pricing Items, ' \
                       'Apply Pricing Logic, ' \
                       'Hold Prepaid Balance, ' \
                       'Publish Rated Information,Rerate Events       '
    functionality_text += 'Do you like to know more about turbo charging major components, say absolutely or no to exit'
    return question(functionality_text).reprompt("You can say absolutely to continue or no to exit")

# #@ask.launch
# def start_skill_2():
#      welcome_message_2 = 'Do you like to know more about turbo charging major components, say absolutely'
#      return question(welcome_message_2)
#         #absolutely

@ask.intent("majorcomponents")
def majorcomponents():
    majorcomponents_text='The Major Components in Turbo charging are , A V M Availability Manager, ' \
                         'E S Event Server R B and F R, ' \
                         'U H Update Handler, ' \
                         'DB2E Database to event, ' \
                         'IMDG In memory data grid'
    majorcomponents_text += 'Which component you want to know more about AVM or Event Server or no to exit?'
    return question(majorcomponents_text).reprompt("want to know more about AVM or Event server or no to exit")

# #@ask.launch
# def start_skill_3():
#     welcome_message_3 = 'Do you want to know about any specific component AVM, Event Server, Which component you want to know more about AVM or Event Server ?'
#     return question(welcome_message_3)
#             #AVM

@ask.intent("AVMdetials")
def AVMdetials():
    AVMdetials_txt="AVM The Availability Manager (AVM) is responsible for maintaining a highly " \
                   "available system as well as detecting failures of network entities in real-time. " \
                   "When a crash of a network node is detected, the Availability Manager processes " \
                   "the incoming event and immediately invokes a set of commands to handle it. " \
                   "It also updates its internal network snapshot." \
                   "DO you want to know about E S say Event Server or no to exit"
    return question(AVMdetials_txt).reprompt("want to know about ES say Event Server or no to exit")

#EVENT SERVER
@ask.intent("ESdetials")
def ESdetials():
    ESdetials_text='The Event Server is The heart of Turbo Charging, ' \
                   'A single process which handles all main flows Event Processor. ' \
                   'All input to E S are events. It replaces Enabler '
    return question(ESdetials_text).reprompt("if you want to repeat please say Turbo charging sessions or no to exit ")

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()
