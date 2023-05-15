import csv
from facultad import Facultad
from carrera import Carrera
class ManejadorFacultades(object):
	"""docstring for ManejadorFacultades"""
	def __init__(self):
		self.__lista = []
	def cargar(self, archivo="facultades.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=",")
		i=0
		for fila in reader:
			if int(fila[0])!=i:
				self.__lista.append(Facultad(fila[0],fila[1],fila[2],fila[3],fila[4]))
				i=int(fila[0])
			else:
				self.__lista[i-1].agregarCarrera(fila[1],fila[2],fila[3],fila[4],fila[5])
	def listar(self):
		for facultad in self.__lista:
			print(facultad)
			facultad.mostrarCarreras()
	def mostrarCarrerasFacultad(self,i):
		i-=1
		self.__lista[i].mostrarCarreras()
	def buscarCarrera(self,carrera):
		for facu in self.__lista:
			facu.buscarCarrera(carrera)

if __name__ == '__main__':
	mane=ManejadorFacultades()
	mane.cargar()
	mane.listar()