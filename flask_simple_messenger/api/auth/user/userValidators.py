from wtforms import ValidationError

from api.auth.user.userModel import User


class UsernameIsNotOccupied:
    def __init__(self) -> None:
        self.message = 'This Username is Already Occupied'
    
    def __call__(self, form, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError(self.message)


class UserIsRegistred:
    def __init__(self) -> None:
        self.message = 'No User with Such Username'
    
    def __call__(self, form, field):
        user = User.query.filter_by(username=field.data).first()
        if not(user):
            raise ValidationError(self.message)


class PasswordIsMatching:
    def __init__(self) -> None:
        self.message = 'Wrong Password'
    
    def __call__(self, form, field):
        user = User.query.filter_by(username=form.username.data).first()
        if not(user):
            return
        if user.password != field.data:
            raise ValidationError(self.message)
