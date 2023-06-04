from Empleado import Empleado
class EmpPlanta(Empleado):
	"""docstring for EmpPlanta"""
	def __init__(self, basico,ant,dni,nnom,direc,tel):
		super().__init__(dni,nnom,direc,tel)
		self.__basico = basico
		self.__ant = ant
	def __str__(self):
		return f"{super().__str__()}\nBasico: {self.__basico}\nAntiguedad: {self.__ant}"
	def sueldo(self):
		return self.__basico+self.__ant*self.__basico*0.01