class Conjunto():
	__conjunto=[]
	def __init__(self,lista):
		self.__conjunto=lista
	def __add__(self,other):
		if isinstance(other,Conjunto):
			for i in other.__conjunto:
				if not i in self.__conjunto:
					self.__conjunto.append(i)
		# esta solucion no era apta cuando habian elementos repetidos
		# 	self.__conjunto.extend(other.__conjunto)
		if isinstance(other,int):
			self.__conjunto.append(other)
		return self
	def __radd__(self,other):
		if isinstance(other,int):
			self.__conjunto.append(other)
		return self
	def __str__(self):
		return f"{self.__conjunto}"
	def __sub__(self,other):
		if isinstance(other,Conjunto):
			for i in other.__conjunto:
				if i in self.__conjunto:
					self.__conjunto.pop(self.__conjunto.index(i))
		elif isinstance(other,int):
			if other in self.__conjunto:
				self.__conjunto.pop(self.__conjunto.index(other))
		return self
	def __rsub__(self,other):
		if isinstance(other,int):
			if other in self.__conjunto:
				self.__conjunto.pop(self.__conjunto.index(other))
		return self
	def __eq__(self,other):
		if isinstance(other,Conjunto):
			if len(other.__conjunto)==len(self.__conjunto):
				i=0
				flag=True
				while flag and i<len(self.__conjunto):
					if not(other.__conjunto[i] in self.__conjunto):
						flag=False
					i+=1
			else:
				flag=False
		else:
			flag=False
		return flag