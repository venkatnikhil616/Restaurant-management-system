from app import app, db, MenuItem

def add_menu_items():
    with app.app_context():
        # Create some menu items
        items = [
            MenuItem(name='Burger', description='Juicy beef burger', price=5.99, available=True),
            MenuItem(name='Pizza', description='Cheesy pizza with toppings', price=8.99, available=True),
            MenuItem(name='Pasta', description='Creamy Alfredo pasta', price=7.99, available=True),
            MenuItem(name='Salad', description='Fresh garden salad', price=4.99, available=True),
            MenuItem(name='Soda', description='Chilled carbonated drink', price=1.99, available=True),
            MenuItem(name='Coffee', description='Hot brewed coffee', price=2.49, available=True),
            MenuItem(name='Tea', description='Refreshing iced tea', price=2.49, available=True),
            MenuItem(name='Steak', description='Grilled sirloin steak', price=12.99, available=True),
            MenuItem(name='Fries', description='Crispy golden fries', price=3.99, available=True),
            MenuItem(name='Soup', description='Hearty vegetable soup', price=5.49, available=True),
            MenuItem(name='Cake', description='Chocolate fudge cake', price=4.99, available=True),
            MenuItem(name='Ice Cream', description='Vanilla ice cream', price=3.49, available=True),
            MenuItem(name='Smoothie', description='Fruit smoothie', price=5.99, available=True),
            MenuItem(name='Wrap', description='Chicken wrap with veggies', price=6.99, available=True),
            MenuItem(name='Burger Combo', description='Burger with fries and soda', price=8.99, available=True),
            MenuItem(name='Pizza Combo', description='Pizza with salad and drink', price=10.99, available=True),
        ]

        # Add all menu items to the session and commit
        db.session.add_all(items)
        db.session.commit()

        print('Menu items added successfully!')

if __name__ == '__main__':
    add_menu_items()
