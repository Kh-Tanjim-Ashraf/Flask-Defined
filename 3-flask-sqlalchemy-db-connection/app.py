from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import Boolean, func

app = Flask(__name__)

# Setup the base class for the model
class Base(DeclarativeBase):
    pass

# Include the DB connection configuration with relative path to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskManager.sqlite'

# Initialize the db by inheriting the base model, so that, SQLAlchemy can map & maintain the registry of database tables with the Python model classes.
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create a db model regarding a 'Task' table; Modern version of SQLAlchemy required Type Hinting.
class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(nullable=False)
    isCompleted: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)
    dateCreated: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

# Homepage Route
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Receive data from the frontend form
        newTask = request.form['task']
        
        # Create an object of `Task` model
        newTaskObj = Task(content=newTask)

        # Create a db session to insert the new task object in the DB; wrap with a try/except block
        try:
            db.session.add(newTaskObj)
            db.session.commit()
            return redirect('/')
        except:
            return "<h3>There is a problem inserting the new task</h3>"
    else:
        # Create the query to fetch the task records
        query = db.select(Task).order_by(Task.dateCreated.desc())
        # Execute the query
        tasks = db.session.scalars(query).all()
        # Pass the list of tasks into the template
        return render_template('index.html', tasks=tasks)

# Task Delete Route
@app.route('/delete/<int:id>/')
def taskDelete(id):
    # Check if a task exist with the id, otherwise return 404
    task = Task.query.get_or_404(id)

    # Detele the task
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "<h3>There is a problem deleting the task</h3>"

if __name__ == "__main__":
    app.run(debug=True)