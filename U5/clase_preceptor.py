from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class Preceptor(db.Model):
	__tablename__="preceptor"
	id=db.Column(db.Integer,primary_key=True)
	nombre=db.Column(db.String(80),nullable=False)
	apellido=db.Column(db.String(80),nullable=False)
	correo=db.Column(db.String(40),unique=True,nullable=False)
	clave=db.Column(db.String(40),unique=True,nullable=False)