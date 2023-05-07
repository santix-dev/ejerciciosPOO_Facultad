class MateriaAprobada():
	def __init__(self, dni="",nombre="",fecha="",nota=0.0,aprobacion=""):
		self.__dni = dni
		self.__materia = nombre.lower()
		self.__fecha = fecha
		self.__nota = float(nota)
		self.__aprobacion = aprobacion #E: examen, P: promocion, X: equivalencia
	def dni(self):
		return self.__dni
	def nota(self):
		return self.__nota
	def materia(self):
		return self.__materia
	def fecha(self):
		return self.__fecha
	def anio(self):
		return self.__anio
	def verifMateria(self,materia):
		flag=False
		if materia==self.__materia:
			flag=True

	def __str__(self):
		return f"{self.__dni} {self.__materia} {self.__nota} {self.__aprobacion}"
		