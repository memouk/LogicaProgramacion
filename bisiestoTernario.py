from Generales.captura import clsGenerales

class ternario:
    og=clsGenerales()


    def __init__(self) -> None:
        self.__Iniciar__()

    def __Iniciar__(self):
        dato=self.og.leerEnteroPos("ingrese el año")
        if self.__esBisiesto__(dato):
            rpta=", si es bisiesto"
        else:
            rpta=", no es bisiesto"
        self.og.Mensaje(str(dato)+rpta)

        rpta= ", si es bisiesto" if self.__esBisiesto__(dato) else ", no es bisiesto"

    def __esBisiesto__(self,year):
        if (year %4 ==0 and year%100 !=0) or year % 400 == 0:
            return True
        else:
            False

xx=ternario()
