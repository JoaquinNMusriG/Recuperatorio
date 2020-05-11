import numpy as np
import Diario

class ManejadorDiario:
    __cantidad = np.empty(0)

    def __init__(self, cantidadMediciones= 144): #revisar
        self.__cantidad = np.empty(0)

# Agrega un registro diario a la coleccion
    def agregarDiario(self, diario):
        if (diario[0] != ''):
            reg = Diario.Diario(diario[0],float(diario[1]),float(diario[2]))
            self.__cantidad = np.append(self.__cantidad,reg)
        else:
            print('ERROR.')
# Calcula y retorna la mayor temperatura
    def temperaturaMaxima(self):
        max = 0
        for diario in self.__cantidad:
            if (diario.getTemperatura() > max):
                max = diario.getTemperatura()
        return max
# Calcula y retorna la temperatura mínima
    def temperaturaMinima(self):
        min = 50
        for diario in self.__cantidad:
            if (diario.getTemperatura() < min):
                min = diario.getTemperatura()
        return min
   #Calcula la cantidad de minutos de viento  = cantidad de lecturas con viento > 0 multiplicado por 10
    def vientoTotal(self):
       cont = 0
       for diario in self.__cantidad:
           if diario.getViento() > 0:
               cont += 1
       return (cont * 10)
