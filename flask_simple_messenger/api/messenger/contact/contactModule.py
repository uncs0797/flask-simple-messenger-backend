from flask import Blueprint, jsonify, request

from api.auth.user.userModel import User
from app import App
from api.auth.authModule import validateToken
from api.messenger.contact.contactModel import Contact

db = App.db()

def getContacts():
    response, user = validateToken()
    if not(user):
        return response
    contactListLeft = Contact.query.join(User, Contact.contact2_id==User.id).filter((Contact.contact1 == user)).with_entities(Contact.contact2_id.label('contact_id'),  User.username.label('contact_name'))
    contactListRight = Contact.query.join(User, Contact.contact1_id==User.id).filter((Contact.contact2 == user)).with_entities(Contact.contact1_id.label('contact_id'), User.username.label('contact_name'))
    contactList = contactListLeft.union(contactListRight).all()
    contactList = [{'contact_id':contact.contact_id, 
                    'contact_name':contact.contact_name, 
                    } for contact in contactList]
    response = jsonify(contactList)
    return response

def postContact():
    response, user = validateToken()
    if not(user):
        return response
    contactID = request.form['contact']
    contactUser = User.query.filter_by(id=contactID).first()
    if not(contactUser):
        return 'no such user'
    contact = Contact(contact1_id=user.id, contact2_id=contactUser.id,)
    db.session.add(contact)
    db.session.commit()
    return 'contact posted'

class ContactModule(Blueprint):

    def __init__(self):
        super().__init__('contacts', 'contacts', url_prefix='/contacts')

        self.setRouting()

    def setRouting(self):
        self.add_url_rule('/', 'getContacts', getContacts, methods=['GET'])
        self.add_url_rule('/', 'postContact', postContact, methods=['POST'])