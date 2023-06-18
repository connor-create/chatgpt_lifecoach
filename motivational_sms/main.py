import time
import threading
from datetime import datetime
import pytz
import random

from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

from sms import send_sms, make_call
from chatgpt import dan

est_tz = pytz.timezone('US/Eastern')
today_date = est_tz.localize(datetime.now())

task_map = [{
        "start": time(6, 0),
        "task": "go to the gym"
    }, 
    {
        "start": time(12, 0),
        "task": "go for a jog"
    }, 
    {   
        "start": time(18, 0),
        "task": "work on youtube video"
    }, 
    {
        "start": time(22, 0),
        "task": "go to bed"
    }
]

def is_now_between_times(start, end):
    now = est_tz.localize(datetime.now())
    if start < end: 
        return now >= start and now <= end
    else: 
        return now >= start or now <= end
    
def send_motivational_sms():
    send_sms("+15707892341", dan("a very vulgar motivational message to get connor to quit videogames and work on his coding project"))

def make_motivational_call():
    make_call("+15707892341", "you are very lazy, keep working on that video bitch or else you will be a loser the rest of your life, got it?")

def is_now_time(start):
    return True

def monitor():
    while True:
        for task in task_map:
            if is_now_time(task["start"]):
                make_motivational_call() 
        time.sleep(60)

# app = Flask(__name__)

# @app.route('/sms', methods=['POST'])
# def sms():
#     message_body = request.form['Body']
#     resp = MessagingResponse()

#     # resp.message(reply_text )
#     # return str(resp)

if __name__ == '__main__':
    # x = threading.Thread(target=monitor)
    time.sleep(3)
    make_motivational_call()
    # send_motivational_sms()
    # x.start()
    # app.run()