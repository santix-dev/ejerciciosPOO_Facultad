from clasereparacion import Reparacion
import csv

class Manejador_reparacion:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo= open("reparaciones.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            crear=Reparacion(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__lista.append(crear)
        
    def getvehiculo(self, patente):
        i=0
        repacion=None
        while i<len(self.__lista) and repacion==None:
            if self.__lista[i].getpatente() == str(patente):
                repacion=self.__lista[i]
            i+=1
        return repacion
    def verifReparaciones(self,patente):
        coincidencias=0
        terminados=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getpatente() == str(patente):
                coincidencias+=1
                if reparacion.getvehiculo(self.__lista[i].getpatente()).getestado() == "T":
                    terminados+=1

        if c == j:#Todas las reparaciones estan terminadas
            return True
        else:
            return False
    