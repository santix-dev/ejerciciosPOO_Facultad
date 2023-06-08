from apoyo import Apoyo
from docente import Docente
from docente_investigador import Doc_Inv
from investigador import Investigador
from nodo import Nodo
from personal import Personal
from interfaz import InterfazLista
from zope.interface import implementer
@implementer(InterfazLista)
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
			self.__actual=self.__actual.getSiguiente()
			return dato
	def __getitem__(self,indice):
		if indice < 0:
			raise IndexError("Index out of range")
		actual = self.__comienzo
		for _ in range(indice):
			if actual is None:
				raise IndexError("Index out of range")
			actual = actual.getSiguiente()
		return actual.personal()
	def agregar(self,personal):
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
			return nodo.personal()
		else:
			print("No existe esa posicion")
	def toJSON(self):
		personal=[]
		for persona in self:
			personal.append(persona.toJSON())
		print(personal)
		d={
			"__class__":self.__class__.__name__,
			"personal":personal
		}
		return d
	def ordenarXapellido(self):
		lista=[persona for persona in self]
		lista.sort()
		for persona in lista:
			print(f"Nombre {persona.nombre()},Apellido: {persona.apellido()} tipo: {persona.clase()}, sueldo: {persona.basico()}")			
	# 	i=0
	# 	band_cambio=True
	# 	nodo=self.__comienzo
	# 	nodo_sig=self.__comienzo.getSiguiente()
	# 	while i<self.__tope and band_cambio:
	# 		# Bandera para indicar si se realizó algún intercambio en la pasada actual
	# 		band_cambio = False
	# 		# Iterar de 0 a n-i-1, ya que los últimos i elementos ya están ordenados
	# 		for j in range(0, self.__tope - i - 1):
	#         	# Comparar elementos adyacentes y realizar intercambio si el primero es mayor que el segundo
	# 			if self[j] > self[j + 1]:
	# 				self[j], self[j + 1] = self[j + 1], self[j]
	# 				band_cambio = True
	# 		i+=1
	# def ordenar2(self):
	# 	nodo=self.__comienzo
	# 	i=0
	# 	cabeza=True
	# 	while nodo!=None:
	# 		if cabeza:
	# 			if nodo.getSiguiente().personal()>nodo.personal():
	# 				self.__comienzo=nodo.getSiguiente()
	# 				nodo.setSiguiente(nodo.getSiguiente)

	# 		i+=1