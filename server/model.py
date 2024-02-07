from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

# Initialize SQLAlchemy

db = SQLAlchemy()

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    piz_id = db.Column(db.Integer, Sequence ("piz_id_seq"), primary_key=True)
    piz_name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
     

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    res_id = db.Column(db.Integer, Sequence(res_id_seq, primary_key=True))
    res_name = db.Column(db.String(255), unique=True) 
    res_address = db.Column(db.String(255), nullable=False)



class Restaurant_Pizza(db.Model):
    __tablename__ = "respizza"

    respizza_id = db.Column(db.Integer, Sequence("respizza_id_seq", primary_key=True))    
    respizza_price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default= func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
