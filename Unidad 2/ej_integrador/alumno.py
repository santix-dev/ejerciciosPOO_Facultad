class Alumno():
	def __init__(self, dni="",apellido="",nombre="",carrera="",anio=""):
		self.__dni = str(dni)
		self.__apellido = apellido
		self.__nombre = nombre
		self.__carrera = carrera
		self.__anio = int(anio)
	def mostrarDatosAlumno(self):
		print(f"""
DNI: {self.__dni}
Apellido y nombre: {self.__apellido} {self.__nombre}
Carrera: {self.__carrera}, {self.__anio}° año
			""")
	def verificarDni(self,dni):
		return self.__dni==dni
	def dni(self):
		return self.__dni
	def nombre(self):
		return f"{self.__apellido} {self.__nombre}"
	def anio(self):
		return self.__anio
	def __lt__(self,other):
		return self.__anio<other.__anio
		