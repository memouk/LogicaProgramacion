from Generales.captura import clsGenerales 

class desAnidad:

    og=clsGenerales()
    def __init__(self) -> None:
        M=self.og.leerRealPosMy0("ingrese el descuento de la bolita verde")
        N=self.og.leerRealPosMy0("ingrese el descuento de la bolita amarilla")
        vC=self.og.leerRealPosMy0("ingrese el descuento de la bolita verde")
        ay="ingrese el colord ela bolita"
        colBol=self.og.leerCadena2(ay)
        self.og.Mensaje(self.__Facturar__(M,N,vC,colBol))

    def __Facturar__(self,dVe,dAm,vrPago,coBo):

        vrDscto=self.__hallarDscto__(vrPago,self.__descuento__(coBo,dVe,dAm))
        vrAPag=vrPago-vrDscto
        cad= "\nvalor de la compra: ",vrPago
        cad+="descuento otorgado : ", vrDscto
        cad+="\nValor a pagar",vrAPag
        return cad
    
    


    def __descuento__(self,cB,dV,dA):
        cB=cB.lower()
        if "verde".__eq__(cB):
            return dV
        else:
            if "amarillo".__eq__(cB):
                return dA
            else:
                if "azul".__eq__(cB):
                    return 50
                else:
                    if "rojo".__eq__(cB):
                        return 100
                    else:
                        return 0
                    
    def __hallarDscto__(self,vrCompra,pDscto):
        return vrCompra*pDscto/100
    
memo=desAnidad()    
    
