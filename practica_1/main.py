import csv
from cliente import Cliente
from reparacion import Reparacion
from manejadorCliente import ManejadorCliente
from manejadorReparacion import ManejadorReparacion

if __name__ == '__main__':
	clientes=ManejadorCliente()
	clientes.cargar()
	reparaciones=ManejadorReparacion()
	reparaciones.cargar()
	print("""
	1) Ver reparaciones y datos de un cliente	
	2) Ver si se terminaron las reparaciones
	3) Listar clientes con reparaciones sin terminar
	4) Ver clientes que le hacen servicio a mas de un vehiculo
		""")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				dni=str(input("Ingrese dni cliente: "))
				i=clientes.indiceCliente(dni)
				while type(i)==type(False):
					dni=str(input("Cliente no encontrado, ingrese dni: "))
				clientes.mostrarCliente(i)
				pat=clientes.patenteCliente(i)
				reparaciones.mostrarReparacionesXPatente(pat)
			case 2:
				pat=str(input("Ingrese la patente"))
				flag=reparaciones.reparacionesTerminadas(pat)
				if flag:
					clientes.cambiarEstadoT(pat)
					reparaciones.mostrarTotal(pat)
			case 3:
				clientes.pendientes(reparaciones)
			case 4:
				clientes.clientesConMasDeUnCarro()

		print("""
	1) Ver reparaciones y datos de un cliente	
	2) Ver si se terminaron las reparaciones
	3) Listar clientes con reparaciones sin terminar
	4) Ver clientes que le hacen servicio a mas de un vehiculo
		""")
		opc=int(input(""))
