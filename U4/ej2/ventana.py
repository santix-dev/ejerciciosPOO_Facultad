from tkinter import *
from tkinter import ttk

class ventana():
	__ventana=Tk()
	__ventana.title("Calculadora IVA")
	__ventana.geometry("300x300")
	__ventana.resizable(width=False,height=False)
	__porc=StringVar()
	def __init__(self):
		self.__mainframe=ttk.Frame(self.__ventana,padding="50 50 50 50")
		self.__mainframe.grid(column=0,row=0)
		self.__mainframe.columnconfigure(2,weight=1)
		self.__mainframe.rowconfigure(2,weight=1)
		#================================================
		ttk.Label(self.__mainframe,text="Precio sin IVA").grid(column=0,row=0)
		self.__precio_s_iva=StringVar()
		self.__precio_s_iva_entry=ttk.Entry(self.__mainframe,textvariable=self.__precio_s_iva)
		self.__precio_s_iva_entry.grid(column=1,row=0)
		#================================================
		ttk.Radiobutton(self.__mainframe,value=21,text="IVA 21%",variable=self.__porc).grid(column=0,row=1,sticky="W")
		ttk.Radiobutton(self.__mainframe,value=10.5,text="IVA 10.5%",variable=self.__porc).grid(column=0,row=2,sticky="W")
		#ttk.Label(self.__mainframe,textvariable=self.__porc).grid(column=0,row=2)
		#================================================
		ttk.Label(self.__mainframe,text="IVA").grid(column=0,row=3)
		self.__iva=StringVar()
		self.__iva_entry=ttk.Entry(self.__mainframe,textvariable=self.__iva)
		self.__iva_entry.grid(column=1,row=3,pady=10)

		#================================================
		ttk.Label(self.__mainframe,text="Precio con IVA").grid(column=0,row=4)
		self.__precio_c_iva=StringVar()
		self.__precio_c_iva_entry=ttk.Entry(self.__mainframe,textvariable=self.__precio_c_iva)
		self.__precio_c_iva_entry.grid(column=1,row=4)
		#================================================
		estilo_salir=ttk.Style()
		estilo_salir.configure("TButton",background="red")
		# estilo_salir.configure("boton.salir",background="red")
		self.__calcular=ttk.Button(self.__mainframe,text="Calcular",command=self.calcular)
		self.__calcular.grid(column=0,row=5,pady=10)
		self.__salir=ttk.Button(self.__mainframe,text="Salir",command=self.__ventana.destroy)
		self.__salir.grid(column=1,row=5,pady=10,sticky="e")
		#================================================
		self.__ventana.mainloop()


	def calcular(self):
		try:
			precio=round(float(self.__precio_s_iva.get()),2)
			porc=round(float(self.__porc.get()),2)/100
			iva=round(precio*porc,2)
			self.__iva.set(iva)
			self.__precio_c_iva.set(iva+precio)
		except:
			ttk.Label(self.__mainframe,text="Ingrese datos numericos").grid(column=0,row=6,columnspan=2)
if __name__ == '__main__':
	vent=ventana()