class Cliente(object):
	def __init__(self, dni="",apellido="",nombre="",telefono="",patente="",vehiculo="",estado=""):
		self.__dni = str(dni)
		self.__apellido = apellido
		self.__nombre = nombre
		self.__telefono = telefono
		self.__patente = patente
		self.__vehiculo = vehiculo
		self.__estado = estado #t terminado p pendiente
	def verifDNI(self,dni):
		return self.__dni==str(dni)
	def __str__(self):
		return f"""DNI: {self.__dni}				Apellido y nom: {self.__apellido} {self.__nombre}
Patente: {self.__patente}					Vehiculo: {self.__vehiculo}"""
	def patente(self):
		return self.__patente
	def estadoTerminado(self):
		self.__estado="T"
	def mostrarDatosParaPagar(self):
		print(f"""{self.__nombre} {self.__apellido}   tel: {self.__telefono}   vehiculo: {self.__vehiculo}""")
	def datosCliPendiente(self):
		print(f"""{self.__nombre} {self.__apellido}   tel: {self.__telefono}   
patente: {self.__patente}			vehiculo: {self.__vehiculo}""")
	def estado(self):
		return self.__estado
	def __eq__(self,other):
		return (self.__dni==other.__dni and self.__apellido==other.__apellido and self.__nombre==other.__nombre and self.__telefono==other.__telefono)

		