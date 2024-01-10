from app import App
from api.auth.user.userModel import User

db = App.db()


class Contact(db.Model):

    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    contact1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contact2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    contact1 = db.relationship(User, 
                             foreign_keys=[contact1_id],
                             )
    contact2 = db.relationship(User, 
                               foreign_keys=[contact2_id],
                               )

    def __repr__(self):
        return f'<Contact pair of {self.contact1.username} and {self.contact2.username}' 