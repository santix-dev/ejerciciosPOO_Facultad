import precios as p
from helado import Helado
from sabor import Sabor
from manejadorsabores import ManejadorSabores
class ManejadorHelados(object):
	"""docstring for ManejadorHelados"""
	def __init__(self):
		self.__lista = []
	def venderHelado(self,manSabores):
		"""must receive sabores controller"""
		for k,v in p.tHelado.items():
			print(f"{k}) {v[0]:5}gr ${v[1]:5>}")
		opc=input("Ingrese tipo de helado: ")
		gramos=p.tHelado[opc][0]
		precio=p.tHelado[opc][1]
		sabores=int(input("Cantidad de sabores: "))
		while 1>int(sabores) or 4<int(sabores):
			sabores=int(input("Seben ser entre 1 y 4 sabores: "))
		self.__lista.append(Helado(gramos,precio))
		self.agregarSabores(sabores,manSabores)
	def agregarSabores(self,n,sabores):
		sabores.mostrarSabores()
		for i in range(n):
			sabor=int(input(f"Ingrese sabor {i+1}: "))
			sabor=sabores.verifSabor(sabor)
			self.__lista[-1].agregarSabor(sabores.sabor(sabor))
	def saboresMasVendidos(self,manSabores):
		contSab=[0]*manSabores.len()
		dicSabores={}
		for helado in self.__lista:
			helado.contarSabores(contSab)
		i=0
		# print(contSab)
		print("Sabores mas vendidos: ")
		while i < manSabores.len() and i<5:
			if max(contSab)!=0:
				mayor=contSab.index(max(contSab))
				print("posicion mayor (id en teoria): ",mayor,manSabores.sabor(mayor+1))
				print(f"{i+1}) {manSabores.sabor(mayor+1)}, pedido {contSab[mayor]} veces")
				contSab[mayor]=0
				i+=1
			else:
				i=5
	def gramosXsabor(self,id,sabores):
		total=0
		for helado in self.__lista:
			if helado.tiene(id):
				gr=helado.gramos()
				cant=helado.cantSabores()
				total+=gr/cant
		print(f"Se vendio un estimado de {total} gramos de el helado {sabores.sabor(id)}")
	def saboresXtipoHelado(self,gramos,sabores):
		lista_ids=[]
		for helado in self.__lista:
			if helado.gramos()==gramos:
				helado.obtenerIDs(lista_ids)
		print(f"Sabores vendidos en helados de {gramos}gr")
		for idSabor in lista_ids:
			print(sabores.sabor(idSabor))
	def importeRecaudado(self):
		dic_gramos={"100":0,"150":1,"250":2,"500":3,"1000":4}
		lista_acum=[0]*5
		for helado in self.__lista:
			lista_acum[dic_gramos[helado.gramos()]]+=helado.precio()
		for i in range(len(lista)):
			print(f"Total Recaudado por helados de {p.tHelado[str(i+1)]}: {lista_acum[i]}")







if __name__ == '__main__':
	sel=ManejadorHelados()
	sabores=ManejadorSabores()
	sabores.cargar()
	sel.venderHelado(sabores)
	sel.venderHelado(sabores)
	sel.venderHelado(sabores)
	sel.saboresMasVendidos(sabores)
