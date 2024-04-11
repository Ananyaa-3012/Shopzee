from functools import wraps
from flask import jsonify, request, make_response
from routes import app
import jwt
import datetime
from model.models import *



def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        print(token)
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            # Decode the token and verify it with your secret key
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            # You can use the username to perform further actions
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
    return decorated



def user_token(email):
    id = User.query.filter_by(email=email).first().id
    token = jwt.encode({'ID': id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},app.config['SECRET_KEY'])
    return token 

def store_token(email):
    
    ID = StoreManager.query.filter_by(email=email).first().id
    token = jwt.encode({'ID': ID, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},app.config['SECRET_KEY'])
    return token 


def admin_token(email):
    
    ID = Admin.query.filter_by(email=email).first().id
    token = jwt.encode({'ID': ID, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},app.config['SECRET_KEY'])
        
    return token 