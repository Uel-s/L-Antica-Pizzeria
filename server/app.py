from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
#from model import 

# Create a Flask application instance
app = Flask(__name__)

# Configure the database URI for SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizzeria.db"

# Disable modification tracking for SQLAlchemy (not recommended in production)

app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

#Initialize Flask-Migrate

migrate = Migrate(app, db)
db.init_app(app)

#Initialize Flask-RESTful

api = Api(app)

################################################################

# Run the Flask app

if __name__ == "__main__":
    app.run(port=5555, debug = True)