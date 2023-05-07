import csv
import numpy as np

from alumno import Alumno
from materia import MateriaAprobada
from controladorAlumno import ControladorAlumno
from controladorMateria import ControladorMateria

if __name__ == '__main__':
	alumnos=ControladorAlumno(9)
	materias=ControladorMateria()
	alumnos.cargar()
	materias.cargar()
	print("""
1) Promedios de un alumno
2) Estudiantes que aprobaron una materia promocionando
3) Listado de alumnos
		""")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				dni=str(input("Ingrese DNI: "))
				while not alumnos.buscarAlumno(dni) and dni!="0":
					dni=str(input("Alumno no encontrado. Ingrese DNI: "))
				print("Promedio alumno (con y sin aplazos): ",materias.promediosAlumno(dni))
			case 2:
				mat=str(input("Ingrese el nombre de una materia")).lower()
				materias.promocionadosConMas7(mat,alumnos)
			case 3:
				alumnos.ordenars()
				alumnos.mostrarAlumnos()



		print("""
1) Promedios de un alumno
2) Estudiantes que aprobaron una materia promocionando
3) Listado de alumnos
			""")
		opc=int(input(""))
