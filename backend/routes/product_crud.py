from routes import app
from model.models import *
from flask import request, jsonify
import os
import base64

@app.route("/pdt_create/<int:id>", methods=["GET","POST"])
def create_product(id):
    if request.method=="GET":
        return jsonify({"message": "pdt_create"})
    
    if request.method=="POST":
        try:
            cat = Category.query.filter_by(id=id).one()
            if cat:
                if 'image' not in request.files:
                    return jsonify({"message":"no image selected"}), 400
                
                image = request.files['image']
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(filepath)
                pdt_name=request.form["name"]
                prod = Product.query.filter_by(name=pdt_name).first()
                if prod:
                    return jsonify({"message":"product already exists"}), 409
                pdt = Product(        
                    image=image.filename,
                    name=pdt_name,
                    category=id,
                    stock=request.form["stock"],
                    unit=request.form["unit"],
                    manufac=request.form["manufac"],
                    expiry=request.form["expiry"],
                    price=request.form["price"]
                )

                db.session.add(pdt)
                db.session.commit()

                img_path = os.path.join('static', 'images', pdt.image)
                with open(img_path, 'rb') as f:
                    img_data = f.read()
                    base64_encoded_data = base64.b64encode(img_data).decode('utf-8')

                pdt_dict = {
                    'img' : base64_encoded_data,
                    'name' : pdt.name,
                    'stock' : pdt.stock,
                    'unit' : pdt.unit,
                    'manufac' : pdt.manufac,
                    'expiry' : pdt.expiry,
                    'price' : pdt.price,
                    'category' : pdt.category
                }
                return jsonify(pdt_dict)
            
        except:
            return jsonify({"message":"category not found"}), 404

@app.route("/pdt_update/<int:cat_id>/<int:pdt_id>", methods=["GET","POST"])
def update_product(cat_id,pdt_id):
    cat=Category.query.filter_by(id=cat_id).one()
    if request.method=="GET":
        products=Product.query.all()
        pdts=[]
        for pdt in products:
            pdt_dict={
                'name' : pdt.name,
                'category' : cat.name,
                'stock' : pdt.stock,
                'unit' : pdt.unit,
                'manufac' : pdt.manufac,
                'expiry' : pdt.expiry,
                'price' : pdt.price                
            }
            pdts.append(pdt_dict)
        return jsonify(pdts)
    if request.method=="POST":
        if cat:
            pdt=Product.query.filter_by(id=pdt_id).one()  
            if pdt:
                image = request.files['image']
                if image:
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                    image.save(filepath)
                    pdt.image=image.filename
    
                print(request.form)
                pdt.category=cat_id
                pdt.stock=request.form["stock"]
                pdt.unit=request.form["unit"]
                pdt.manufac=request.form["manufac"]
                pdt.expiry=request.form["expiry"]
                pdt.price=request.form["price"]
                db.session.commit() 

                img_path = os.path.join('static', 'images', pdt.image)
                with open(img_path, 'rb') as f:
                    img_data = f.read()
                    base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
                    pdt_dict = {
                        'img' : base64_encoded_data,
                        'name' : pdt.name,
                        'stock' : pdt.stock,
                        'unit' : pdt.unit,
                        'manufac' : pdt.manufac,
                        'expiry' : pdt.expiry,
                        'price' : pdt.price,
                        'category' : pdt.category
                    }
                    return jsonify(pdt_dict)
            else:
                return jsonify({"message":"product not found"}),404
        else:
            return jsonify({"message":"category not found"}),404
    
@app.route("/pdt_delete/<int:pid>", methods=["GET","POST"])
def delete_product(pid):
    if request.method=="POST":
        pdt=Product.query.filter_by(id=pid).one()        
        db.session.delete(pdt)
        db.session.commit()
        return jsonify({"message":"product deleted"})
    return jsonify({"message":"delete product"})
