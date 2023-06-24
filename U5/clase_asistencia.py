from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class Asistencia(db.Model):
	__tablename__="asistencia"
	id=db.Column(db.Integer,primary_key=True)
	fecha=db.Column(db.Date,nullable=False)
	codigoclase=db.Column(db.Integer,nullable=False)
	asistio=db.Column(db.String(1),nullable=False)
	justificacion=db.Column(db.String(30),nullable=False)
	idestudiante=db.Column(db.Integer,db.ForeignKey("estudiante.id"))