from carrera import Carrera
class Facultad(object):
	"""docstring for Facultad"""
	def __init__(self, codigo,nombre,direccion,localidad,telefono):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__direccion = direccion
		self.__localidad = localidad
		self.__telefono = telefono
		self.__lista = []
	def agregarCarrera(self,codigo,nombre,titulo,duracion,tipo):
		self.__lista.append(Carrera(codigo,nombre,titulo,duracion,tipo))
	def __str__(self):
		return f"""{self.__codigo}) {self.__nombre}\n direccion: {self.__direccion} localidad: {self.__localidad}"""
	def mostrarCarreras(self):
		for carrera in self.__lista:
			print(carrera)
	def buscarCarrera(self,carrera):
		carrera=carrera.lower()
		i=0
		flag=False
		while not flag and i<len(self.__lista):
			if self.__lista[i].nombre()==carrera:
				print(f"{self.__codigo}.{self.__lista[i].codigo()}")
				print(self.__lista[i])
				print("Localidad: ",self.__localidad)
				flag=True
			else:
				i+=1
