from personal import Personal
class Docente(Personal):
	"""docstring for Docente"""
	def __init__(self,carrera,cargo,catedra,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self._carrera = carrera
		self._cargo = cargo
		self._catedra = catedra
		