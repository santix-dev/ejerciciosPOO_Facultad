import csv
from viajero import Viajero

if __name__ == '__main__':
	lista=[]
	cadena="nombre@gmail.com.ar"
	cadena.split("@")
	archivo=open("viajeros.csv")
	reader=csv.reader(archivo,delimiter=",")
	for fila in reader:
		lista.append(Viajero(fila[0],fila[1],fila[2],fila[3],fila[4]))
	print("""
		1) ingresar numero de viajero
		2) Consultar cantidad de millas
		3) Acumular millas
		4) Canjear millas
		5) Ver viajero con mayor cantidad de millas
		6) Acumular millas con sobrecarga de operador
		7) Canjear millas con sobrecarga de operador
	""")
	opc=int(input("Ingrese opsao: "))
	while opc!=0:
		match opc:
			case 1:
				flag=False
				num=int(input("Ingrese numero de viajero: "))
				while not flag:
					i=0
					while (i<len(lista) and not flag):
						flag=lista[i].verifNum(num)
						i+=1
					if not flag:
						num=int(input("viajero no encontrado, ingrese numero nuevamente: "))
				i-=1
			case 2:
				print(f"Millas acumuladas: {lista[i].cantidadTotalDeMillas()}")
			case 3:
				millas=int(input("Ingrese la cantidad de millas a acumular: "))
				lista[i].acumulaarMillas(millas)
			case 4:
				millas=int(input("Ingrese la cantidad de millas a canjear"))
				lista[i].canjearMillas(millas)
			case 5:
				mayor=lista[0]
				for i in range(1,len(lista)):
					mayor=lista[i] if lista[i]>mayor else mayor
				print(f"El viajero con mas millas es {mayor.nombre()}")
			case 6:
				print(f"millas antes de acumular: {lista[i].cantidadTotalDeMillas()}")
				millas=int(input("Ingrese la cantidad de millas a acumular: "))
				lista[i]+millas
				print(f"millas despues de acumular: {lista[i].cantidadTotalDeMillas()}")
			case 7:
				print(f"millas antes de canjear: {lista[i].cantidadTotalDeMillas()}")
				millas=int(input("Ingrese la cantidad de millas a acumular: "))
				lista[i]-millas
				print(f"millas despues de canjear: {lista[i].cantidadTotalDeMillas()}")
			case _:
				pass
		print("""
		1) Cambiar numero de viajero
		2) Consultar cantidad de millas
		3) Acumular millas
		4) Canjear millas
		5) Ver viajero con mayor cantidad de millas
		6) Acumular millas con sobrecarga de operador
		7) Canjear millas con sobrecarga de operador
		""")
		opc=int(input("Ingrese opsao: "))
		print(opc)




