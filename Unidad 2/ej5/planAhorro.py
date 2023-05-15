class PlanAhorro():
	__codigo=0
	__modelo=""
	__version=""
	__valor=0.0
	__cuotas=int(60)
	__licit=int(20)
	def __init__(self, codigo=0, modelo="",version="",valor=0.0):
		self.__codigo = int(codigo)
		self.__modelo = modelo
		self.__version = version
		self.__valor = float(valor)
		self.__licit = self.__licit
		return
	def actualizarValor(self,new=0):
		self.__valor=float(new)
		return 
	def valorCuota(self):
		return (self.__valor/self.__cuotas)+self.__valor*0.1
	def __str__(self):
		return f"Codigo: {self.__codigo}   Modelo: {self.__modelo}   Version: {self.__version} Valor: {self.__valor}"
	def montoLicitacion(self):
		print(f"Para licitar el vehiculo {self.__modelo} {self.__version} necesita tener pagado ${float(self.valorCuota())*self.__licit}")
		return
	def codigo(self):
		return self.__codigo
	def modificarCuotasLicitacion(self,newLicit):
		self.__licit=newLicit
		return