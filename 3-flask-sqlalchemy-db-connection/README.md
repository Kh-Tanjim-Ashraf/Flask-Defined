# Flask App - DB Connection utilizing SQLAlchemy

This is a simple Flask application demonstrating how to integrate an SQLite database into a Flask server.

## How to Setup

1. Create a Python virtual environment.
   > python -m venv env
2. Activate the virtual environment (_using Bash terminal_).
   > source env/Scripts/activate
3. Install the required dependecies of the project using the `pip` command.
   > pip install -r requirements.txt
4. Initialized the SQLite database from the database models defined inside the Flask project by utilizing the SQLAlchemy ORM. A file named `db_migration.py` file exist in the directory for this purpose. Execute the python script.
   > python db_migration.py
5. Spin up the Flask server.
   > python app.py

<small>Note: Since it's running on a development server, we can access the web server at http://localhost:5000 from the browser.</small>
