from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class Estudiante(db.Model):
	__tablename__="estudiante"
	id=db.Column(db.Integer,primary_key=True)
	nombre=db.Column(db.String(80),nullable=False)
	apellido=db.Column(db.String(80),nullable=False)
	dni=db.Column(db.String(8),unique=True,nullable=False)
	idcurso=db.Column(db.Integer,db.ForeignKey("curso.id"))
	idpadre=db.Column(db.Integer,db.ForeignKey("padre.id"))