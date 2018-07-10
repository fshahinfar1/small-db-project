from flask import Flask, render_template, request, redirect, url_for
import sys
import data as D
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
def index():
    products = D.get_products()
    authors = D.get_authors()
    data = {
    'products': products,
    'authors': authors
    }
    return render_template('index.html', **data)

@app.route('/loginsignup', methods=['GET', 'POST'])
def login_signup():
    if request.method == 'GET':
        return render_template('login_signup.html')
    elif request.method == 'POST':
        data = request.form
        try:
            D.insert_customer(data)
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            return redirect(url_for('login_signup'))

@app.route('/product', methods=['GET', 'POST'])
def register_product():
    if request.method == 'GET':
        return render_template('register_product.html')
    elif request.method == 'POST':
        data = request.form
        try:
            D.insert_product(data)
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            return redirect(url_for('register_product'))


@app.route('/order', methods=['GET', 'POST'])
def register_order():
    if request.method == 'GET':
        data = {
        'products': D.get_products(),
        }
        return render_template('register_order.html', **data)
    elif request.method == 'POST':
        data = request.form
        print(data, sys.stdout)
        try:
            for i in data:
                print(i, data[i])
            for item in data['selected_item']:
                print(item, '*')
            # D.insert_order(data)
            # D.insert_order_product_relation(data)
            return redirect(url_for('index'))
        except Exception as e:
            print(e, sys.stderr)
            return redirect(url_for('register_order'))
