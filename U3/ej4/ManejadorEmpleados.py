from Empleado import Empleado
from EmpPlanta import EmpPlanta
from EmpExterno import EmpExterno
from EmpContratado import EmpContratado
class ManejadorEmpleados(object):
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension=10, incremento=5):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarInscripcion(self, unEmpleado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad]=unEmpleado
        self.__cantidad += 1
    def cargar(self):
    	archivo=open("planta.csv")
    	reader=csv.reader(archivo,delimiter=";")
    	for fila in reader:
    		self.agregarInscripcion(EmpPlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
    	archivo=open("contratados.csv")
    	reader=csv.reader(archivo,delimiter=";")
    	for fila in reader:
    		self.agregarInscripcion(EmpContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6]))
    	archivo=open("externos.csv")
    	reader=csv.reader(archivo,delimiter=";")
    	for fila in reader:
    		self.agregarInscripcion(EmpExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9]))
    def registrarHoras(self,dni,horas):
    	i=0
    	flag=False
    	while not flag and i<self.__cantidad:
    		if self.__empleados[i].dni()==dni:
    			horas=input("Ingrese horas: ")
    			self.__empleados[i].registrarHoras(horas)
    		else:
    			i+=1
    def totalXtarea(self,tarea):
    	total=0
    	for i in range(self.__cantidad):
    		if isinstance(self.__empleados[i],EmpExterno):
    			if self.__empleados[i].tarea()==tarea and self.__empleados[i].tareaFinalizada():
    				total+=self.__empleados[i].costoObra()
    	print(f"El total a pagar para: {tarea}, es de {total}")
    def ayudas(self):
    	for i in range(self.__cantidad):
    		if self.__empleados[i].sueldo()<150000:
    			print(f"{self.__empleados[i].nomDirDni()}")
    def sueldos(self):
    	for i in range(self.__cantidad):
    		print(f"{self.__empleados[i].nombre()}, Tel.: {self.__empleados[i].telefono()}\nSueldo: {self.__empleados[i].sueldo()}")

