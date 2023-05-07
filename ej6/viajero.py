class Viajero():
	__num_viajero=""
	__dni=""
	__nom=""
	__ape=""
	__millas_acum=""
	def __init__(self, num="",dni="",nom="",ape="",millas=""):
		self.__num_viajero=num
		self.__dni=dni
		self.__nom=nom
		self.__ape=ape
		self.__millas_acum=int(millas)
	def cantidadTotalDeMillas(self):
		return self.__millas_acum
	def acumularMillas(self,millas):
		self.__millas_acum+=millas
		return self.__millas_acum
	def canjearMillas(self,millas):
		if self.__millas_acum>=millas:
			self.__millas_acum-=millas
			print(f"millas canjeadas. millas restantes: {self.__millas_acum}")
		else:
			print("error: usted no cuenta con suficientes millas")
		return self.__millas_acum
	def verifNum(self,num):
		return int(self.__num_viajero)==num
	def __gt__(self,other):
		return self.__millas_acum>other.cantidadTotalDeMillas()
	def nombre(self):
		return self.__nom
	def __add__(self,other):
		self.__millas_acum+=int(other)
		return self
	def __sub__(self,other):
		self.__millas_acum-=int(other)
		return self


		
