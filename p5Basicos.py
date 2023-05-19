from Generales.captura import clsGenerales
from Generales.captura import clsVectorGral

class p5Basicos:
    og=clsGenerales()
    ov=clsVectorGral()

    def __init__(self) -> None:
        x=self.og.leerEnteroPosMy0("ingrese la cantidad de numeros reales al leer")
        Nros= [None]*x
        Nros=self.ov.llenarRealesNeg(Nros,"ingrese el primer numero")
        self.ov.mostrarDatos(Nros,"los valores que ingreso fue")
        self.__realizarProc__(Nros)

        
    
    def __realizarProc__(self,v):
        t=len(v)
        self.og.Mensaje("suma :"+str(self.__sumaVect__(v)))
        while True:
            indPos=self.og.leerEnteroPos("ingrese pos entre 0 y "+str(t-1))


    def __sumaVect__(self,v):

        acum=0
        for i in range(len(v)):
            acum +=v[i]
        return acum

    def __vrPot__(self,v,pos):
        return v[pos]**2

memo=p5Basicos()