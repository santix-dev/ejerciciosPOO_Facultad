# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:58:50 2020

@author: morte
@edited by: santix
"""
import csv
import numpy as np
from alumno import Alumno
class ControladorAlumno():
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__alumnos = np.empty(dimension, dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarAlumno(self, unAlumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]=unAlumno
        self.__cantidad += 1
    def getAlumno(self, indice):
        return self.__alumnos[indice]
    def mostrarAlumnos(self):
        for i in range(self.__cantidad):
            self.__alumnos[i].mostrarDatosAlumno()
    def cargar(self,nomArch="alumnos.csv"):
    	archivo=open(nomArch)
    	reader=csv.reader(archivo,delimiter=";")
    	for fila in reader:
    		self.agregarAlumno(Alumno(fila[0],fila[1],fila[2],fila[3],fila[4]))
    def buscarAlumno(self,dni):
    	flag=False
    	i=0
    	while not flag and i<self.__cantidad:
    		flag=self.__alumnos[i].verificarDni(dni)
    		i+=1
    	return flag
    def obtenerIndiceAlumno(self,dni):
    	flag=False
    	i=0
    	while not flag and i<self.__cantidad:
    		flag=self.__alumnos[i].verificarDni(dni)
    		i+=1
    	if flag:
    		i-=1
    	else:
    		i=False
    	return i
    def ordenarXanio(self):
	    cont=0
	    ordenado=False
	    tamano=self.__cantidad
	    comparaciones=tamano
	    for i in range(0,tamano):
	        if ordenado==True:
	            break
	        for j in range(0,comparaciones-1):
	            ordenado=True
	            cont=cont+1
	            if self.__alumnos[j].anio()>self.__alumnos[j+1].anio():
	                ordenado=False
	                aux=self.__alumnos[j]
	                self.__alumnos[j]=self.__alumnos[j+1]
	                self.__alumnos[j+1]=aux
	        comparaciones=comparaciones-1
	    return
    def ordenarXnombres(self):
	    cont=0
	    ordenado=False
	    tamano=self.__cantidad
	    comparaciones=tamano
	    for i in range(0,tamano):
	        if ordenado==True:
	            break
	        for j in range(0,comparaciones-1):
	            ordenado=True
	            cont=cont+1
	            if self.__alumnos[j].nombre()>self.__alumnos[j+1].nombre() and self.__alumnos[j].anio()==self.__alumnos[j+1].anio():
	                ordenado=False
	                aux=self.__alumnos[j]
	                self.__alumnos[j]=self.__alumnos[j+1]
	                self.__alumnos[j+1]=aux
	        comparaciones=comparaciones-1
	    return
    def ordenars(self):
    	self.ordenarXanio()
    	self.ordenarXnombres()
























    # def calcularDistanciasP0(self, unPunto):
    #     for i in range(self.__cantidad):
    #         distancia = unPunto.distanciaEuclidea(self.__alumnos[i])
    #         print('Distancia del punto {} al punto {} es {}'.format(unPunto, self.__alumnos[i], distancia))
    # def testArregloPuntos(self):
    #     p1 = Punto(4, 5)
    #     p2 = Punto(3, 4)
    #     p3 = Punto(-9, 5)
    #     p4 = Punto(3, 2)
    #     p5 = Punto(1, 7)
    #     self.agregarPunto(p1)
    #     self.agregarPunto(p2)
    #     self.agregarPunto(p3)
    #     self.agregarPunto(p4)
    #     self.agregarPunto(p5)

# if __name__ == '__main__':
#     arregloPuntos = ArregloNumPy(3,10)
#     arregloPuntos.testArregloPuntos()
#     punto0 = arregloPuntos.getUnPunto(0)
#     arregloPuntos.calcularDistanciasP0(punto0)
#     arregloPuntos.mostrarPuntos()