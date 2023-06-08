import json
from apoyo import Apoyo
from docente import Docente
from docente_investigador import Doc_Inv
from investigador import Investigador
from lista import ListaEnlazada
from nodo import Nodo
from personal import Personal
from ManejadorPersonal import ManejadorPersonal
from ObjectEncoder import ObjectEncoder
if __name__ == '__main__':
	personal=ManejadorPersonal()
	personal.cargar()
	print("1) Agregar agentes a la colección.")
	print("2) Insertar a agentes a la colección.")
	print("3) Mostrar que tipo de agente se encuentra en una posicion de la lista.")
	print("4) generar un listado ordenado por nombre con todos los datos de los docentes investigadores de una carrera.")
	print("5) contar la cantidad de docentes investigadores, y de investigadores que trabajen en un area.")
	print("6) generar listado con nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
	print("7) Dada una categoría de investigación (I, II, III, IV o V), listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores de esa categoría. mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.    ")
	print("8) Almacenar los datos")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				personal.agregarAgente()
			case 2:
				personal.insertarAgente()
			case 3:
				pos=int(input("Ingrese posicion: "))
				personal.mostrarClase(pos)
			case 4:
				carre=input("Ingrese carrera: ")
				personal.listadoXnombreYcarrera(carre)
			case 5:
				area=input("Ingrese area: ")
				personal.contar_docInv_Inv(area)
			case 6:
				personal.listadoXapellido()
			case 7:
				categ=input("Ingrese categoría: ")
				personal.listadoXcategoria(categ)
			case 8:
				personal.guardarDatos()
		print("1) Agregar agentes a la colección.")
		print("2) Insertar a agentes a la colección.")
		print("3) Mostrar que tipo de agente se encuentra en una posicion de la lista.")
		print("4) generar un listado ordenado por nombre con todos los datos los docentes investigadores de una carrera.")
		print("5) contar la cantidad de docentes investigadores, y de investigadores que trabajen en un area.")
		print("6) generar listado con nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
		print("7) listar apellido, nombre e importe extra por docencia e investigación, de los docentes investigadores de una categoría. mostrar el total de dinero a solicitar al Ministerio")
		print("8) Almacenar los datos")
		opc=int(input(""))