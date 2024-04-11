from routes import app
from model.models import *
from flask import request, jsonify
import base64
import os

@app.route("/cat_create", methods=["POST"])
def create_category():
    if request.method=="POST":
        if 'image' not in request.files:
            return jsonify({"message":"image not found"}), 400
        
        image = request.files['image']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(filepath)

        cat = Category(
            image = image.filename,
            name = request.form['name'],
            desc = request.form['desc'],
        )
        db.session.add(cat)
        db.session.commit()
        return jsonify({'message':'New Category sent for Admin Approval'})


@app.route("/cat_update/<int:id>", methods=["POST"])
def update_category(id):
    if request.method=="POST":
        cat=Category.query.filter_by(id=id).one()  
        if cat:
            image = request.files['image']
            if image:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(filepath)
                cat.new_image=image.filename
  
            cat.new_desc=request.form["desc"]    
            cat.approval=3
            db.session.commit()

            img_path = os.path.join('static', 'images', cat.image)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
                cat_dict = {
                    'img' : base64_encoded_data,
                    'name' : cat.name,
                    'desc' : cat.desc
                }
                return jsonify({'message': 'Category update sent for approval'})
        else:
            return jsonify({"error":"category not found"}),409

@app.route("/store/cat_delete/<int:id>", methods=["GET","POST"])
def store_delete_category(id):
    if request.method=="POST":
        cat=Category.query.filter_by(id=id).one()    
        cat.approval=2
        db.session.commit()
        return jsonify({"message":"cat_delete"})
    return jsonify({"message":"cat_delete"})

#Admin Routes #create = 0; approved = 1; delete = 2; update = 3;
@app.route("/admin/cat_create", methods=["POST"])
def admin_create_category():
    if request.method=="POST":
        if 'image' not in request.files:
            return jsonify({"message":"image not found"}), 400
        
        image = request.files['image']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(filepath)

        cat = Category(
            image = image.filename,
            name = request.form['name'],
            desc = request.form['desc'],
            approval = 1
        )
        db.session.add(cat)
        db.session.commit()
        return jsonify({"message":"category created"})
    
@app.route("/admin/cat_update/<int:id>", methods=["POST"])
def admin_update_category(id):
    if request.method=="POST":
        cat=Category.query.filter_by(id=id).one()  
        if cat:
            image = request.files['image']
            if image:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(filepath)
                cat.image=image.filename
  
            cat.desc=request.form["desc"]    
            db.session.commit()
            return jsonify({'message': 'Category updated successfully'})
        else:
            return jsonify({"error":"category not found"}),409

@app.route("/cat_delete/<int:id>", methods=["GET","POST"])
def delete_category(id):
    if request.method=="POST":
        cat=Category.query.filter_by(id=id).one()    
        db.session.delete(cat)
        db.session.commit()
        return jsonify({"message":"category deleted"})
    return jsonify({"message":"cat_delete"}) 