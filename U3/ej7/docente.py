from personal import Personal
class Docente(Personal):
	"""docstring for Docente"""
	def __init__(self,carrera,cargo,catedra,cuil,apellido,nombre,basico,antig):
		Personal.__init__(self,cuil,apellido,nombre,basico,antig)
		self._carrera = carrera.lower()
		self._cargo = cargo.lower()
		self._catedra = catedra.lower()
	def toJSON(self):
		d={
			"__class__":self.__class__.__name__,
			"__atributos__":{
				"carrera":self._carrera,
				"cargo":self._cargo,
				"catedra":self._catedra,
				"cuil":self._cuil,
				"apellido":self._apellido,
				"nombre":self._nombre,
				"basico":self._basico,
				"antig":self._antig,
			}
		}
		# print(d)
		return d
	def clase(self):
		return self.__class__.__name__

if __name__ == '__main__':
	p=Docente("Informatica","jtp","algoritmos",20443166662,"gimenez","santiago",30000,1)
	p.toJSON()