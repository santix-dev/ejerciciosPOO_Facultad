class Email():
	__idCuenta=""
	__dominio=""
	__tdominio=""
	__contrasena=""
	def __init__(self, cuenta="", dom="", tdom="", psw=""):
		self.__idCuenta = cuenta
		self.__dominio = dom
		self.__tdominio = tdom
		self.__contrasena = psw
	def retornaEmail(self):
		email=self.__idCuenta+"@"+self.getDominio()+"."+self.__tdominio
		return email
	def getDominio(self):
		return self.__dominio
	def verifPsw(self,psw):
		return self.__contrasena==psw
	def changePsw(self,oldPsw,newPsw):
		if self.verifPsw(oldPsw):
			self.__contrasena=newPsw
		else:
			print("contraseña incorrecta")
	def crearCuenta(self,cuenta="", psw=""):
		datos=cuenta.split("@")
		dom=datos[1].split(".",1)
		self.__idCuenta=datos[0]
		self.__dominio=dom[0]
		self.__tdominio=dom[1]
		return
	def mostrarDatos(self):
		print(f"[{self.__idCuenta}, {self.__dominio}, {self.__tdominio}, {self.__contrasena}]")
		return


	
