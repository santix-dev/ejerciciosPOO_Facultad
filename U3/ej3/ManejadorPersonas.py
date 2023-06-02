class ManejadorPersonas(object):
	"""docstring for ManejadorPersona"""
	def __init__(self):
		self.__lista = []
	def cargar(self,archivo="Personas.csv"):
		archivo=open(archivo)
		reader=csv.reader(archivo,delimiter=";")
		next(reader)
		for fila in reader:
			self.__lista.append(Persona(fila[0],fila[1],fila[2]))
	def listar(self):
		for Persona in self.__lista:
			print(Persona)
	def Persona(self,i):
		return self.__lista[i-1]
	def agregarPersona(self,nom,direc,dni):
		self.__lista.append(Persona(nom,direc,dni))
	def ultimaPersona(self):
		return self.__lista[-1]