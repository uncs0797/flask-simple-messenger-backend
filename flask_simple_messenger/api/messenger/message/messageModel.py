from app import App
from api.auth.user.userModel import User


db = App.db()


class Message(db.Model):

    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reciever_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False) 

    sender = db.relationship(User, 
                             foreign_keys=[sender_id],
                             backref='outcommingMessages',
                             )
    reciever = db.relationship(User, 
                               foreign_keys=[reciever_id],
                               backref='incommingMessages',
                               )

    def __repr__(self):
        return f'<Message from {self.sender_id} to {self.reciever_id}, \'{self.message}\'>' 