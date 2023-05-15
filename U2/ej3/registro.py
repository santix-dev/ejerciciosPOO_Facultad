class Registro():
	__temperatura=0
	__humedad=0
	__presion=0
	def __init__(self, temp=0,hum=0,pres=0):
		self.__temperatura = int(temp)
		self.__humedad = int(hum)
		self.__presion = int(pres)
		return
	def mostrarDatos(self):
		print(f"temperatura= {self.__temperatura}  humedad= {self.__humedad}  presion= {self.__presion}")
		return
	def temperatura(self):
		return self.__temperatura	
	def humedad(self):
		return self.__humedad	
	def presion(self):
		return self.__presion	