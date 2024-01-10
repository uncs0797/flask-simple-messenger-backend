from flask import Blueprint

from api.messenger.message.messageModule import MessagesModule


class MessengerModule(Blueprint):

    def __init__(self):
        super().__init__('messenger', 'messenger', url_prefix='/messenger')

        self.setRouting()
        self.register_blueprint(MessagesModule())

    def setRouting(self):
        pass
