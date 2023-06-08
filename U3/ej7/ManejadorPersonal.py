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
	def mostrarClase(self,pos):
		print(f"el personal en la {pos} posicion es de tipo: {type(self.__lista.mostrarElemento(pos))}")
	def listadoXnombreYcarrera(self,carrera):
		lista_aux=[]
		for persona in self.__lista:
			if isinstance(persona,Doc_Inv):
				lista_aux.append(persona)
		lista_aux.sort()
		for doc in lista_aux:
			print(doc)
	def contar_docInv_Inv(self,area):
		inv=0
		doc_inv=0
		for persona in self.__lista:
			if isinstance(persona,Doc_Inv) and persona.area()==area:
				doc_inv+=1
			elif isinstance(persona,Investigador) and persona.area()==area:
				inv+=1
		print(f"En este area trabajan: {inv} investigadores y {doc_inv} docentes-investigadores")
	def listadoXapellido(self):
		self.__lista.ordenarXapellido()
	def listadoXcategoria(self,cat):
		total=0
		for persona in self.__lista:
			if isinstance(persona,Doc_Inv) and persona.categoria()==cat:
				print(persona.nombre(),persona.apellido(),persona.plus())
				total+=persona.plus()
		print("total a solicitar al ministerio para pagar extras a docentes investigadores: ",total)
