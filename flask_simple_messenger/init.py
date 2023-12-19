from app import App
from api.auth.authModule import AuthModule

app = App.app()
db = App.db()

app.register_blueprint(AuthModule())

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True,host='0.0.0.0')