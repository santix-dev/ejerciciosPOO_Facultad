import csv
from registro import Registro
from manejador import manejadorReg

if __name__=="__main__":
	mes=manejadorReg()
	archivo=open("registrometeorologico.csv")
	reader=csv.reader(archivo)
	for fila in reader:
		mes.cargar(fila)
	print("""
		1) Mostrar dias de mayor y menor valor de las variables
		2) Mostrar temperatura promedio por cada hora del mes
		3) Mostrar valores de un dia

		""")
	opc=int(input(""))
	match opc:
		case 1:
			print("Dia de mayor temperatura: ",mes.mayorDiaTemp())
			print("Dia de mayor humedad: ",mes.mayorDiaHum())
			print("Dia de mayor presion: ",mes.mayorDiaPres())
			print("Dia de menor temperatura: ",mes.menorDiaTemp())
			print("Dia de menor humedad: ",mes.menorDiaHum())
			print("Dia de menor presion: ",mes.menorDiaPres())
		case 2:
			mes.tempPromedioXHora()
		case 3:
			dia=int(input("Ingrese el dia a mostrar"))
			mes.mostrarVariablesDiarias(dia)


	# mes.mostrarDatos()
