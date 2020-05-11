class Diario:
    __hora = None
    __temperatura = 100
    __viento= 0

    def __init__(self,hora,temperatura, viento):
        self.__hora = hora
        self.__temperatura = temperatura
        self.__viento = viento

    def getTemperatura(self):
        return self.__temperatura

    def getViento(self):
        return self.__viento
