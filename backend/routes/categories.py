from routes import app
from model.models import *
from flask import session, request, jsonify
import base64
import os
import base64
import redis
import json
from tokensJWT import *

redis_cli = redis.Redis(host="localhost", port=6379, db=0)


    # @app.route("/clear-cache", methods=["POST"])
    # # @jwt_required
    # def clear_cache():
    #     try:

    #         return jsonify({'message': 'Cache cleared successfully'}), 200
    #     except Exception as e:
    #         return jsonify({'error': str(e)}), 500

@app.route("/user/category", methods=["GET"])
# @jwt_required
def user_category():
    category_cache = redis_cli.get('category_cached')
    if category_cache:
        return category_cache.decode('utf-8')

    data = Category.query.filter_by(approval=1).all()
    categories = []

    for cat in data:
        img_path = os.path.join('.','static', 'images', cat.image)
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
    cat_json = json.dumps(categories)
    redis_cli.setex('category_cached', 1800, cat_json.encode('utf-8'))  
    return cat_json

@app.route("/category", methods=["GET"])
# @jwt_required
def all_category():
    data = Category.query.filter_by(approval=1).all()
    categories = []

    for cat in data:
        img_path = os.path.join('.','static', 'images', cat.image)
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
    cat_json = json.dumps(categories)
    redis_cli.setex('category_cached', 1800, cat_json.encode('utf-8'))  
    return cat_json


@app.route("/getCategory/<int:id>", methods=["GET"])
# @jwt_required
def one_category(id):
    cat = Category.query.filter_by(approval=1, id=id).one()

    img_path = os.path.join('.','static', 'images', cat.image)
    with open(img_path, 'rb') as f:
        img_data = f.read()
        base64_encoded_data = base64.b64encode(img_data).decode('utf-8')  # Encode as Base64

    cat_dict = {
        'id' : cat.id,
        'image':base64_encoded_data,
        'name':cat.name,
        'desc':cat.desc
    }
    
    return jsonify(cat_dict)