from app import App
from api.auth.authModule import AuthModule
from api.messenger.messengerModule import MessengerModule

app = App.app()
db = App.db()

app.register_blueprint(AuthModule())
app.register_blueprint(MessengerModule())

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True,host='0.0.0.0')