import csv
from sabor import Sabor
class ManejadorSabores(object):
	"""docstring for ManejadorSabores"""
	def __init__(self):
		self.__lista = []
	def cargar(self,archivo="sabores.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=";")
		next(reader)
		for fila in reader:
			self.__lista.append(Sabor(fila[0],fila[1],fila[2]))
	def mostrarSabores(self):
		for sabor in self.__lista:
			print(sabor)
	def sabor(self,i):
		return self.__lista[i-1]
	def test(self):
		self.cargar()
		self.mostrarSabores()
	def verifSabor(self,indice):
		if self.sabor(indice) not in self.__lista:
			indice=int(input("Codigo erroneo, ingrese sabor"))
			indice=self.verifSabor()
		return indice
	def len(self):
		return len(self.__lista)

if __name__ == '__main__':
	man=ManejadorSabores()
	man.test()
