from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from routes import db

#--------------------MODELS-----------------
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, unique=True, nullable=False)
    password=db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)
    login_time = db.Column(db.DateTime(timezone=True))
    order=db.relationship('Order', cascade='delete')
    cart = db.relationship('Cart', cascade='delete')

class StoreManager(db.Model):
    __tablename__='storemanager'
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, unique=True, nullable=False)
    password=db.Column(db.String, nullable=False)
    approval = db.Column(db.Integer, default=0)
    
class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, unique=True, nullable=False)
    password=db.Column(db.String, nullable=False)
    
class Category(db.Model):
    __tablename__='category'
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name=db.Column(db.String, unique=True, nullable=False)
    desc=db.Column(db.String, nullable=False)
    image=db.Column(db.String)
    approval = db.Column(db.Integer, default=0)
    new_desc=db.Column(db.String, default=None)
    new_image=db.Column(db.String, default=None)
    pdt = db.relationship('Product', cascade='delete')   

class Product(db.Model):
    __tablename__='product'
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name=db.Column(db.String, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    stock=db.Column(db.Integer, nullable=False)
    unit=db.Column(db.Integer, nullable=False)
    manufac=db.Column(db.String)
    expiry=db.Column(db.String)
    price=db.Column(db.Integer, nullable=False)
    image=db.Column(db.String)
    approval = db.Column(db.Integer, default=0)
    total_sales=db.Column(db.Integer, default=0)
    order = db.relationship('Order')  
    cart = db.relationship('Cart', cascade='delete') 

class Cart(db.Model):
    __tablename__='cart'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
    price=db.Column(db.Integer)
    qty=db.Column(db.Integer, nullable=False)
    
class Order(db.Model):
    __tablename__='order'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    pdt_name=db.Column(db.String, db.ForeignKey('product.name'))
    price=db.Column(db.Integer)
    qty=db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime(timezone=True), server_default=func.now())


