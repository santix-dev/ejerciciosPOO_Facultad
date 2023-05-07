import csv
from materia import MateriaAprobada
class ControladorMateria():
	def __init__(self):
		self.__lista = []
	def agregar(self,dni,nombre,fecha,nota,aprobacion):
		self.__lista.append(MateriaAprobada(dni,nombre,fecha,nota,aprobacion))
	def cargar(self,nomArch="materiasAprobadas.csv"):
		archivo=open(nomArch)
		reader=csv.reader(archivo,delimiter=";")
		for fila in reader:
			self.agregar(fila[0],fila[1],fila[2],fila[3],fila[4])

		