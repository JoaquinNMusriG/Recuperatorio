import Historico

class ManejadorHistorico:
    __datos = []
    def __init(self):
        self.__datos = []

	# agrega un registro histórico a la coleccion
    def agregarHistorico(self, resumen):
        if (resumen[0] != '') & (resumen[3].isdigit()):
            res = Historico.Historico(resumen[0],float(resumen[1]),float(resumen[2]),int(resumen[3]))
            self.__datos.append(res)
        else:
            print('ERROR.')

	# determina los días más calurosos
    def masCaluroso(self, hoy):
        Hoy = Historico.Historico(hoy[0],float(hoy[1]),float(hoy[2]),int(hoy[3]))
        for registro in self.__datos:
            if (registro > Hoy):
                print(registro)
