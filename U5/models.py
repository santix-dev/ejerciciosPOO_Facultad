from __main__ import app
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
	estudiante=db.relationship("Estudiante",backref="Asistencia")

class Curso(db.Model):
	__tablename__="curso"
	id=db.Column(db.Integer,primary_key=True)
	anio=db.Column(db.Integer,nullable=False)
	division=db.Column(db.Integer,nullable=False)
	idpreceptor=db.Column(db.Integer,db.ForeignKey("preceptor.id"))

class Padre(db.Model):
	__tablename__="padre"
	id=db.Column(db.Integer,primary_key=True)
	nombre=db.Column(db.String(80),nullable=False)
	apellido=db.Column(db.String(80),nullable=False)
	correo=db.Column(db.String(40),unique=True,nullable=False)
	clave=db.Column(db.String(40),unique=True,nullable=False)

class Preceptor(db.Model):
	__tablename__="preceptor"
	id=db.Column(db.Integer,primary_key=True)
	nombre=db.Column(db.String(80),nullable=False)
	apellido=db.Column(db.String(80),nullable=False)
	correo=db.Column(db.String(40),unique=True,nullable=False)
	clave=db.Column(db.String(40),nullable=False)
	def __str__(self):
		return f"{self.todict()}"
	def todict(self):
		return {
			"id":self.id,
			"nombre":self.nombre,
			"apellido":self.apellido,
			"correo":self.correo
		}

class Estudiante(db.Model):
	__tablename__="estudiante"
	id=db.Column(db.Integer,primary_key=True)
	nombre=db.Column(db.String(80),nullable=False)
	apellido=db.Column(db.String(80),nullable=False)
	dni=db.Column(db.String(8),unique=True,nullable=False)
	idcurso=db.Column(db.Integer,db.ForeignKey("curso.id"))
	idpadre=db.Column(db.Integer,db.ForeignKey("padre.id"))