import json
from vehiculo import Vehiculo
from nuevo import Nuevo
from usado import Usado
from nodo import Nodo
from listaEnlazada import Lista
from ObjectEncoder import ObjectEncoder




if __name__ == '__main__':
	vehiculos=Lista()
	vehiculos.cargar()
	print("1) Insertar un vehículo en la colección en una posición determinada.")
	print("2) Agregar un vehículo a la colección.")
	print("3) Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
	print("4) Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
	print("5) Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
	print("6) Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
	print("7) Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”")
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				pos=int(input("Ingrese posicion: "))
				nuevo=vehiculos.leerVehiculo()
				vehiculos.Insertar(nuevo,pos)
			case 2:
				nuevo=vehiculos.leerVehiculo()
				vehiculos.Agregar(nuevo)
			case 3:
				pos=int(input("Ingrese posicion: "))
				vehiculos.mostrarClaseElemento(pos)
			case 4:
				pat=input("Ingrese patente: ")
				vehiculos.modificarPrecioUsado(pat)
			case 5:
				vehiculos.vehiculoMasBarato()
			case 6:
				vehiculos.todos_modelo_precio_puertas()
			case 7:
				encoder=ObjectEncoder()
				encoder.guardarJSONArchivo(vehiculos.toJSON(),"vehiculos.json")
