from app import App

app = App.app()
db = App.db()


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True,host='0.0.0.0')