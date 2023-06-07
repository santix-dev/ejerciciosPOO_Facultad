from lista import ListaEnlazada
from apoyo import Apoyo
from docente import Docente
from docente_investigador import Doc_Inv
from investigador import Investigador
from ObjectEncoder import ObjectEncoder
class ManejadorPersonal():
	"""docstring for ManejadorPersonal"""
	def __init__(self):
		self.__lista = ListaEnlazada()
	def cargar(self):
		decoder=ObjectEncoder()
		d=decoder.leerJSONArchivo()
		self.__lista=decoder.decodificarDiccionario(d)
	def agregarAgente(self):
		print("1)Docente\n2)Investigador\n3)Apoyo\n4)Docente investigador")
		t=int(input("Ingrese tipo agente: "))
		if t<1 or t>4:
			print("tipo no valido")
			return
		cuil=input("cuil: ")
		apellido=input("apellido: ")
		nombre=input("nombre: ")
		basico=input("basico: ")
		antig=input("antig: ")
		if t==1:
			carrera=input("carrera: ")
			cargo=input("cargo: ")
			catedra=input("catedra: ")
			persona=Docente(carrera,cargo,catedra,cuil,apellido,nombre,basico,antig)
		elif t==2:
			area=input("area: ")
			tipo=input("tipo: ")
			persona=Investigador(area,tipo,cuil,apellido,nombre,basico,antig)
		elif t==3:
			categoria=input("categoria: ")
			persona=Apoyo(categoria,cuil,apellido,nombre,basico,antig)
		elif t==4:
			categoria=input("categoria: ")
			plus=input("plus: ")
			carrera=input("carrera: ")
			cargo=input("cargo: ")
			catedra=input("catedra: ")
			area=input("area: ")
			tipo=input("tipo: ")
			persona=Doc_Inv(categoria,plus,carrera,cargo,catedra,area,tipo,cuil,apellido,nombre,basico,antig)
		self.__lista.agregar(persona)
	def insertarAgente(self):
		print("1)Docente\n2)Investigador\n3)Apoyo\n4)Docente investigador")
		t=int(input("Ingrese tipo agente: "))
		p=int(input("Ingrese posicion: "))
		if t<1 or t>4:
			print("tipo no valido")
			return
		cuil=input("cuil: ")
		apellido=input("apellido: ")
		nombre=input("nombre: ")
		basico=input("basico: ")
		antig=input("antig: ")
		if t==1:
			carrera=input("carrera: ")
			cargo=input("cargo: ")
			catedra=input("catedra: ")
			persona=Docente(carrera,cargo,catedra,cuil,apellido,nombre,basico,antig)
		elif t==2:
			area=input("area: ")
			tipo=input("tipo: ")
			persona=Investigador(area,tipo,cuil,apellido,nombre,basico,antig)
		elif t==3:
			categoria=input("categoria: ")
			persona=Apoyo(categoria,cuil,apellido,nombre,basico,antig)
		elif t==4:
			categoria=input("categoria: ")
			plus=input("plus: ")
			carrera=input("carrera: ")
			cargo=input("cargo: ")
			catedra=input("catedra: ")
			area=input("area: ")
			tipo=input("tipo: ")
			persona=Doc_Inv(categoria,plus,carrera,cargo,catedra,area,tipo,cuil,apellido,nombre,basico,antig)
		self.__lista.insertar(persona,p)
	def guardarDatos(self):
		d=self.__lista.toJSON()
		encoder=ObjectEncoder()
		encoder.guardarJSONArchivo(d)
