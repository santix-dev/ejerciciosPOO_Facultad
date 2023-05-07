class Alumno():
	def __init__(self, dni="",apellido="",nombre="",carrera="",anio=""):
		self.__dni = dni
		self.__apellido = apellido
		self.__nombre = nombre
		self.__carrera = carrera
		self.__anio = int(anio)
	def mostrarDatosAlumnno(self):
		print(f"""
DNI: {self.__dni}
Apellido y nombre: {self.__apellido} {self.__nombre}
Carrera: {self.__carrera}, {self.__anio}° año
			""")
		