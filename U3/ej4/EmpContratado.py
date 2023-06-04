from Empleado import Empleado
class EmpContratado(Empleado):
	"""docstring for EmpContratado"""
	__valor_h = 30
	def __init__(self, fecha_i,fecha_f,,horas,dni,nnom,direc,tel):
		super().__init__(dni,nnom,direc,tel)
		self.__fecha_i = fecha_i
		self.__fecha_f = fecha_f
		self.__horas = horas
	def __str__(self):
		return f"{super().__str__()}\nfecha_i: {self.__fecha_i}\nfecha_f: {self.__fecha_f}"
	def sueldo(self):
		return self.__valor_h*self.__horas
	def registrarHoras(self,horas):
		self.__horas+=horas