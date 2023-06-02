import csv
import csv
import numpy as np
from Taller import Taller
from Persona import Persona
from Inscripcion import Inscripcion
from ManejadorTalleres import ManejadorTalleres
from ManejadorPersonas import ManejadorPersonas
from ManejadorInscripciones import ManejadorInscripciones
from ObjectEncoder import ObjectEncoder

if __name__ == '__main__':
	personas=ManejadorPersonas()
	inscripciones=ManejadorInscripciones()
	talleres=ManejadorTalleres()
	print("1) Cargar talleres y personas")
	print("2) Inscribir persona en taller")
	print("3) Consultar inscripcion")
	print("4) Consultar inscriptos a un taller")
	print("5) Registrar pago")
	print("6) Guardar Inscripciones")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				talleres.cargar()
			case 2:
				talleres.listar()
				taller=int(input("Ingrese id taller"))
				taller=talleres.getTaller(taller)
				inscripciones.inscribir(personas,taller)
			case 3:
				dni=input("Ingrese DNI:")
				inscripciones.consultarInscripcion(dni)
			case 4:
				talleres.listar()
				taller=int(input("Ingrese id taller"))
				inscripciones.listarAlumnosXtaller(taller)
			case 5:
				dni=input("Ingrese dni: ")
				inscripciones.pagar(dni)
			case 6:
				d=inscripciones.toJSON()
				vuelca=ObjectEncoder()
				vuelca.guardarJSON(d,"inscripciones.json")
		print("1) Cargar talleres y personas")
		print("2) Inscribir persona en taller")
		print("3) Consultar inscripcion")
		print("4) Consultar inscriptos a un taller")
		print("5) Registrar pago")
		print("6) Guardar Inscripciones")
		opc=int(input(""))



