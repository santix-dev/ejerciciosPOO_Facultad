from Persona import Persona
from Taller import Taller
class Inscripcion(object):
	"""docstring for Inscripcion"""
	def __init__(self,fecha,pago,persona,taller):
		self.__fecha = fecha
		self.__pago = pago
		self.__persona = persona
		self.__taller = taller
	def idTaller(self):
		return self.__taller.idTaller()
	def persona(self):
		return self.__persona
	def pagar(self):
		self.__pago=True
	def toJSON(self):
		d=
		{
			'__class__':self.__class__.__name__,
			'__atributos__':
			{
				'fecha':self.__fecha,
				'pago':self.__pago,
				'persona':self.__persona,
				'taller':self.__taller
			}
		}
		return d
