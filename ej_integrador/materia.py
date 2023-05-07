class MateriaAprobada():
	def __init__(self, dni="",nombre="",fecha="",nota=0.0,aprobacion=""):
		self.__dni = dni
		self.__nombreMat = nombre
		self.__fecha = fecha
		self.__nota = float(nota)
		self.__aprobacion = aprobacion #E: examen, P: promocion, X: equivalencia

		