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