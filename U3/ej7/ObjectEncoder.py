import json
from pathlib import Path
from apoyo import Apoyo
from docente import Docente
from docente_investigador import Doc_Inv
from investigador import Investigador
from lista import ListaEnlazada
from nodo import Nodo
from personal import Personal
#from ManejadorPersonal import ManejadorPersonal
from lista import ListaEnlazada
class ObjectEncoder(object):
	def decodificarDiccionario(self, d):
		if '__class__' not in d:
			return d
		else:
			class_name=d['__class__'] # nombre de la clase manejador
			class_=eval(class_name)   # class ahora es el constructor de la clase manejador

			if class_name=='ListaEnlazada':
				lista_personal=d['personal'] # lista de objetos
				unPersonal = lista_personal[0] # uno de los objetos de la lista
				manejador=class_()
				for i in range(len(lista_personal)):
					unPersonal=lista_personal[i]           # en cada iteracion sera uno de los objetos almacenados, teiene
					                                       # __class__ y __atributos__
					class_name=unPersonal.pop('__class__') # obtengo el nombre de la clase de ese objeto
					class_=eval(class_name)                # obtengo el constructor con eval
					atributos=unPersonal['__atributos__']      # saco los atributos
					#print(atributos,i)
					objetoPersonal=class_(**atributos)	   # creo una instancia con class_(en cada iteracion se convierte 
					manejador.agregar(objetoPersonal)# en el constructor correspondiente al objeto almacenado) y le
					                                      # envio los atributos como diccionario, para funcionar deben 
					                                       # tener el mismo nombre de variable en el archivo json y en 
					                                       # el constructor
					
			return manejador
	def guardarJSONArchivo(self, diccionario, archivo="personal.json"):
		with open(archivo,"w") as destino:
			json.dump(diccionario, destino, indent=4)
			destino.close()
	def leerJSONArchivo(self,archivo="personal.json"):
		with open(archivo) as fuente:
			diccionario=json.load(fuente)
			fuente.close()
			return diccionario
	def convertirTextoADiccionario(self, texto):
		return json.loads(texto)