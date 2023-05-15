import csv
from planAhorro import PlanAhorro
from manejadorPlan import ManejadorPlan

if __name__ == '__main__':
	lista=ManejadorPlan()
	lista.carga("planes.csv")
	print("""
1) Actualizar precios
2) Ingresar valor y mostrar plan con cuotas menores a ese valor
3) Mostrar monto para licitar vehiculo
4) Modificar licitacion de un plan por su codigo
"""	)
	opc=int(input("Ingrese opcion: "))
	while opc!=0:
		match opc:
			case 1:
				lista.actualizarPrecios()
			case 2:
				lista.planesInferiores()
			case 3:
				lista.valorLicitaciones()
			case 4:
				lista.modificarLicitacionPlan()
		print("""
1) Actualizar precios
2) Ingresar valor y mostrar plan con cuotas menores a ese valor
3) Mostrar monto para licitar vehiculo
4) Modificar licitacion de un plan por su codigo
"""	)
		opc=int(input("Ingrese opcion: "))
		