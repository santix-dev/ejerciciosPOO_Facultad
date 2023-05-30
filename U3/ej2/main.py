import csv
import precios as p
from helado import Helado
from sabor import Sabor
from manejadorhelados import ManejadorHelados
from manejadorsabores import ManejadorSabores



if __name__ == '__main__':
	sabores=ManejadorSabores()
	sabores.cargar()
	helados=ManejadorHelados()
	print(f"1) Vender helado\n2) Mostrar los 5 sabores mas vendidos") 	
	print(f"3) Ver total de gramos vendidos por sabor")
	print(f"4) Mostrar todos los sabores vendidos en un tipo de helado")
	print(f"5) Determinar importe recaudado por cada tipo de helado")
	opc=int(input())
	while opc!=0:
		match opc:
			case 1:
				helados.venderHelado(sabores)
			case 2:
				helados.saboresMasVendidos(sabores)
			case 3:
				sabor=int(input("Ingrese id de sabor: "))
				helados.gramosXsabor(sabor,sabores)
			case 4:
				for k,v in p.tHelado.items():
					print(f"{k}) {v[0]:5}gr ${v[1]:5>}")
				tipo=input("Ingrese un tipo de heladinio: ")
				gramos=p.tHelado[tipo][0]
				helados.saboresXtipoHelado(gramos,sabores)


				pass
		print(f"1) Vender helado\n2) Mostrar los 5 sabores mas vendidos") 	
		print(f"3) Ver total de gramos vendidos por sabor")
		print(f"4) Mostrar todos los sabores vendidos en un tipo de helado")
		print(f"5) Determinar importe recaudado por cada tipo de helado")
		opc=int(input())


		