from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def post_orders():
    name_r = request.form['name_give']
    count_r = request.form['count_give']
    address_r = request.form['address_give']
    phone_r = request.form['phone_give']

    order = {
        'name': name_r,
        'count': count_r,
        'address': address_r,
        'phone': phone_r
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success'})

@app.route('/order', methods=['GET'])
def get_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)