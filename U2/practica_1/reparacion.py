class Reparacion(object):
	def __init__(self, patente="",reparacion="",precio_rep="",precio_man_obra="",estado=""):
		self.__patente = patente
		self.__reparacion = reparacion
		self.__precio_rep = float(precio_rep)
		self.__precio_man_obra = float(precio_man_obra)
		self.__estado = estado
	def patente(self):
		return self.__patente
	def __str__(self):
		return f"""{self.__reparacion}		{self.__precio_rep}		{self.__precio_man_obra}		{self.__precio_rep+self.__precio_man_obra}"""
	def subtotal(self):
		return self.__precio_rep+self.__precio_man_obra
	def estado(self):
		return self.__estado
	def info(self):
		return self.__reparacion
		