from app import App

db = App.db()

class User(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    sessions = db.relationship('Session', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'