import unittest
from nuevo import Nuevo
from usado import Usado
from listaEnlazada import Lista
import random
class Test_vehiculos(unittest.TestCase):
	"""docstring for Test_vehiculos"""
	__lista=Lista()
	__vehic=Usado("zzz999","2012","100000","chevrolet","corsa","5","rojo","1000000")
	def setUp(self):
		__lista.cargar()
	def test_agregar(self):
		self.assertNotIn(vehic,self.__lista)
		self.__lista.agregar(vehic)
		self.assertIn(vehic,self.__lista)
	def test_insertar_primero(self):
		pos=0
		self.__lista.insertar(self.__vehic,pos)
		self.assertEqual(pos,self.__lista.posicion(self.__vehic.patente()))
	def test_insertar_medio(self):
		pos=3
		self.__lista.insertar(self.__vehic,pos)
		self.assertEqual(pos,self.__lista.posicion(self.__vehic.patente()))
	def test_posicion(self):
		pos=random.randint(0,5)
		vehic=self.__lista.vehiculo(pos)
		self.assertEqual(self.__lista.posicion(vehic,pos))
	def test_precio(self):
		precio=random.randint(400,1500)
		self.__lista.agregar(vehic)
		pat=vehic.patente()
		self.__lista.modificarPrecioUsado(pat,precio)
		self.assertEqual(self.__lista.vehiculo().precio(),precio)
