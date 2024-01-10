from wtforms import Form, StringField, PasswordField, validators

from api.auth.user.userValidators import PasswordIsMatching, UserIsRegistred, UsernameIsNotOccupied


class RegistrationForm(Form):
    username = StringField('Username', [
        validators.Length(min=4, max=25), 
        UsernameIsNotOccupied()
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    username = StringField('Username', [
        validators.Length(min=4, max=25),
        UserIsRegistred()
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        PasswordIsMatching(),
    ])