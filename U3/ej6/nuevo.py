from vehiculo import Vehiculo

class Nuevo(Vehiculo):
	"""docstring for Nuevo"""
	__marca="Ford"
	def __init__(self, version, modelo,puertas,color,precio_base):
		super().__init__(modelo,puertas,color,precio_base)
		self.__version = version
	def importeVenta(self):
		importe=self._precio_base+self._precio_base*0.1 if self.__version=="base" else self._precio_base+self._precio_base*0.1+self._precio_base*0.02		
		return importe
	def modificarPrecio(self,precio):
		self._precio_base=precio
	def mod_pr_puertas(self):
		print(f"{self.mod_puertas()},importe: {self.importeVenta()}")
	def toJSON(self):
		d = {
			"__class__":self.__class__.__name__,
			"__atributos__":
			{
				"version":self.__version,
				"modelo":self._modelo,
				"puertas":self._puertas,
				"color":self._color,
				"precio_base":self._precio_base
			}

		}
		return d