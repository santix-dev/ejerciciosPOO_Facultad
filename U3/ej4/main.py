from Empleado import Empleado
from EmpPlanta import EmpPlanta
from EmpContratado import EmpContratado
from ManejadorEmpleados import ManejadorEmpleados
if __name__ == '__main__':
	empleados=ManejadorEmpleados()
	empleados.cargar()
	print("1) Registrar horas")
	print("2) Ver total por tarea")
	print("3) Ayuda economica")
	print("4) Mostrar sueldos")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				dni=input("Ingrese dni: ")
				horas=input("Ingrese horas")
				empleados.registrarHoras(dni,horas)
			case 2:
				tarea=input("Ingrese tarea: ")
				empleados.totalXtarea(tarea)
			case 3:
				empleados.ayudas()
			case 4:
				empleados.sueldos()
		print("1) Registrar horas")
		print("2) Ver total por tarea")
		print("3) Ayuda economica")
		print("4) Mostrar sueldos")
		opc=int(input(""))