from personal import Personal
from docente import Docente
from investigador import Investigador
class Doc_Inv(Docente,Investigador):
	"""docstring for Doc_Inv"""
	def __init__(self,categoria,plus,carrera,cargo,catedra,area,tipo,cuil,apellido,nombre,basico,antig):
		Docente.__init__(self,carrera,cargo,catedra,cuil,apellido,nombre,basico,antig)
		Investigador.__init__(self,area,tipo,cuil,apellido,nombre,basico,antig)
		self.__categoria = categoria
		self.__plus = plus
		