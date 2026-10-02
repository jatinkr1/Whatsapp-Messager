#step1 installing all required libraries
from twilio rest import Client
from datetime imprt datetime,timedelta
import time

#step2 twilio cridentials
account_sid='xxx'
auth_token='xxx'

client= Client(account_sid,auth_token)

#step3 define send messgae function
def send_whatsapp_message(receipient_number,message_body):
  try:
    message= client.messages.create(
      from_='whatsapp:xxxxxxxxxx',
      body=message_body,
      to=f'whatsapp:{recipient_number},
    )
    print(f'Message sent successfully! Message SID{message.sid}')
  except Exception as e:
    print('An error occured')
