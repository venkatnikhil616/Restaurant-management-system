Restaurant Management System
This project is a comprehensive Restaurant Management System developed using the Flask web framework. It demonstrates proficiency in Python backend development, database management with SQLAlchemy, and responsive frontend design using Bootstrap.
🚀 Features
Dynamic Menu Management: Add and organize menu items efficiently.
Table Tracking: Manage restaurant seating and availability.
Responsive UI: A clean, mobile-friendly interface built with HTML5, CSS3, and Bootstrap.
Database Integration: Utilizes SQLAlchemy ORM for robust data persistence and management.
🛠️ Tech Stack
Backend: Python, Flask
Database: SQLite, SQLAlchemy (ORM)
Frontend: HTML5, CSS3, Bootstrap
💻 Getting Started
Follow these steps to set up the project locally on your machine.
1.Clone the Repository
git clone https://github.com/venkatnikhil616/Restaurant-management-system.git

2.cd Restaurant-Management-System

3. Set Up Virtual Environment
Creating a virtual environment keeps your project dependencies isolated.
# Create the environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt --break-system-packages

4. Run the Application
python app.py
Once the server is running, open your browser and navigate to: http://127.0.0.1:5000

📊 Database Management
The system uses SQLite for data storage. To inspect the database contents:
Locate the .db file (usually in the instance/ folder).
Go to the SQLite Online Viewer.
Drag and drop the database file into the browser to view tables and entries.
📂 Project Structure
├── app.py              # Main application entry point
├── database.py         # Database configurations and models
├── add_table.py        # Script to manage table data
├── add_meun_itrem.py   # Script to manage menu data
├── templates/          # HTML files
├── static/             # CSS, JS, and Images
└── requirements.txt    # List of required Python packages
📬 Contact & Feedback
Feel free to explore the repository! If you have any questions or feedback, please reach out via the contact form on the website or open an issue in this repository.
