from routes import app
from model.models import *
from flask import request
from tokensJWT import *
import os 
import base64


@app.route("/admin/login", methods=["POST"])
def admin_login():
        email=request.json["email"]
        pwd=request.json["password"]
        try:
            admin=Admin.query.filter_by(email=email).first()
            if admin and pwd==admin.password:
                token = admin_token(email)
                print('Token')
                return jsonify({'token':token, 'userType': 'admin'})
            else:
                 return jsonify({'message':'Invalid'})
        except:
             return jsonify({'message':'ABC'})

@app.route("/approval/managers", methods=["GET","POST"])
def approval_managers():
    if request.method == "POST":
        id = request.json['id']
        code = request.json['code']
        manager = StoreManager.query.filter_by(id=id).first()
        manager.approval = int(code)
        db.session.commit()
        return jsonify({'message':'Approval Success'})
    elif request.method == "GET":
        managers = StoreManager.query.filter_by(approval=0).all()
        manager_list=[]
        for x in managers:
            manager_dict={
                 'id': x.id,
                 'name': x.name,
                 'email': x.email,
                 'approval': x.approval
            }             
            manager_list.append(manager_dict)
        return jsonify({'managers': manager_list})


#create = 0; approved = 1; delete = 2; update = 3;
@app.route("/approval/categories", methods=["GET"])
def approval_categories():
    code = request.args.get('code')
    cat=[]
    if code in ("0","2"):
        categories = Category.query.filter_by(approval=code).all()
        for item in categories:
            img_path = os.path.join('.','static', 'images', item.image)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                base64_encoded_data = base64.b64encode(img_data).decode('utf-8')
            cat_dict={
                'id': item.id,
                'name': item.name,
                'desc': item.desc,
                'image': base64_encoded_data,
            }
            cat.append(cat_dict)

    if code=="3":
        categories = Category.query.filter_by(approval=code).all()
        for item in categories:
            img_path = os.path.join('.','static', 'images', item.image)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                img = base64.b64encode(img_data).decode('utf-8')

            img_path = os.path.join('.','static', 'images', item.new_image)
            with open(img_path, 'rb') as f:
                img_data = f.read()
                new_img = base64.b64encode(img_data).decode('utf-8')
            cat_dict={
                'id': item.id,
                'name': item.name,
                'desc': item.desc,
                'new_desc': item.new_desc,
                'image': img,
                'new_image': new_img
            }
            cat.append(cat_dict)
    return jsonify(cat)

@app.route("/approval/category/<int:id>", methods=["POST"])
def upd_approve_categories(id):
    code=request.json['code']
    print(code)
    cat=Category.query.filter_by(id=id).first()
    if code==3:
        cat.desc,cat.new_desc=cat.new_desc,''
        cat.image,cat.new_image=cat.new_image,''
        cat.approval=1
        db.session.commit()
        return jsonify({'message':'Updated'})
    elif code==0:
        cat.approval=1
        db.session.commit()
        return jsonify({'message':'Approved'})

@app.route("/reject/category/<int:id>", methods=["POST"])
def reject_category(id):
    code=request.json['code']
    cat=Category.query.filter_by(id=id).first()
    if code==3:
        cat.new_desc=''
        cat.new_image=''
        cat.approval=1
        db.session.commit()
        return jsonify({'message':'Rejected'})
    elif code==2:
        cat.approval=1
        db.session.commit()
        return jsonify({'message':'Rejected'})
