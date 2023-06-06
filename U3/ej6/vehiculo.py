from abc import ABC
class Vehiculo(ABC):
	"""docstring for Vehiculo"""
	def __init__(self, modelo,puertas,color,precio_base):
		self._modelo = modelo
		self._puertas = puertas
		self._color = color
		self._precio_base = precio_base	
	def mod_puertas(self):
		print(f"modelo: {self._modelo} {self._puertas} puertas")