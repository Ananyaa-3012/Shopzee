from routes import app
from model.models import *
from flask import jsonify
import base64
import os
from datetime import date
import redis
from tokensJWT import *


@app.route("/pdt_view/<int:cid>", methods=["GET"])
# @jwt_required
def view_products(cid):
    cat=Category.query.filter_by(id=cid).first()
    data=Product.query.filter_by(category=cid).all()
    product=[]
    today = date.today()
    for pdt in data:
        year, month, day = map(int, pdt.expiry.split('-'))
        expiry_date = date(year, month, day)
        if expiry_date >= today:
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
                'price':pdt.price,
                'stock' : pdt.stock,
                'unit' : pdt.unit,
                'category' : pdt.category
            }
            product.append(pdt_dict)
    return jsonify(product)


@app.route("/getProduct/<int:id>", methods=["GET"])
# @jwt_required
def view_product(id):
    pdt=Product.query.filter_by(id=id).first()

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
        'price':pdt.price,
        'stock' : pdt.stock,
        'unit' : pdt.unit,
        'category' : pdt.category
    }
    return jsonify(pdt_dict)
