from routes import app
from model.models import *
from flask import jsonify
from tokensJWT import *

@app.route("/export", methods=["GET"])
def export():
    products=Product.query.all()
    pdts=[]
    for pdt in products:
        cat = Category.query.filter_by(id=pdt.category).one()
        pdt_dict={
                'name' : pdt.name,
                'category' : cat.name,
                'stock' : pdt.stock,
                'unit' : pdt.unit,
                'manufac' : pdt.manufac,
                'expiry' : pdt.expiry,
                'price' : pdt.price,         
                'total_sales': pdt.total_sales       
        }
        pdts.append(pdt_dict)
    return jsonify(pdts)
