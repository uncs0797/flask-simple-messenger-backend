from flask import Blueprint

from api.messenger.message.messageModule import MessagesModule
from api.messenger.contact.contactModule import ContactModule


class MessengerModule(Blueprint):

    def __init__(self):
        super().__init__('messenger', 'messenger', url_prefix='/messenger')

        self.setRouting()
        self.register_blueprint(MessagesModule())
        self.register_blueprint(ContactModule())

    def setRouting(self):
        pass
