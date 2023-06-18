from twilio.rest import Client
from config import TWILIO_AUTH_KEY, TWILIO_SID


account_sid = TWILIO_SID
auth_token = TWILIO_AUTH_KEY
client = Client(account_sid, auth_token)

def send_sms(phone_number: str, msg: str):
    client.messages \
        .create(
            body=msg,
            from_='+1555555555',
            to=phone_number
        )
    
def make_call(phone_number: str, msg: str):
    client.calls.create(
            twiml=f'<Response><Say>{msg}</Say></Response>',
            to=phone_number,
            from_='+1555555555'
        )