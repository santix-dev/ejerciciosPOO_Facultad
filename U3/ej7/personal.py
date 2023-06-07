from abc import ABC
class Personal(ABC):
	"""docstring for Personal"""
	def __init__(self,cuil,apellido,nombre,basico,antig):
		self._cuil = cuil
		self._apellido = apellido
		self._nombre = nombre
		self._basico = basico
		self._antig = antig
		