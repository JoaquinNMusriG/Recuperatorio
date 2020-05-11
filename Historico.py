class Historico:
    __fecha = None
    __tempMaxima = 60
    __tempMinima = -30
    __vientoCantidad = 0

    def __init__(self,fecha, tempMaxima, tempMinima, vientoCantidad):
        self.__fecha = fecha
        self.__tempMaxima = tempMaxima
        self.__tempMinima = tempMinima
        self.__vientoCantidad = vientoCantidad

    def getFecha(self):
        return self.__fecha

    def __str__(self):
        return 'fecha= {}, tempMax= {:.2f}, tempMin= {:.2f}, viento= {}'.format(self.__fecha, self.__tempMaxima, self.__tempMinima, self.__vientoCantidad)

#No veo forma de poder comparar las temperaturas de los registros historicos
#si no existen los metodos get de las temp max y min. Para poder resolver el último inciso
#voy a agregar estos métodos aunque sepa q no se deben agregar métodos

    def gettempMax(self):
        return self.__tempMaxima

    def gettempMin(self):
        return self.__tempMinima

    def __gt__(self, otro):
        resultado = False
        if (self.gettempMax() > otro.gettempMax()) & (self.gettempMin() > otro.gettempMin()):
            resultado = True
        return resultado
