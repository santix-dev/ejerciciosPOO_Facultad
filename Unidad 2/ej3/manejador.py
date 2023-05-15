from registro import Registro
class manejadorReg():
	__lista=[]
	def __init__(self):
		self.__lista = [[]]
		return
	def cargar(self, obj):
		i=int(obj[0])
		if i>len(self.__lista):
			self.__lista.append([])
		self.__lista[i-1].append(Registro(obj[2],obj[3],obj[4]))
	def mostrarDatos(self):
		for dia in self.__lista:
			print(f"=====Dia: {int(self.__lista.index(dia))+1}======")
			for fila in dia:
				fila.mostrarDatos()
		return
	def mayorDiaHum(self):
		hum=0
		ndia=1
		for dia in self.__lista:
			for fila in dia:
				if fila.humedad()>hum:
					hum=fila.humedad()
					ndia=int(self.__lista.index(dia))+1
		return ndia
	def mayorDiaTemp(self):
		temp=0
		ndia=1
		for dia in self.__lista:
			for fila in dia:
				if fila.temperatura()>temp:
					temp=fila.temperatura()
					ndia=int(self.__lista.index(dia))+1
		return ndia
	def mayorDiaPres(self):
		pres=0
		ndia=1
		for dia in self.__lista:
			for fila in dia:
				if fila.presion()>pres:
					pres=fila.presion()
					ndia=int(self.__lista.index(dia))+1
		return ndia
	def menorDiaHum(self):
		hum=999
		ndia=1
		for dia in self.__lista:
			for fila in dia:
				if fila.humedad()<hum:
					hum=fila.humedad()
					ndia=int(self.__lista.index(dia))+1
		return ndia
	def menorDiaTemp(self):
		temp=999
		ndia=1
		for dia in self.__lista:
			for fila in dia:
				if fila.temperatura()<temp:
					temp=fila.temperatura()
					ndia=int(self.__lista.index(dia))+1
		return ndia
	def menorDiaPres(self):
		pres=999
		ndia=1
		for dia in self.__lista:
			for fila in dia:
				if fila.presion()<pres:
					pres=fila.presion()
					ndia=int(self.__lista.index(dia))+1
		return ndia
	def tempPromedioXHora(self):
		# horas es una lista de 24 componentes (acumuladores)
		# cada uno ira acumulando la temperatura por la misma hora de cada dia
		# inicializacion de la lista horas en 0
		horas=[]
		for i in range(0,24):
			horas.append(0)
		# se acumula por cada hora, la temperatura de todos los dias
		for dia in self.__lista:
			i=0
			for reg in dia:
				horas[i]+=reg.temperatura()
				i+=1
		# se saca el promedio de cada hora
		dias=len(self.__lista)
		for i in range(len(horas)):
			horas[i]/=dias
		#se muestra
		i=0
		for promHora in horas:
			print(f"Temperatura promedio de las {i}hs: {promHora}")
			i+=1
		return
	def mostrarVariablesDiarias(self,dia):
		tab=" "*20
		print(f"hora{tab}temperatura{tab}humedad{tab}presion")
		i=0
		for reg in self.__lista[dia-1]:
			print(f" {i}  {tab}    {reg.temperatura()}    {tab}    {reg.humedad()}    {tab}    {reg.presion()}")
			i+=1