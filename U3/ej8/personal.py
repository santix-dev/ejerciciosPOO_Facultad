from abc import ABC
class Personal(ABC):
	"""docstring for Personal"""
	def __init__(self,cuil,apellido,nombre,basico,antig):
		self._cuil = str(cuil)
		self._apellido = apellido.lower()
		self._nombre = nombre.lower()
		self._basico = float(basico)
		self._antig = int(antig)
	def __lt__(self,other):
		return self._apellido<other._apellido
	def nombre(self):
		return self._nombre
	def apellido(self):
		return self._apellido
	def basico(self):
		return self._basico
	def dni(self):
		return self._cuil[slice(2,-1)]
	def modificarBasico(self,nuevo):
		self._basico=nuevo
	def sueldo(self):
		return self._basico+self._basico*self._antig/100
