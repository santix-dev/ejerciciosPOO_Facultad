class Reparacion:
    __patente= ""
    __reparacion=""
    __precio_repuesto=0
    __costo_manoobra=0
    __estado=""

    def __init__(self, patente="", reparacion="", precio_repuesto=0, mano_obra="", estado=""):
        self.__patente=patente
        self.__reparacion=reparacion
        self.__precio_repuesto=precio_repuesto
        self.__costo_manoobra=mano_obra
        self.__estado= estado

    def __str__(self):
        return("{} {} {} {} {}".format(self.__patente,self.__reparacion, self.__precio_repuesto, self.__costo_manoobra, self.__estado))
    
    def getreparacion(self):
        return self.__reparacion
    
    def getpatente(self):
        return self.__patente
    
    def getpreciorepues(self):
        return self.__precio_repuesto
    
    def get_manoobra(self):
        return self.__costo_manoobra
    
    def getestado(self):
        return self.__estado

    def subtotal(self):
        return self.__precio_repuesto + self.__costo_manoobra
    #def 