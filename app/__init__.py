# so this __init__ file is where we set up all stuff flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#python dotenv specifies to import the package like this:
from dotenv import load_dotenv

#built in module provides a way to read environment variables
import os

# db and migrate are variables that give access to database operations
db = SQLAlchemy()
migrate = Migrate()

#this method will load the values in our env file so os module can see them
load_dotenv()
def create_app(test_config = None):
    app = Flask(__name__)
    if not test_config:

    #to hide a warning about a feature in SQLALCHEMY we wont be using
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #this sets up the connection to the connection string for our database
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        
    # connects db and migrate to our flask app, using the package's recommended syntax
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    from app.models.book import Book
    from app.models.author import Author
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    from .author_routes import authors_bp
    app.register_blueprint(authors_bp)
    
    from .book_routes import books_bp
    app.register_blueprint(books_bp)
    #this import cant go to the top or else we will get a circular import error
    return app