from apoyo import Apoyo
from docente import Docente
from docente_investigador import Doc_Inv
from investigador import Investigador
from nodo import Nodo
from personal import Personal
class ListaEnlazada():
	"""docstring for ListaEnlazada"""
	def __init__(self):
		self.__comienzo = None
		self.__actual = None
		self.__tope = 0
		self.__indice = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.__indice==self.__tope:
			self.__actual=self.__comienzo
			self.__indice=0
			raise StopIteration
		else:
			self.__indice+=1
			dato = self.__actual.personal()
			self.__actual=self.getSiguiente()
			return dato
	def agregarPersonal(self,personal):
		nodo=Nodo(personal)
		nodo.setSiguiente(self.__comienzo)
		self.__comienzo=nodo
		self.__actual=nodo
		self.__tope+=1
	def insertar(self,personal,posicion):
		i=-1
		nuevo=Nodo(personal)
		nodo=self.__comienzo
		anterior=None
		while nodo!=None and i<posicion:
			i+=1
			anterior=nodo
			nodo=nodo.getSiguiente()
		if anterior!=None:
			anterior.setSiguiente(nuevo)
			nuevo.setSiguiente(nodo)
			self.__tope+=1
		else:
			print("No existe esa posicion")
	def mostrarElemento(self,posicion):
		i=-1
		nodo=self.__comienzo
		while nodo!=None and i<posicion:
			i+=1
			nodo=nodo.getSiguiente()
		if nodo!=None:
			print(nodo.personal())
		else:
			print("No existe esa posicion")