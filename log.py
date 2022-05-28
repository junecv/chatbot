from twilio.rest import Client
from datetime import datetime, timedelta
import pytz
from env import access_secret

account_sid = access_secret('LINK_TO_SECRET')
auth_token = access_secret('LINK_TO_SECRET')
client = Client(account_sid, auth_token)

def get_chatlog(incoming_contact = 'whatsapp:+1__TEST_NUMBER__', hours = 24, minutes = 0):

    # now
    now = datetime.now(tz=pytz.utc)
    chatlog_start_time = now - timedelta(hours=hours, minutes=minutes)

    inbound_messages = client.messages.list(
        date_sent_after = chatlog_start_time,
        to=incoming_contact,
    )

    outbound_messages = client.messages.list(
        date_sent_after = chatlog_start_time,
        from_=incoming_contact,
    )

    inbound_lst = [(i.date_sent, '\nHuman: ' +  i.body)for i in inbound_messages]
    outbound_lst = [(i.date_sent, '\nAI: ' +  i.body) for i in outbound_messages]

    chat_log = inbound_lst + outbound_lst
    chat_log.sort(key = lambda x: x[0])
    chat_log = [i[1] for i in chat_log]

    return chat_log

get_chatlog()
