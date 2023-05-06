import csv
from planAhorro import PlanAhorro
class ManejadorPlan():
	__lista=[]
	def __init__(self):
		self.__lista = []
		return
	def carga(self, nomArch="planes.csv"):
		archivo=open(nomArch)
		reader=csv.reader(archivo, delimiter=";")
		for fila in reader:
			self.__lista.append(PlanAhorro(fila[0],fila[1],fila[2],fila[3]))
		return
	def actualizarPrecios(self):
		for plan in self.__lista:
			print(plan)
			valorNuevo=int(input("Ingrese nuevo valor (0 para no cambiar)"))
			if valorNuevo>0:
				plan.actualizarValor(valorNuevo)
		return
	def planesInferiores(self):
		valor=float(input("Ingrese valor de cuota maximo: "))
		for plan in self.__lista:
			if plan.valorCuota()<valor:
				print(plan,f" Valor cuota: {plan.valorCuota()}")
	def valorLicitaciones(self):
		for plan in self.__lista:
			plan.montoLicitacion()
		return
	def modificarLicitacionPlan(self):
		cod=int(input("Ingrese Codigo de plan: "))
		i=-1
		flag=False
		while not flag and i<len(self.__lista):
			i+=1
			flag=self.__lista[i].codigo()==cod
		if not flag:
			print("No se encontro el plan con ese codigo")
		else:
			new=int(input("Ingrese la cantidad de cuotas para licitar: "))
			self.__lista[i].modificarCuotasLicitacion(new)
		return

