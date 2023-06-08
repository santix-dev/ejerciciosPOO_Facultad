from zope.interface import implementer
from nodo import Nodo
from vehiculo import Vehiculo
from interfaz import InterfazLista
from ObjectEncoder import ObjectEncoder

@implementer(InterfazLista)
class Lista():
	"""docstring for Lista"""
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
			dato = self.__actual.vehiculo()
			self.__actual=self.getSiguiente()
			return dato
	def cargar(self):
		encoder=ObjectEncoder()
		self=encoder.decodificarDiccionario(encoder.leerJSONArchivo("vehiculos.json"))
	def agregar(self,vehiculo):
		nodo=Nodo(vehiculo)
		nodo.setSiguiente(self.__comienzo)
		self.__comienzo=nodo
		self.__actual=nodo
		self.__tope+=1
	def insertar(self,vehiculo,posicion):
		i=-1
		nuevo=Nodo(vehiculo)
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
			print(nodo.vehiculo())
		else:
			print("No existe esa posicion")
	def mostrarClaseElemento(self,posicion):
		i=-1
		nodo=self.__comienzo
		while nodo!=None and i<posicion:
			i+=1
			nodo=nodo.getSiguiente()
		if nodo!=None:
			print("el elemento es de tipo: ",type(nodo.vehiculo()))
		else:
			print("No existe esa posicion")
	def modificarPrecioUsado(self,patente):
		nodo=self.__comienzo
		while nodo!=None and nodo.vehiculo().patente()!=patente:
			nodo=nodo.getSiguiente()
		if nodo!=None:
			precio=int(input("Ingrese precio: "))
			nodo.modificarPrecio(precio)
			print(nodo.vehiculo().importeVenta())
	def vehiculoMasBarato(self):
		aux=self.__comienzo
		menor=aux
		precio=menor.vehiculo().importeVenta()
		while aux!=None:
			if aux.vehiculo().importeVenta()<precio:
				menor=aux
				precio=menor.vehiculo().importeVenta()
			aux=aux.getSiguiente()
		print(menor.vehiculo(),precio)
	def todos_modelo_precio_puertas(self):
		aux=self.__comienzo
		while aux!=None:
			print(aux.vehiculo().mod_pr_puertas())
	def toJSON(self):
		d={
			"__class__":self.__class__.__name__,
			"vehiculos":[nodo.toJSON() for nodo in self]
		}
	def leerVehiculo(self):
		print("1) Nuevo\n2) Usado")
		opc=int(input())
		if opc==1:
			vers=input("Version: ")
			mod=input("modelo: ")
			puer=input("puertas: ")
			col=input("color : ")
			prec=input("Precio base: ")
			vehiculo=Nuevo(vers,mod,puer,col,prec)
		elif opc==2:
			pat=input("patente: ")
			ano=input("anio: ")
			km=input("km: ")
			marca=input("marca : ")
			mod=input("modelo: ")
			puer=input("puertas: ")
			col=input("color : ")
			prec=input("Precio base: ")
			vehiculo=Usado(pat,ano,km,marca,mod,puer,col,prec)
		return vehiculo
