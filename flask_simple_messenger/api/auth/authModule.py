from flask import Blueprint, request, make_response, jsonify
from app import App
from api.auth.user.userModel import User
from api.auth.session.sessionModel import Session
from api.auth.user.userForm import LoginForm, RegistrationForm

db = App.db()

def validateToken():
    token = request.cookies['authToken']
    session = Session.query.filter_by(token=token).first()
    if not(session):
        response = make_response('noSuchToken,')
        return response
    response = make_response('OK')
    return response

def createUserSession(user):
    token = user.username
    session = Session(user_id=user.id, token=token)
    db.session.add(session)
    db.session.commit()
    return session


def register():
    form = RegistrationForm(request.form)
    if not(form.validate()):
        response = jsonify(errors=form.errors)
        return response
    newUser = User(
        username=form.data['username'],
        password=form.data['password'],
        )
    db.session.add(newUser)
    db.session.commit()
    response = make_response('OK')
    return response


def login(): #TODO reduce quantity of database queries for user with given username
    form = LoginForm(request.form)
    if not(form.validate()):
        response = jsonify(errors=form.errors)
        return response
    user = User.query.filter_by(username=form.data['username']).first()
    session = Session.query.filter_by(user_id=user.id).first() or createUserSession(user)
    token = session.token
    response = make_response('OK')
    response.set_cookie('authToken', token)
    return response


def logout():
    if not('authToken' in request.cookies.keys()):
        response = make_response('OK')
        return response
    token = request.cookies['authToken']
    session = Session.query.filter_by(token=token).first()
    if session:
        db.session.delete(session)
    response = make_response('OK')
    response.delete_cookie('authToken')
    return response



class AuthModule(Blueprint):

    def __init__(self):
        super().__init__('auth', 'auth', url_prefix='/auth')

        self.setRouting()

    def setRouting(self):
        self.add_url_rule('/register', 'register', register, methods=['POST'])
        self.add_url_rule('/login', 'login', login, methods=['POST'])
        self.add_url_rule('/logout', 'logout', logout, methods=['POST'])

