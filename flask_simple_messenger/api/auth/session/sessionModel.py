from app import App
from api.auth.user.userModel import User


db = App.db()


class Session(db.Model):

    __tablename__ = 'session'
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return f'<Session {self.token}>'    