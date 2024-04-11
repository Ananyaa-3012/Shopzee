from routes import app
from model.models import *
from flask import request
from tokensJWT import *
import base64
import os
import datetime

@app.route("/register", methods=["GET","POST"])
def user_signup():
    if request.method=="POST": 
        name=request.json["name"]
        eml=request.json["email"]
        pwd=request.json["password"]
        adrs=request.json["address"]
        if User.query.filter_by(email=eml).first():
            return jsonify({'message':"Email already has an account"}), 409
        usr=User(name=name,email=eml,password=pwd, address=adrs)
        db.session.add(usr)
        db.session.commit()
        token = user_token(eml)
        user=User.query.filter_by(email=eml).first()
        return jsonify({'message':"User Created", 'token': token, 'userType' : 'user', 'userId': user.id})

@app.route("/login", methods=["POST"])
def user_login():
    email=request.json["email"]
    pwd=request.json["password"]
    user=User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message':'Invalid'})
    if user.password == pwd:
        token = user_token(email)
        user.login_time=datetime.datetime.now()
        db.session.commit()
        return jsonify({'token':token, 'userType': 'user', 'userId': user.id})
    else:
        return jsonify({'message':'Invalid'})


@app.route("/search", methods=["POST"])
def search():
    query=request.json['query']
    type = request.json['type']
    if type=='category':
        get_cat=Category.query.filter(Category.name.like(f'%{query}%')).all()
        categories=[]
        for cat in get_cat:
            img_path = os.path.join('static', 'images', cat.image)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                base64_encoded_data = base64.b64encode(img_data).decode('utf-8')  # Encode as Base64

            cat_dict = {
                'id' : cat.id,
                'image':base64_encoded_data,
                'name':cat.name,
                'desc':cat.desc
            }
            categories.append(cat_dict)
        return jsonify({'categories':categories})
    elif type=='product':
        cat = request.json['category']
        get_pdt=Product.query.filter_by(category=cat).filter(Product.name.like(f'%{query}%')).all()
        product=[]

        for pdt in get_pdt:
            img_path = os.path.join('static', 'images', pdt.image)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
            
            pdt_dict = {
                'id' : pdt.id,
                'image':base64_encoded_data,
                'name':pdt.name,
                'manufac':pdt.manufac,
                'expiry':pdt.expiry,
                'price':pdt.price
            }
            product.append(pdt_dict)
        return jsonify({'products':product})

@app.route("/user/profile", methods=["GET"])
def user_profile():
    user_id = request.args.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_dict={
            'name': user.name,
            'email': user.email,
            'address': user.address,
            }
        return jsonify(user_dict)
    else:
        return jsonify({'message': 'User not found'})