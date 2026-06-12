from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    'dev-secret-key'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
