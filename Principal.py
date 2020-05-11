from ManejadorDiario import ManejadorDiario
from ManejadorHistorico import ManejadorHistorico
import csv

if __name__ == "__main__":
    archivo = open('diario.csv')
    reader = csv.reader(archivo, delimiter = ';')
    ArregloDiario = ManejadorDiario(144)
    for lista in reader:
        ArregloDiario.agregarDiario(lista)
    archivo.close()

    archivo = open('historico.csv')
    reader = csv.reader(archivo, delimiter = ';')
    ListaHistorico = ManejadorHistorico()
    for lista in reader:
        ListaHistorico.agregarHistorico(lista)
    archivo.close()

    amplT = ArregloDiario.temperaturaMaxima() - ArregloDiario.temperaturaMinima()
    print ('La amplitud térmica del dia de hoy es: {:.2f}'.format(amplT))

    resumen = ['11/05/20',ArregloDiario.temperaturaMaxima(),ArregloDiario.temperaturaMinima(),str(ArregloDiario.vientoTotal())]
    ListaHistorico.agregarHistorico(resumen)

    print('La siguiente lista corresponde a los registros históricos más calurosos que el actual:')
    ListaHistorico.masCaluroso(resumen)
