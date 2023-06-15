from tkinter import *
from tkinter import ttk


class Ventanta():
	__ventana=Tk()
	__ventana.title("Calculadora IPC")
	__ipc=StringVar()
	def __init__(self):
		self.__mainframe=ttk.Frame(self.__ventana,padding="3 3 12 12")#crea un marco (frame) que existira dentro de ventana, priimer paramtero
		self.__mainframe.grid(column=0,row=0,sticky=(N,W,E,S))#indica que el marco se colocara en la columna y fila 0 de la ventana. sticky hace referencia hacia donde se puede expandir		
		self.__mainframe.columnconfigure(4)
		self.__mainframe.rowconfigure(4)
		# ==============================================
		self.__item_label=ttk.Label(self.__mainframe,text="item")
		self.__cantidad_label=ttk.Label(self.__mainframe,text="Cantidad")
		self.__precio_ano_base_label=ttk.Label(self.__mainframe,text="precio ano base")
		self.__precio_ano_actual_label=ttk.Label(self.__mainframe,text="precio ano actual")
		self.__item_label.grid(column=0,row=0)
		self.__cantidad_label.grid(column=1,row=0)
		self.__precio_ano_base_label.grid(column=2,row=0)
		self.__precio_ano_actual_label.grid(column=3,row=0)
		# ==============================================
		self.__vestimenta_label=ttk.Label(self.__mainframe,text="Vestimenta")#creo una etiqueta que se encuentra dentro del marco mainframe
		self.__vestimenta_label.grid(column=0,row=1)
		self.__vestimenta_cant=StringVar() # crea una variable 
		self.__vestimenta_ano_base=StringVar() # crea una variable 
		self.__vestimenta_ano_actual=StringVar() # crea una variable 
		self.__vestimenta_cant_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__vestimenta_cant)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__vestimenta_cant_entry.grid(column=1,row=1,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		self.__vestimenta_ano_base_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__vestimenta_ano_base)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__vestimenta_ano_base_entry.grid(column=2,row=1,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		self.__vestimenta_ano_actual_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__vestimenta_ano_actual)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__vestimenta_ano_actual_entry.grid(column=3,row=1,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		# ==============================================
		self.__alimentos_label=ttk.Label(self.__mainframe,text="alimentos")#creo una etiqueta que se encuentra dentro del marco mainframe
		self.__alimentos_label.grid(column=0,row=2)
		self.__alimentos_cant=StringVar() # crea una variable 
		self.__alimentos_ano_base=StringVar() # crea una variable 
		self.__alimentos_ano_actual=StringVar() # crea una variable 
		self.__alimentos_cant_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__alimentos_cant)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__alimentos_cant_entry.grid(column=1,row=2,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		self.__alimentos_ano_base_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__alimentos_ano_base)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__alimentos_ano_base_entry.grid(column=2,row=2,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		self.__alimentos_ano_actual_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__alimentos_ano_actual)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__alimentos_ano_actual_entry.grid(column=3,row=2,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		# ==============================================
		self.__educacion_label=ttk.Label(self.__mainframe,text="educacion")#creo una etiqueta que se encuentra dentro del marco mainframe
		self.__educacion_label.grid(column=0,row=3)
		self.__educacion_cant=StringVar() # crea una variable 
		self.__educacion_ano_base=StringVar() # crea una variable 
		self.__educacion_ano_actual=StringVar() # crea una variable 
		self.__educacion_cant_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__educacion_cant)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__educacion_cant_entry.grid(column=1,row=3,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		self.__educacion_ano_base_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__educacion_ano_base)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__educacion_ano_base_entry.grid(column=2,row=3,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		self.__educacion_ano_actual_entry= ttk.Entry(self.__mainframe,width=7,textvariable=self.__educacion_ano_actual)# crea un input, que se encuentra en mainframe, tiene width 7 y lo que se ingresa lo guarda en textvariable
		self.__educacion_ano_actual_entry.grid(column=3,row=3,sticky=(W,E))# posiciono el input en la columna y fila 1, y le permito que se expanda hacia los lados	
		# ==============================================
		ttk.Button(self.__mainframe,text="Calcular IPC",command=self.calularIPC).grid(column=1,row=5,sticky=(W,E))
		ttk.Button(self.__mainframe,text="Salir").grid(column=2,row=5,columnspan=2,sticky=(W,E))
		# ==============================================
		ttk.Label(self.__mainframe,textvariable=self.__ipc).grid(column=1,row=6,sticky=(E))
		ttk.Label(self.__mainframe,text="IPC: ").grid(column=0,row=6,sticky=(E))

	def calularIPC(self):
		try:
			cant_v=round(float(self.__vestimenta_cant.get()),2)
			cant_a=round(float(self.__alimentos_cant.get()),2)
			cant_e=round(float(self.__educacion_cant.get()),2)
			p_b_v=round(float(self.__vestimenta_ano_base.get()),2)
			p_b_a=round(float(self.__alimentos_ano_base.get()),2)
			p_b_e=round(float(self.__educacion_ano_base.get()),2)
			p_a_v=round(float(self.__vestimenta_ano_actual.get()),2)
			p_a_a=round(float(self.__alimentos_ano_actual.get()),2)
			p_a_e=round(float(self.__educacion_ano_actual.get()),2)
			base=(cant_v*p_b_v+cant_a*p_b_a+cant_e*p_b_e)
			actual=(cant_v*p_a_v+cant_a*p_a_a+cant_e*p_a_e)
			self.__ipc.set((actual/base)*100)
		except:
			self.__ipc.set("Ingrese datos numericos")
	def ejecutar(self):
		self.__ventana.mainloop()
