from datetime import date 
from Empleado import Empleado

class EmpExterno(Empleado):
	"""docstring for EmpExterno"""
	self.__valor_h = 30
	def __init__(self, tarea,fecha_i,fecha_f,mViatico,mSVida,costObra,dni,nnom,direc,tel):
		super().__init__(dni,nnom,direc,tel)
		self.__tarea = tarea
		self.__fecha_i = fecha_i
		self.__fecha_f = fecha_f
		self.__mViatico = mViatico
		self.__mSVida = mSVida
		self.__costObra = float(costObra)
	def __str__(self):
		return f"{super().__str__()}\nfecha_i: {self.__fecha_i}\nfecha_f: {self.__fecha_f}\nTarea: {self.__tarea}"
	def sueldo(self):
		return self.__costObra - self.__mViatico - self.__mSVida
	def tarea(self):
		return self.__tarea
	def tareaFinalizada(self):
		return self.__fecha_f>=date().now()
	def costoObra(self):
		return self.__costObra