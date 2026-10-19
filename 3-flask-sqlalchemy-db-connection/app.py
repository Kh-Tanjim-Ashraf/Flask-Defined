from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import Boolean, func

app = Flask(__name__)

# Setup the base class for the model
class Base(DeclarativeBase):
    pass

# Include the DB connection configuration with relative path to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskManager_1.sqlite'

# Initialize the db by inheriting the base model, so that, SQLAlchemy can map & maintain the registry of database tables with the Python model classes.
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create a db model regarding a 'Task' table; Modern version of SQLAlchemy required Type Hinting.
class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(nullable=False)
    isCompleted: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)
    dateCreated: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

if __name__ == "__main__":
    app.run(debug=True)