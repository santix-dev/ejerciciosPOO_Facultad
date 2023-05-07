from conjunto import Conjunto

if __name__ == '__main__':
	a=Conjunto([1,2,3,4])
	b=Conjunto([3,6,9])
	print(a+b)
	c=Conjunto([1,2,3,4])
	d=Conjunto([3,6,9])
	print(c-d)
	distinto1=Conjunto([1,2,3])
	distinto2=Conjunto([1,2,4])
	iguala1=Conjunto([1,2,3])
	if distinto2==distinto1:
		print("Conjuntos iguales")
	else:
		print("Conjuntos distintos")
	if distinto1==iguala1:
		print("Conjuntos iguales")
	else:
		print("Conjuntos distintos")
