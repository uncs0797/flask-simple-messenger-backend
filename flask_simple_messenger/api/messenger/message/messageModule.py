from flask import Blueprint

def getMessages():
    return 'list of messages'

def postMessage():
    return 'message posted'

class MessagesModule(Blueprint):

    def __init__(self):
        super().__init__('messages', 'messages', url_prefix='/messages')

        self.setRouting()

    def setRouting(self):
        self.add_url_rule('/', 'getMessages', getMessages, methods=['GET'])
        self.add_url_rule('/', 'postMessageToUser', postMessage, methods=['POST'])