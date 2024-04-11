from routes import app
from model.models import *
from flask import request, jsonify
from tokensJWT import *

@app.route("/store/register", methods=["GET","POST"])
def signup():
    if request.method=="POST": 
        name=request.json["name"]
        email=request.json["email"]
        password=request.json["password"]
        if StoreManager.query.filter_by(email=email).first():
            return jsonify({'message':"Email already has an account"}), 409

        # Create a new store manager profile
        new_store_manager = StoreManager(
            name=name,
            email=email,
            password=password,
        )
        db.session.add(new_store_manager)
        db.session.commit()
        token = store_token(email)
        store=StoreManager.query.filter_by(email=email).first()
        return jsonify({'message': 'Store manager profile created, awaiting admin approval', 'token': token, 'userType' : 'storeManager', 'userId': store.id}), 201

@app.route("/store/login", methods=["GET", "POST"])
def store_login():
        email=request.json["email"]
        pwd=request.json["password"]
        try:
            store=StoreManager.query.filter_by(email=email).first()
            if store and pwd==store.password:
                print(store.approval)
                if int(store.approval)==0:
                     return jsonify({'message':'Account approval pending'}), 409
                elif int(store.approval)==-1:
                     return jsonify({'message':'Your account has been suspended. Kindly login with another account'}), 409
                token = store_token(email)
                return jsonify({'token':token, 'userId': store.id, 'userType' : 'storeManager'})
            else:
                 return jsonify({'message':'Invalid Credentials'}), 409
        except:
             return jsonify({'message':'ABC'}),409
