import numpy as np
from Inscripcion import Inscripcion
class ManejadorInscripciones():
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension=10, incremento=5):
        self.__inscripciones = np.empty(dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarInscripcion(self, unInscripcion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad]=unInscripcion
        self.__cantidad += 1
    def getInscripcion(self, indice):
        return self.__inscripciones[indice]
    def inscribir(self,manPersonas,taller):
        nom=input("Ingrese nombre: ")
        direc=input("Ingrese direccion: ")
        dni=input("Ingrese DNI: ")
        manPersonas.agregarPersona(nom,direc,dni)
        pers=manPersonas.ultimaPersona()
        fecha=input("Ingrese fecha (dd/mm/aaaa): ")
        self.agregarInscripcion(Inscripcion(fecha,False,pers,taller))
    def consultarInscripcion(self,dni):
        flag=False
        i=0
        while i<self.__cantidad and not flag:
            if self.__inscripciones[i].persona().dni()==dni:
                print(self.__inscripciones[i].taller().nombreTaller())
                flag=True
                if not self.__inscripciones[i].pagado():
                    print(self.__inscripciones[i].taller().monto())
                else:
                    print("Ya pago")
            else:
                i+=1
        if i==self.__cantidad:
            print(f"La persona con dni {dni} no esta inscripta")
    def listarAlumnosXtaller(self,idTaller):
        for i in range(self.__cantidad):
            if self.__inscripciones[i].idTaller()==idTaller:
                print(self.__inscripciones[i].persona())
    def pagar(self,dni):
        flag=False
        i=0
        while i<self.__cantidad and not flag:
            if self.__inscripciones[i].persona().dni()==dni:
                self.__inscripciones[i].pagar()
                flag=True
            else:
                i+=1
        if i==self.__cantidad:
            print(f"La persona con dni {dni} no esta inscripta")
    def toJSON(self):
        d={
        '__class__':self.__class__.__name__,
        'inscripciones':[ins.toJSON() for ins in self.__inscripciones]
        }
        return d


    # def mostrarInscripciones(self):
    #     for i in range(self.__cantidad):
    #         self.__inscripciones[i].mostrarDatosInscripcion()
    # def cargar(self,nomArch="Inscripciones.csv"):
    # 	archivo=open(nomArch)
    # 	reader=csv.reader(archivo,delimiter=";")
    #     reader
    # 	for fila in reader:
    # 		self.agregarInscripcion(Inscripcion(fila[0],fila[1],fila[2],fila[3],fila[4]))