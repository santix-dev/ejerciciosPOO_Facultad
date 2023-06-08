from personal import Personal
from docente import Docente
from investigador import Investigador
class Doc_Inv(Docente,Investigador):
	"""docstring for Doc_Inv"""
	def __init__(self,categoria,plus,carrera,cargo,catedra,area,tipo,cuil,apellido,nombre,basico,antig):
		Docente.__init__(self,carrera,cargo,catedra,cuil,apellido,nombre,basico,antig)
		Investigador.__init__(self,area,tipo,cuil,apellido,nombre,basico,antig)
		self.__categoria = categoria.lower()
		self.__plus = float(plus)
	def toJSON(self):
		d={
			"__class__":self.__class__.__name__,
			"__atributos__":{
				"categoria":self.__categoria,
				"plus":self.__plus,
				"carrera":self._carrera,
				"cargo":self._cargo,
				"catedra":self._catedra,
				"area":self._area,
				"tipo":self._tipo,
				"cuil":self._cuil,
				"apellido":self._apellido,
				"nombre":self._nombre,
				"basico":self._basico,
				"antig":self._antig,
			}
		}
		# print(d)
		return d
	def __str__(self):
		return f"""
			categoria:{self.__categoria},
			plus:{self.__plus},
			carrera:{self._carrera},
			cargo:{self._cargo},
			catedra:{self._catedra},
			area:{self._area},
			tipo:{self._tipo},
			cuil:{self._cuil},
			apellido:{self._apellido},
			nombre:{self._nombre},
			basico:{self._basico},
			antig:{self._antig}"""
	def __gt__(self,other):
		return self._nombre>other._nombre
	def clase(self):
		return self.__class__.__name__
	def categoria(self):
		return self.__categoria
	def plus(self):
		return self.__plus



if __name__ == '__main__':
	p=Doc_Inv("ii",10000,"Informatica","jtp","algoritmos","inteligencia artificial","jr",20443166662,"gimenez","santiago",30000,1)
	p.toJSON()