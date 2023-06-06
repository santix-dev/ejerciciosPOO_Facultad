import json
from vehiculo import Vehiculo
from datetime import date

class Usado(Vehiculo):
	"""docstring for Usado"""
	def __init__(self, patente,ano,km,marca,modelo,puertas,color,precio_base):
		super().__init__(modelo,puertas,color,precio_base)
		self.__marca = marca
		self.__patente = patente
		self.__ano = ano
		self.__km = km
	def importeVenta(self):
		fechaAct=date.today().year
		antiguedad=(fechaAct-self.__ano)/100
		importe=self._precio_base-self._precio_base*antiguedad if self.__km<100000 else self._precio_base-self._precio_base*antiguedad-self._precio_base*0.02		
		return importe
	def modificarPrecio(self,precio):
		self._precio_base=precio
	def mod_pr_puertas(self):
		print(f"{self.mod_puertas()},importe: {self.importeVenta()}")
	def toJSON(self):
		d = {
			"__class__":self.__class__.__name__,
			"__atributos__":
			{
				"patente":self.__patente,
				"ano":self.__ano,
				"km":self.__km,
				"marca":self.__marca,
				"modelo":self._modelo,
				"puertas":self._puertas,
				"color":self._color,
				"precio_base":self._precio_base
			}

		}
		return d
