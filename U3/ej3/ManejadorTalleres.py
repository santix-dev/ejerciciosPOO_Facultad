import numpy as np
from Taller import Taller
class ManejadorTalleres():
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension=10, incremento=5):
        self.__talleres = np.empty(dimension, dtype=Taller)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarTaller(self, unTaller):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__talleres.resize(self.__dimension)
        self.__talleres[self.__cantidad]=unTaller
        self.__cantidad += 1
    def getTaller(self, indice):
        i=0
        flag=False
        while not flag and i<self.__cantidad:
            if indice==self.__talleres[i].idTaller():
                flag=True
            else:
                i+=1
        if flag:
            return True

        return self.__talleres[indice]
    def listar(self):
        for i in range(self.__cantidad):
            self.__talleres[i].mostrarDatosTaller()
    def cargar(self,nomArch="Talleres.csv"):
        archivo=open(nomArch)
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            self.agregarTaller(Taller(fila[0],fila[1],fila[2],fila[3]))