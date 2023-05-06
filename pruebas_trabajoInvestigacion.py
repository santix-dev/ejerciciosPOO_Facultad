class Alumno():
	__nombre=""
	__apellido=""
	__dni=0
	__promedio=0.0
	def __init__(self,nom="",ape="",dni=0,prom=0.0):
		self.__nombre=nom
		self.__apellido=ape
		self.__dni=dni
		self.__promedio=prom
	def __str__(self):
		return f"Nombre: {self.__nombre}   Apellido: {self.__apellido}   DNI: {self.__dni}   Promedio: {self.__promedio}"

alumno1 = Alumno("Santiago", "Gimenez", 44123456, 8.0)
alumno2 = Alumno("Marcos", "Molina", 44654321, 8.5)
lista=[alumno1,alumno2]

print(lista[1])
print(lista[0])
#------------------------
alumno0 = Alumno("Juan", "Juarez", 42111333, 9.2)
lista.append(alumno0)
for objeto in lista:
	print(objeto)
#------------------------
print(f"Indice de alumno1: {lista.index(alumno1)}")
print(f"Indice de alumno2: {lista.index(alumno2)}")
print(f"Indice de alumno0: {lista.index(alumno0)}")
lista.pop()
for objeto in lista:
	print(objeto)
lista.pop(0)
for objeto in lista:
	print(objeto)
	print(lista.index(objeto))
lista.insert(0,alumno0)
lista.insert(1,alumno1)
for objeto in lista:
	print(objeto)
	print(lista.index(objeto))
lista.clear()
print(lista)
lista.append(alumno0)
for objeto in lista:
	print(objeto)
del lista
print(lista)