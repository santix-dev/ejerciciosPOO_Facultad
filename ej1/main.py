import csv
from Email import Email
def mostrarMenu():
	print("""
		1) Cambiar contraseña
		2) Crear cuenta
		3) Leer archivo
		4) Ver cuentas con un dominio
		0) Salir
	""")
def crearCuenta(cuenta="", psw=""):
	datos=cuenta.split("@")
	dom=datos[1].split(".",1)
	return Email(datos[0],dom[0],dom[1],psw)
if __name__ == "__main__":
	nom=input("Ingrese nombre: ")
	mail=input("Ingrese mail: ")
	print(f"estimado {nom} te enviaremos tus mensajes a la direccion de correo {mail}")
	cuenta=Email(mail)
	cuentas=[]
	mostrarMenu()
	opc=int(input(""))
	while opc!=0:
		match opc:
			case 1:
				oldPsw=input("Ingrese la contraseña actual: ")
				if cuenta.verifPsw(oldPsw):
					newPsw=input("Ingrese la contraseña nueva: ")
					cuenta.changePsw(oldPsw,newPsw)
			case 2:
				mail=input("Ingrese mail: ")
				cuenta2=Email()
				cuenta2.crearCuenta(mail)
			case 3:
				archivo=open("correos.csv")
				reader=csv.reader(archivo,delimiter=",")
				for fila in reader:
					if ('@' in fila[0] and '.com' in fila[0].split("@")[1]):
						cuentas.append(crearCuenta(fila[0]))
					else:
						print(f"cuenta no valida: {fila[0]}")
				for correo in cuentas:
					correo.mostrarDatos()
			case 4:
				dom=input("Ingrese un dominio: ")
				cont=0
				archivo=open("correos.csv")
				reader=csv.reader(archivo,delimiter=",")
				for fila in reader:
					if dom in fila[0]:
						cont+=1
				print(f"hay {cont} cuentas con dominio {dom}")
			case _:
				print("Se salió") 
		mostrarMenu()
		opc=int(input(""))