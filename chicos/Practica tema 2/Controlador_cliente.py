from clasecliente import Cliente
import csv
from Controlador_reparacion import Manejador_reparacion

class Manejador_Cliente:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo= open("clientes.csv")
        reader= csv.reader(archivo, delimiter=";")
        
        for fila in reader:
            crear=Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            self.__lista.append(crear)
        archivo.close()
# Leer un Dni de un cliente por teclado en informar los datos del cliente y todas las 
# reparaciones hechas al vehículo siguiendo el siguiente formato:


# Determinar el o los clientes que le hacen servicio a más de un vehículo, mostrando dni, 
# nombre, apellido, teléfono, patente y vehículo 
    def informadatos(self, dni,reparacion):
        i=0
        ban=False

        while(i<len(self.__lista)) & (ban==False):
            if self.__lista[i].getdni() == str(dni):
                ban=True
                # i= self.__lista[i]
            else:
                i+=1
        if ban == True:
            print(f"DNI:{self.__lista[i].getdni() :<20} Apellidos y nombre:{self.__lista[i].getAyN()} \n Patente:{self.__lista[i].getpatente() :<20} Vehiculo:{self.__lista[i].getvehiculo()}")
            patente=self.__lista[i].getpatente()
            # rep=reparacion.getvehiculo(patente)
            reparacion.mostrarReparaciones(patente)
            print(f"Reparacion:{rep.getreparacion():<10} Precio repuesto:{rep.getpreciorepues():<10} Mano de obra:{rep.get_manoobra():<10} Subtotal:{rep.subtotal()}")

    def mostrarReparaciones(self,pat):# en manejador reparacion
        total=0.0
        for rep in self.lista:
            if rep.coincide(pat):
                print(rep)
                total+=rep.subtotal()
        print("total: ",total)

    def cambiarestado(self, patente, reparacion:Manejador_reparacion):
        i=-1
        flag=False
        while not flag and i<len(self.lista):
            i+=1
            flag=lista[i].verifPatente(patente)
        if flag:
            lista[i].altEstadoTermnado()
            print("{} {} {} {}".format(self.__lista.getAyN(), self.__lista().gettelefono(), self.__lista.getvehiculo(),))

    def sinfinalizar(self, reparacion:Manejador_reparacion):
        for i in range(len(self.__lista)):
            if reparacion.getvehiculo(self.__lista[i].getpatente()).getestado() == "P":
                print(f"{self.__lista[i].getAyN():<20} {self.__lista[i].gettelefono()} \n {self.__lista[i].getpatente():<20} {self.__lista[i].getvehiculo()}\n {reparacion.getvehiculo(self.__lista[i].getpatente()).getreparacion()}" )

    def comparar(self):
        a=self.__lista[0]
        for i in range(len(self.__lista)):
            if a == self.__lista[i+1]:
                a=self.__lista[i+1]
                print("{} {} {} {} {}".format(self.__lista[i].getdni(), self.__lista[i].getAyN(), self.__lista[i].gettelefono(), self.__lista[i].getpatente(), self.__lista[i].getvehiculo()))



