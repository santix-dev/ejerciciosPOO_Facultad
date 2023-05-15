import csv
from materia import MateriaAprobada
class ControladorMateria():
	def __init__(self):
		self.__lista = []
	def agregar(self,dni,nombre,fecha,nota,aprobacion):
		self.__lista.append(MateriaAprobada(dni,nombre,fecha,nota,aprobacion))
	def cargar(self,nomArch="materiasAprobadas.csv"):
		archivo=open(nomArch)
		reader=csv.reader(archivo,delimiter=";")
		for fila in reader:
			self.agregar(fila[0],fila[1],fila[2],fila[3],fila[4])
	def promediosAlumno(self,dni):
		# se calcula un solo promedio ya que el archivo y el ejercicio tratan unicamente de materias
		# aprobadas, por lo tanto el promedio con y sin aplazos es el mismo, ya que no hay materias
		# desaprobadas para sumar
		nota=0.0
		cantNotas=0
		for registro in self.__lista:
			if registro.dni()==dni:
				nota+=registro.nota()
				cantNotas+=1
		nota/=cantNotas
		return nota
	def promocionadosConMas7(self,mat,alumnos):
		print("DNI    Apellido y nombre    Fecha    Nota    Año que cursa")
		for materia in self.__lista:
			if materia.materia()==mat:
				dni=materia.dni()
				i=alumnos.obtenerIndiceAlumno(dni)
				if i!=False:
					alumno=alumnos.getAlumno(i)
					print(f"{alumno.dni()}    {alumno.nombre()}    {materia.fecha()}    {materia.nota()}    {alumno.anio()}")

