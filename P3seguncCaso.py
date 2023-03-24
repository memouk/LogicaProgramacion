import math
from Generales.captura import clsGenerales

class segunCaso:
    og=clsGenerales()


    def __init__(self) -> None:
        self.__Iniciar__()

    def __Iniciar__(self):
        self.og.Mensaje("X = " + str(self.__hallarX__()))

    def __hallarX__(self):
        H=self.og.leerEnteroPosMy0("ingrese l valor de H")
        a=self.og.leerReal("ingrese el valor de alfa")
        b=self.og.leerReal("ingrese el valor de beta")
        
        if (H == 10 or H == 20 or H == 30 or H == 40 ):
            t= self.__valorT__(H)
            x= 2*t*math.sin(a+b)*math.cos(a-b)

        else:
            x=0
        return x
    
    def __valorT__(self, vH):
        n=self.og.leerRealPosMy0("ingrese el valor de n")
        if vH==10:
            return n/2+1
        elif vH==20:
            return n+2
        elif vH==30:
            return (n+2)/(n+1)
        else:
            return 3*n/2
        
punk=segunCaso()


        