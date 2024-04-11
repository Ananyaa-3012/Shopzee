from routes import app
from model.models import *
from flask import request
from flask import jsonify

@app.route("/cart",methods=["GET"])
def cart():
    id=request.args.get('user_id')
    cart=Cart.query.filter_by(user_id=id).all()
    cart_list=[]
    total=0
    for item in cart:
        pdt=Product.query.filter_by(id=item.product_id).one()
        cart_dict = {
            'product_id': item.product_id,
            'name': pdt.name,
            'price': item.price,
            'quantity': item.qty,
            'amount': item.price * item.qty,
        }
        total+=item.price * item.qty
        cart_list.append(cart_dict)
    # print(jsonify({'cart': cart_list, 'total': total}))
    return jsonify({'items': cart_list, 'total': total})


@app.route("/cart/<int:pdt_id>",methods=["GET"])
def cart_item(pdt_id):
    id=request.args.get('user_id')
    cart=Cart.query.filter_by(user_id=id,product_id=pdt_id).one()
    pdt=Product.query.filter_by(id=cart.product_id).one()
    cart_dict = {
        'name': pdt.name,
        'price': cart.price,
        'qty': cart.qty,
        'amount': cart.price * cart.qty,
    }
    return jsonify(cart_dict)

@app.route("/cart_add/<int:pdt_id>",methods=["GET","POST"])
def add_cart(pdt_id):
    pdt=Product.query.filter_by(id=pdt_id).one()
    if request.method=="POST":
        id=request.json['user_id']
        exist_cart=Cart.query.filter_by(user_id=id, product_id=pdt_id).first()
        qty=int(request.json['qty'])
        if exist_cart:
            print("Stock",pdt.stock)
            exist_cart.qty+=qty
            pdt.stock-=qty
            pdt.total_sales+=qty
            db.session.commit()
            return jsonify({'message': 'Cart item updated successfully'})
        new_cart=Cart(user_id=id,product_id=pdt.id,price=pdt.price,qty=qty)
        pdt.stock-=qty
        pdt.total_sales+=qty
        db.session.add(new_cart)
        db.session.commit()
        return jsonify({'message': 'Item added to cart'})

@app.route("/cart_upd/<int:pdt_id>",methods=["GET","POST"])
def upd_cart(pdt_id):
    pdt=Product.query.filter_by(id=pdt_id).one()
    if request.method=="POST":
        id=request.json['user_id']
        qty=int(request.json['qty'])
        cart=Cart.query.filter_by(user_id=id, product_id=pdt_id).one()
        if cart.qty>qty:
            pdt.stock+=(cart.qty-qty)
            pdt.total_sales-=(cart.qty-qty)
        else:
            pdt.stock-=(qty-cart.qty)
            pdt.total_sales+=(qty-cart.qty)
        cart.qty=qty
        db.session.commit()
        return jsonify({'message': 'Cart item updated'})


@app.route("/cart_del/<int:pdt_id>",methods=["POST"])
def del_cart(pdt_id):
    if request.method=="POST":
        pdt=Product.query.filter_by(id=pdt_id).one()
        id=request.json['user_id']
        cart=Cart.query.filter_by(user_id=id, product_id=pdt_id).one()
        pdt.stock+=cart.qty
        pdt.total_sales-=cart.qty
        db.session.delete(cart)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'})


@app.route("/cart_clear",methods=["GET"])
def clear_cart():
    id=request.json['user_id']
    cart=Cart.query.filter_by(user_id=id).all()
    for i in cart:
        pdt=Product.query.filter_by(id=i.product_id).one()
        pdt.stock+=i.qty
        pdt.total_sales-=i.qty
        db.session.delete(i)
        db.session.commit()
    return jsonify({'message': 'Cart cleared successfully'})

@app.route("/checkout", methods=["GET","POST"])
def checkout():
        if request.method=="POST":
            id=request.json['user_id']
            cart=Cart.query.filter_by(user_id=id).all()
            for item in cart:
                pdt=Product.query.filter_by(id=item.product_id).one()
                db.session.add(Order(user_id=id, pdt_name=pdt.name, qty=item.qty, price=item.price))
                db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Redirecting to your orders... Please wait' })
        
        elif request.method=="GET":
            id=request.args.get('user_id')
            times=db.session.query(Order.time).filter_by(user_id=id).distinct().all()
            order=Order.query.filter_by(user_id=id).all()
            orders = []
            order_list=[]
            for time in times:
                for row in order:
                    if row.time == time.time:
                        orders.append({
                            'time': time.time,
                            'product': row.pdt_name,
                            'quantity': row.qty,
                            'amount': row.price*row.qty,
                        })   
                order_list.append(orders)
                orders=[]
            return jsonify({'orders': order_list})
    
