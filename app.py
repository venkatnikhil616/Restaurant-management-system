from flask import Flask, redirect, render_template, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize Database object
db = SQLAlchemy(app)

# --- Database Models ---

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    orders = db.relationship('Order', backref='user', lazy=True)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    is_occupied = db.Column(db.Boolean, default=False)
    reservations = db.relationship('Reservation', backref='table', lazy=True)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(50), nullable=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    customer_name = db.Column(db.String(150), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        table_number = request.form.get('table_number')
        menu_item_id = request.form.get('menu_item')
        quantity = request.form.get('quantity')

        table = Table.query.filter_by(number=table_number).first()
        menu_item = MenuItem.query.get(menu_item_id)

        if table and menu_item:
            total = menu_item.price * int(quantity)
            # Assuming user_id=1 for simplicity
            new_order = Order(user_id=1, table_id=table.id, total=total)
            db.session.add(new_order)
            db.session.commit()

            order_item = OrderItem(order_id=new_order.id, menu_item_id=menu_item.id, quantity=quantity)
            db.session.add(order_item)
            db.session.commit()

            flash('Order placed successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Table or Menu Item not found!', 'danger')

    menu_items = MenuItem.query.all()
    return render_template('order.html', menu_items=menu_items)

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        table_number = request.form.get('table_number')
        customer_name = request.form.get('customer_name')
        reservation_time = request.form.get('reservation_time')

        table = Table.query.filter_by(number=table_number).first()

        if table and not table.is_occupied:
            res_time = datetime.strptime(reservation_time, '%Y-%m-%dT%H:%M')
            new_reservation = Reservation(table_id=table.id, customer_name=customer_name, reservation_time=res_time)
            db.session.add(new_reservation)
            table.is_occupied = True
            db.session.commit()

            flash('Reservation made successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Table is not available or not found!', 'danger')

    tables = Table.query.filter_by(is_occupied=False).all()
    return render_template('reservation.html', tables=tables)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        unit = request.form.get('unit')

        new_item = InventoryItem(name=name, quantity=quantity, unit=unit)
        db.session.add(new_item)
        db.session.commit()

        flash('Inventory item added successfully!', 'success')
        return redirect(url_for('inventory'))

    items = InventoryItem.query.all()
    return render_template('inventory.html', items=items)

@app.route('/report')
def report():
    orders = Order.query.all()
    reservations = Reservation.query.all()
    return render_template('report.html', orders=orders, reservations=reservations)

if __name__ == '__main__':
    # You might need to create the database tables first:
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
