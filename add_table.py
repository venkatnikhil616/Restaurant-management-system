from app import app, db, Table

def add_tables():
    with app.app_context():
        # Create some tables
        tables = [
            Table(number=1, is_occupied=False),
            Table(number=2, is_occupied=False),
            Table(number=3, is_occupied=False),
            Table(number=4, is_occupied=False),
            Table(number=5, is_occupied=False),
            Table(number=6, is_occupied=False),
            Table(number=7, is_occupied=False),
            Table(number=8, is_occupied=False),
            Table(number=9, is_occupied=False),
            Table(number=10, is_occupied=False)
        ]

        # Add all tables to the session and commit
        db.session.add_all(tables)
        db.session.commit()

        print('Tables added successfully!')

if __name__ == '__main__':
    add_tables()
