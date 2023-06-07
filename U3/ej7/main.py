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