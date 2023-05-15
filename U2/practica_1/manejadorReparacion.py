import csv
from reparacion import Reparacion
class ManejadorReparacion(object):
	def __init__(self):
		self.__lista = []
	def cargar(self,file="reparaciones.csv"):
		archivo=open(file)
		reader=csv.reader(archivo,delimiter=";")
		for fila in reader:
			self.agregar(fila[0],fila[1],fila[2],fila[3],fila[4])
	def agregar(self,pat="",repar="",prRep="",prManO="",est=""):
		self.__lista.append(Reparacion(pat,repar,prRep,prManO,est))
	def mostrarReparacionesXPatente(self,pat):
		print("""Reparación		precio repuesto		mano de obra 		subtotal""")
		total=0.0
		for rep in self.__lista:
			if rep.patente()==pat:
				subt=rep.subtotal()
				total+=subt
				print(rep)
		print(f""" 										  total a pagar: {total}""")
	def reparacionesTerminadas(self,pat):
		term=0
		reparaciones=0
		for rep in self.__lista:
			if rep.patente()==pat:
				reparaciones+=1
				if rep.estado()=="T":
					term+=1
		if term==reparaciones:
			flag=True
		else:
			flag=False
		return flag
	def mostrarTotal(self,pat):
		total=0
		for rep in self.__lista:
			if rep.patente()==pat:
				total+=rep.subtotal()
		print(f"Total a pagar: {total}")
	def mostrarReparacionesPendientesXPatente(self,pat):
		for rep in self.__lista:
			if rep.patente()==pat and rep.estado()=="P":
				print(rep.info())
