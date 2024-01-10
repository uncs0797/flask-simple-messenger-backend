from flask import Blueprint, jsonify, make_response, request

from api.auth.user.userModel import User
from api.auth.session.sessionModel import Session
from api.messenger.message.messageModel import Message
from app import App
from api.auth.authModule import validateToken

db = App.db()

def getMessages():
    response, user = validateToken()
    if not(user):
        return response
    contactID = request.form['contact']
    contact = User.query.filter_by(id=contactID).first()
    outcommingMessagesQuery = Message.query.filter_by(reciever_id=contact.id, sender_id=user.id)
    incommingMessagesQuery = Message.query.filter_by(reciever_id=user.id, sender_id=contact.id)
    messageList = incommingMessagesQuery.union(outcommingMessagesQuery).all()
    messageList = [{'id':message.id, 
                    'sender':message.sender.username, 
                    'reciever':message.reciever.username, 
                    'message':message.message,
                    } for message in messageList]
    response = jsonify(messageList)
    return response

def postMessage():
    response, user = validateToken()
    if not(user):
        return response
    contactID = request.form['contact']
    contact = User.query.filter_by(id=contactID).first()
    if not(contact):
        return 'not valid reciever'
    messageBody = request.form['message']
    if not(messageBody):
        return 'message is empty'
    message = Message(sender_id=user.id, reciever_id=contact.id, message=messageBody)
    db.session.add(message)
    db.session.commit()
    return 'message posted'

class MessagesModule(Blueprint):

    def __init__(self):
        super().__init__('messages', 'messages', url_prefix='/messages')

        self.setRouting()

    def setRouting(self):
        self.add_url_rule('/', 'getMessages', getMessages, methods=['GET'])
        self.add_url_rule('/', 'postMessageToUser', postMessage, methods=['POST'])