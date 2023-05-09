import csv
from cliente import Cliente
class ManejadorCliente(object):
	def __init__(self):
		self.__lista = []
	def cargar(self,file="clientes.csv"):
		archivo=open(file)
		reader=csv.reader(archivo,delimiter=";")
		for fila in reader:
			self.agregar(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
	def agregar(self,dni="",ape="",nom="",tel="",pat="",vehic="",est=""):
		self.__lista.append(Cliente(dni,ape,nom,tel,pat,vehic,est))
	def indiceCliente(self,dni):
		dni=str(dni)
		i=0
		flag=False
		while not flag and i<len(self.__lista):
			if self.__lista[i].verifDNI(dni):
				flag=True
			i+=1
		if flag:
			i-=1
		else:
			i=False
		return i
	def mostrarCliente(self,i):
		print(self.__lista[i])
	def patenteCliente(self,i):
		return self.__lista[i].patente()
	def cambiarEstadoT(self,pat):
		flag=False
		i=0
		while not flag and i<len(self.__lista):
			if self.__lista[i].patente()==pat:
				flag=True
			else:
				i+=1
		self.__lista[i].estadoTerminado()
		self.__lista[i].mostrarDatosParaPagar()
	def mostrarDatosConPatente(self,pat):
		self.mostrarDatosConIndice(i)
	def pendientes(self,listaRep):
		for cli in self.__lista:
			if cli.estado()!="T" and not listaRep.reparacionesTerminadas(cli.patente()):
				cli.datosCliPendiente()
				listaRep.mostrarReparacionesPendientesXPatente(cli.patente())
	def clientesConMasDeUnCarro(self):
		lista=[]
		for i in range(len(self.__lista)):
			for j in range(i+1,len(self.__lista)):
				if self.__lista[i]==self.__lista[j]:
					if not self.__lista[i] in lista:
						lista.append(self.__lista[i])
		for i in lista:
			print(i)




