from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

class App(Flask):

    _app = None
    _db = None

        
    @classmethod
    def app(cls):
        if cls._app is None:
            cls._app = Flask(__name__)
            basedir = os.path.abspath(os.path.dirname(__file__))
            cls._app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
            cls._app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            cls._db = SQLAlchemy(cls._app)
        return cls._app
    
    @classmethod
    def db(cls):
        if cls._db is None:
            cls.app()
        return cls._db


 
