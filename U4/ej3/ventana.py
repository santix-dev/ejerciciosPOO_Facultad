from dolar import Dolar
from tkinter import *
from tkinter import ttk
class Ventana():
	"""docstring for Ventana"""
	__dolar=Dolar()
	def __init__(self):
		self.__ventana = Tk()
		self.__ventana.title("Conversor dolares")
		self.__mainframe=ttk.Frame(self.__ventana)
		self.__mainframe.grid(column=0,row=0)
		self.__pesos=StringVar()
		self.__dolares=StringVar()
		self.__dolares.trace("w",self.calcular)
		#=============================
		self.__dolares_entry=ttk.Entry(self.__mainframe,textvariable=self.__dolares)
		self.__dolares_entry.grid(column=1,row=0)
		ttk.Label(self.__mainframe,text="dolares").grid(column=2,row=0)
		ttk.Label(self.__mainframe,text="es equivalente a").grid(column=0,row=1)
		ttk.Label(self.__mainframe,textvariable=self.__pesos,text="xx.xx").grid(column=1,row=1)
		ttk.Label(self.__mainframe,text="pesos").grid(column=2,row=1)
	def calcular(self,*args):
		try:
			dolares=float(self.__dolares.get())
			self.__pesos.set(dolares*self.__dolar.venta())
		except:
			self.__pesos.set(0)
			self.__dolares.set(0)
	def ejecutar(self):
		self.__ventana.mainloop()
