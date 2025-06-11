from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from . import db
from .models import Product, Scent, Order
from datetime import datetime

bp = Blueprint('main', __name__)



@bp.route('/')
def index():
    products = Product.query.order_by(Product.id).all()
    scents = Scent.query.order_by(Scent.id).all()
    return render_template('index.html', products = products, scents = scents, category = 'All products')




@bp.route('/all_products')
def all_products():
    products = Product.query.order_by(Product.id).all()
    scents = Scent.query.order_by(Scent.id).all()
    return render_template('shop.html', products = products, scents = scents, category = 'All products')




@bp.route('/candles')
def candles():
    products = Product.query.filter_by(category='Candle').order_by(Product.id).all()
    scents = Scent.query.order_by(Scent.id).all()
    return render_template('shop.html', products = products, scents = scents, category = 'Candles')




@bp.route('/colognes')
def colognes():
    products = Product.query.filter_by(category='Cologne').order_by(Product.id).all()
    scents = Scent.query.order_by(Scent.id).all()
    return render_template('shop.html', products = products, scents = scents, category = 'Colognes')




@bp.route('/basket', methods=['POST', 'GET'])
def basket():
    product_id = request.values.get('product_id')

    # get an order if one is in progress
    if 'session_id' in session.keys():
        order = Order.query.get(session['session_id'])
    else:
        order = None

    print(order)
    # create new order if none present
    if order is None:
        order =Order(payment_status = False, date=datetime.now(), first_name='', last_name='', email='', phone='', address='', city='', state='', post_code='')
     
        db.session.add(order)
        db.session.commit()
        session['session_id'] = order.id

    
    # calcs total price 
    total_price = 0
    if order is not None:
        for product in order.products:
            total_price = total_price + product.price

    # checks for adding an item
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        print(product)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.basket'))
        else:
            flash('Item already in basket!')
            return redirect(url_for('main.basket'))

    
    return render_template('basket.html', order = order, total_price = total_price)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'session_id' in session:
        order = Order.query.get_or_404(session['session_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.basket'))
        except sqlalchemy.orm.exc.UnmappedInstanceError as e:
            return f'Problem deleting item from order: {str(e)}'
    return redirect(url_for('main.basket'))


@bp.route('/checkout')
def checkout():
    order = Order.query.get(session['session_id'])

    total_price = 0
    if order is not None:
        for product in order.products:
            total_price = total_price + product.price

    return render_template('checkout.html', total_price = total_price)




@bp.route('/product/<int:product_id>')
def product(product_id):

    selected_product = Product.query.filter_by(id=product_id).first()
    scent_notes = [selected_product.scent.scent_note1, selected_product.scent.scent_note2, selected_product.scent.scent_note3]

    products = Product.query.order_by(Product.id).all()

    product_usage_estimate = ''
    measure = ''

    if selected_product.category == "Candle":
        product_usage_estimate = 'APPROXIMATELY 80 HOUR BURN TIME'
        measure = 'g'
    else:
        product_usage_estimate = 'APPROXIMATELY 300 WEARS'
        measure = 'ml'

    related_products = []

    for product in products:
        if product.category == selected_product.category and product.id != selected_product.id:
            related_products.append(product)

    return render_template('product.html', selected_product = selected_product, related_products = related_products, product_usage_estimate = product_usage_estimate, measure = measure, scent_notes = scent_notes)

