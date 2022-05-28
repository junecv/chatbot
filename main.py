import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask
from log import get_chatlog

def chatbot(request):

    # get incoming message and session chat_log
    incoming_msg = request.values.get('Body', '').lower()
    incoming_contact = request.values.get('To')

    # generate response message
    response = MessagingResponse()
    response_msg = response.message()

    # initiate repsonse status 
    responded = False

    chat_log = get_chatlog(incoming_contact)
    
    # get answer from GPT-3 model
    r = ask(incoming_msg, chat_log)

    # construct response message
    response_msg.body(r)

    responded = True

    # return response message 
    return str(response)