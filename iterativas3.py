from Generales.captura import clsGenerales
#from random import *

# for i in [10,20,30,40]:
#     print(i,end=',')

# for i in range(5):
#     print(i,end=',')

# for i in range(10,20+1):
#     print(i)

# print('')

# for i in range(10,20+1,3):
#     print(i)


#for i in range(5):
#    print(randint(10,20+1))

class iterativas3:
    xx= clsGenerales()
    def __init__(self) -> None:
        self.__hallarDatos__()
    def __vrVen__(self,kv):
        acVtas=0
        for i in range(kv):
            vrVta = self.xx.leerRealPosMy0("Ingrese el vr de la venta"+str(i+1)+":")
        acVtas+=vrVta
        return acVtas

    def __vrPorcComi__(self):
        while(True):
            pcomi= self.xx.leerRealPos("porcentaje extra por comisiones")
            if pcomi <= 5.5:
                return pcomi
            else:
                self.xx.Mensaje("error")
    
    def __vrComi__(self, vtasTot,porc):
        return vtasTot*porc/100
    
    def __hallarDatos__(self):
        totKv=totVtas=totComi=totAPag=0
        nVend= self.xx.leerEnteroPosMy0("ingrese cantidad de vendedores")
        for h in range(1,nVend+1):
            cod=self.xx.leerEnteroPosMy0("ingrese el codigo del vendedor"+str(h)+":")
            salBase= self.xx.leerRealPosMy0("ingrese el salario")
            P=self.__vrPorcComi__()
            kv=self.xx.leerEnteroPos("ingrese cantidad de ventas")
            vrVtasvend=vrComi=0
            if kv > 0:
                vrVtasvend=self.__vrVen__(kv)
                vrComi += self.__vrComi__(vrVtasvend,P)
            vrPag= salBase+vrComi
            rpta= "Codigo: "+str(cod)+",cuanto vendio: "+str(vrVtasvend)+", concepto de comisiones: "+str(vrComi)+", Vr pagar"+str(vrPag)
            self.xx.Mensaje(rpta)

            totKv +=kv
            totVtas+= vrVtasvend
            totComi+=vrComi
            totAPag+=vrPag

            rpta= "deje de chibiar con los totales"
            self.xx.Mensaje(rpta)
memo=iterativas3()