from flask import *
import hashlib
from datetime import date
import re

app=Flask(__name__)
app.config.from_pyfile("config.py")

from models import db
from models import Estudiante,Padre,Preceptor,Curso,Asistencia
# @app.route("/cambiar_fechas")
# def cambiar_contras():
# 	asists=db.session.query(Asistencia).all()
# 	for asis in asists:
# 		# return(asis.fecha)
# 		fecha=str(asis.fecha)
# 		fecha=fecha.replace("2023","2022")
# 		asis.fecha=fecha
# 		print(asis.fecha)
# 	db.session.commit()

@app.route("/")
def index():
	if not session.get("correo"):
		return redirect("/login")
	return render_template("index.html")


@app.route("/login",methods=["GET","POST"])
def login():
	if not (request.form.get("correo") and request.form.get("psw") and request.form.get("rol")):
		return render_template("login.html")
	rol=request.form.get("rol")
	mail=request.form.get("correo")
	if validar_email(mail):
		psw=cifrar(request.form.get("psw"))
		if valid_login(mail,psw,rol):
			session["rol"]=rol
			session["correo"]=mail
			session["id"]=(Preceptor.query.filter_by(correo=mail).first()).id
			return redirect("/")
		else:
			return render_template("login.html",mensaje="Datos no validos")
		# return render_template("login.html",mensaje="Datos no validos")
		
			
@app.route("/registrar_asistencia",methods=["POST","GET"])
def registrar_asistencia():
	cursos=db.session.query(Curso).filter(Curso.idpreceptor==session["id"]).all()
	return render_template("seleccionar_curso.html",cursos=cursos)

@app.route("/registrar_asistencia2",methods=["POST","GET"])
def registrar_asistencia2():
	curso=int(request.form.get("curso"))
	clase=int(request.form.get("clase"))
	ano,mes,dia=map(int,request.form.get("fecha").split("-"))
	fecha=date(ano,mes,dia)
	alumnos = db.session.query(Estudiante).filter(Estudiante.idcurso==curso).all()
	for alumno in alumnos:
		asis=Asistencia(fecha=fecha,codigoclase=clase,asistio="p",justificacion="",idestudiante=alumno.id)
		db.session.add(asis)
	db.session.commit()
	return registrar_asistencia3(curso)#alumno.nombre
	

# @app.route("/registrar_asistencia3",methods=["POST","GET"])
def registrar_asistencia3(curso):
	asist=db.session.query(Asistencia).join(Estudiante).filter(Asistencia.asistio=='p',Estudiante.idcurso==curso).first()
	# return asist.estudiante.nombre
	if asist!=None:
		return render_template("registrar_asistencia.html",registro=asist)
	return redirect("/")

@app.route("/cargar_asistencia",methods={"POST","GET"})
def cargar_asistencia():
	id=int(request.form.get("id"))
	asistio=request.form.get("asistencia")
	curso=request.form.get("curso")
	asist=db.session.query(Asistencia).filter(Asistencia.id==id).first()
	asist.asistio=asistio
	db.session.commit()
	if asistio=="n":
		return render_template("justificacion.html",asist=asist)
	return registrar_asistencia3(curso)
	
@app.route("/justificar",methods=["POST","GET"])
def justificar():
	id=request.form.get("id")
	jus=request.form.get("justif")
	curso=request.form.get("curso")
	asist=db.session.query(Asistencia).filter(Asistencia.id==id).first()
	asist.justificacion=jus
	db.session.commit()
	return registrar_asistencia3(curso)

@app.route("/seleccionar_curso")
def curso_informe():
	cursos=db.session.query(Curso).filter(Curso.idpreceptor==session["id"]).all()
	return render_template("seleccionar_curso_informe.html",cursos=cursos)
@app.route("/mostrar_informe",methods=["POST","GET"])
def mostrar_informe():
	curso=request.form.get("curso")
	asistencias=Asistencia.query.join(Estudiante).filter(Estudiante.idcurso==curso).order_by(Estudiante.nombre).all()
	return render_template("informe.html",asistencias=asistencias,type=type)





def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def valid_login(email,psw,rol):
	if rol=="preceptor":
		objeto=db.session.query(Preceptor).filter(Preceptor.correo==email).first()
	elif rol=="padre":
		objeto=db.session.query(Padre).filter(Padre.correo==email).first()
	if objeto!=None:
		return objeto.clave==psw
	else:
		return redirect("/login")

@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")

def cifrar(cadena):
	encoded_cadena = cadena.encode('utf-8')
	psw = hashlib.md5(encoded_cadena).hexdigest()
	return psw

@app.route("/iniciar_sesion",methods=["POST"])
def oeneoe():
	# user = Preceptor(nombre="John", apellido="Doe", correo="correo@example.com", clave="psw")
	# db.session.add(user)
	# db.session.commit()
	preceps=db.session.query(Preceptor).all()
	return render_template("preceptores.html",preceps=preceps)


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		print(date.today())
		print(app.config['SQLALCHEMY_DATABASE_URI'])
		app.run()