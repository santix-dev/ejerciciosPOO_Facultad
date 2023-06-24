from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class Curso(db.Model):
	__tablename__="curso"
	id=db.Column(db.Integer,primary_key=True)
	anio=db.Column(db.Integer,nullable=False)
	division=db.Column(db.Integer,nullable=False)
	id_preceptor=db.Column(db.Integer,db.ForeignKey("preceptor.id"))	