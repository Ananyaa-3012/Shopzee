from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import redis

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'anan3012'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopzee.db"
app.config["UPLOAD_FOLDER"] = "static/images"

from model import *
from routes import admin
from routes import user
from routes import store
from routes import store_profile
from routes import cart_crud
from routes import category_crud
from routes import product_crud
from routes import categories
from routes import products

with app.app_context():
    db.init_app(app)
    db.create_all()