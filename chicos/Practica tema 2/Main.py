from Controlador_reparacion import Manejador_reparacion
from Controlador_cliente import Manejador_Cliente

if __name__ == "__main__":
    reparacion= Manejador_reparacion()
    reparacion.carga()
    cliente=Manejador_Cliente()
    cliente.carga()

    print("---Menu de opciones---")
    print("1:Informar los datos del cliente y todas las reparaciones hechas al vehículo")
    print("2")
    print("3")

    op=input("ingrese opcion de menu")
    while op != "0":
        if op=="1":
            dni=input("ingrese dni para buscar datos del cliente:")
            cliente.informadatos(dni,reparacion)
        elif op=="2":
            # Leer una patente por teclado, determinar si todas las reparaciones están terminadas, 
            # en caso afirmativo, cambiar el estado en el Cliente, y mostrar nombre y apellido del 
            # cliente, el teléfono, el vehículo y el total a pagar.
            paten=input("ingresar numero de patente")
            falg=reparacion.verifReparaciones(paten)
            if flag:
                cliente.cambiarestado(patente)
        elif op=="3":
            cliente.sinfinalizar(reparacion)
        elif op=="4":
            cliente.comparar()
        print("---Menu de opciones---")
        print("1:Informar los datos del cliente y todas las reparaciones hechas al vehículo")
        print("2")
        print("3")

        op=input("ingrese opcion de menu")
