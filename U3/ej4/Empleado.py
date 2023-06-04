class Empleado(object):
	"""docstring for Empleado"""
	def __init__(self, dni,nnom,direc,tel):
		self._dni = dni
		self._nnom = nnom
		self._direc = direc
		self._tel = tel
	def __str__(self):
		return f"DNI: {self._dni}\nNombre: {self._nnom}\nDomicilio: {self._direc}\nTel.: {self._tel}"
	def dni(self):
		return self._dni
	def nomDirDni(self):
		return f"{self._nom}\n{self._direc}\n{self._dni}"