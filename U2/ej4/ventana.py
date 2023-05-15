from coordenada import Coordenada
class Ventana():
	__titulo=""
	__top=0
	__bottom=0
	__left=0
	__right=0
	__Y=0
	__X=0
	def __init__(self,titulo="",top=0,left=0,bot=500,right=500,x=0,y=0):
		self.__titulo = titulo
		self.__top=int(top)
		self.__left=int(left)
		self.__bottom=int(bot)
		self.__right=int(right)
		self.__X=int(x)
		self.__Y=int(y)
	def alto(self):
		return self.__bottom-self.__top
	def ancho(self):
		return self.__right-self.__left
	def getTitulo(self):
		return self.__titulo
	def mostrar(self):
		print(self.__titulo)
		for i in range(self.__top//10,self.__bottom//10):
			print("."*((self.__right-self.__left)//10))
		return
	def moverDerecha(self,mov=0):
		self.__X+=mov
		return
	def moverIzquierda(self,mov=0):
		self.__X-=mov
		return
	def bajar(self,mov=0):
		self.__Y+=mov
		return
	def subir(self,mov=0):
		self.__Y-=mov
		return		

		
		
		