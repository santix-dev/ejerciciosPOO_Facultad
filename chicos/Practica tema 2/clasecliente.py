class Cliente:
    __dni= ""
    __apellido=""
    __nombre=""
    __telefono=""
    __patente=""
    __vehiculo=""
    __estado=""

    def __init__(self, dni="", apellido="", nombre="", telefono="", patente="", vehiculo="", estado=""):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__telefono=telefono
        self.__patente=patente
        self.__vehiculo=vehiculo
        self.__estado=estado

    def __str__(self):
        return("{} {} {} {} {} {} {}".format(self.__dni,self.__apellido, self.__nombre, self.__telefono, self.__patente, self.__vehiculo, self.__estado))
        
    def getdni(self):
        return self.__dni
    
    def getAyN(self):
        return self.__apellido + self.__nombre
    
    def getpatente(self):
        return self.__patente
    
    def getvehiculo(self):
        return self.__vehiculo
    
    def gettelefono(self):
        return self.__telefono
    
    def __eq__(self, otro):
        a= self.__dni + self.getAyN() + self.__telefono
        b=otro.__dni + otro.getAyN() + otro.__telefono
        return a == b
    def verifPatente(self,pat):
        return pat==self.__patente
    def altEstadoTermnado(self):
        self.__estado="t"