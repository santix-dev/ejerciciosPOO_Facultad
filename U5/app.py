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
			return redirect("/") #f"Bienvenido {session['correo']} {session['rol']}"
		else:
			return redirect("/login")
			
@app.route("/registrar_asistencia",methods=["POST","GET"])
def registrar_asistencia():
	# if not (request.form.get("curso") and request.form.get("clase")) or request.args.get("etapa")==1:# or request.form.get("clase"):
	cursos=db.session.query(Curso).all()
	return render_template("seleccionar_curso.html",cursos=cursos)
	# elif request.form.get("etapa")==2:
	# 	print(request.args.get("band"))
	# 	curso=request.form.get("curso")
	# 	clase=request.form.get("clase")
	# 	fecha=date.today()
	# 	alumnos = db.session.query(Estudiante).filter(Estudiante.idcurso==curso).all()
	# 	for alumno in alumnos:
	# 		asis=Asistencia(fecha=fecha,codigoclase=clase,asistio="p",justificacion="",idestudiante=alumno.id)
	# 	db.session.commit()
	# 	return redirect("/registrar_asistencia?etapa=3")
	# elif request.args.get("etapa")==3:
	# 	print("y muy Hasta aca tambien")
	# 	asists=db.session.query(Asistencia).filter(Asistencia.asistio=='p').all()
	# 	if asists:
	# 		return render_template("registrar_asistencia.html",registros=asists)
	# 	else:
	# 		return redirect("/")
	# return redirect("/")

@app.route("/registrar_asistencia3",methods=["POST","GET"])
def registrar_asistencia3():
	asists=db.session.query(Asistencia).filter(Asistencia.asistio=='p').all()
	# for asisti in asists:
	# 	return asisti.fecha
	# return "HOLA"
	if asists!=None:
		return render_template("registrar_asistencia.html",registros=asists)
	return redirect("/")	



@app.route("/registrar_asistencia2",methods=["POST","GET"])
def registrar_asistencia2():
	curso=int(request.form.get("curso"))
	clase=int(request.form.get("clase"))
	fecha=date.today()
	alumnos = db.session.query(Estudiante).filter(Estudiante.idcurso==curso).all()
	for alumno in alumnos:
		asis=Asistencia(fecha=fecha,codigoclase=clase,asistio="p",justificacion="",idestudiante=alumno.id)
		db.session.add(asis)
	db.session.commit()
	return redirect("/registrar_asistencia3")

@app.route("/cargar_asistencia",methods={"POST","GET"})
def cargar_asistencia():
	# return str(request.args.get("alu"))
	id_alu=int(request.args.get("alu"))
	# return str(id_alu)
	asist=db.session.query(Asistencia).filter(Asistencia.asistio=="p",Asistencia.idestudiante==id_alu).first()
	asist.asistio=request.args.get("v")
	db.session.commit()
	if request.args.get("v")=="n":
		return render_template("justificacion.html",id_asis=asist.id)
	return redirect("/registrar_asistencia3")
	
@app.route("/justificar",methods=["POST","GET"])
def justificar():
	id=request.form.get("id")
	jus=request.form.get("justif")
	asist=db.session.query(Asistencia).filter(Asistencia.id==id).first()
	asist.justificacion=jus
	db.session.commit()
	return redirect("/registrar_asistencia3")

@app.route("/informe")
def informe():
	pass





def find_class(correo):
	try:
		objeto=db.session.query(Preceptor).filter(Preceptor.correo==correo).first()
	except:
		objeto=db.session.query(Padre).filter(Padre.correo==correo).first()
	return objeto.__class__.__tablename__


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