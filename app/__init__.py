from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from flask_script import Manager
from flask_migrate import Migrate
import os




app = Flask(__name__, static_folder='../client/build', static_url_path='/')
if os.environ.get('DATABASE_URL'):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:n&6e-oca@localhost/flask'
SECRET_KEY = app.config['SECRET_KEY'] = '5bec7e1b45fb18a457ea033f'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from app import routes
from app import api
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
