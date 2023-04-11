from Generales.captura import clsGenerales

class servPublic:
    og=clsGenerales()
    
    def __init__(self) -> None:
        self.__facturar()

    def __vrKw__(self,est:int)->int:
       ''' if est <=2:
            return 170
        elif est<=4:
            return 195
        else:
            return 220'''
       return 170 if est<=2 else 195 if est<=4 else 220
    
    def __vrM3__(self,est:int)->int:
       return 105 if est<=2 else 130 if est<=4 else 155
    def __vrTel__(self,est:int)->int:
       return 5 if est<=2 else 10 if est<=4 else 15
    def __facturar(self):
       vrDol= self.og.leerRealPosMy0("vr del dolas hoy")
       ctvD=vrDol/100
       kFac=0
       vrTotfac=0
       codInst=self.og.leerEntero("ingrese el codigo de la instalacon  0 vr <=0 para salir")
       self.og.Mensaje("es")
       while codInst>0:
          est=self.og.leerEnteroPosMy0("ingrese el estrato ")
          if est <=6:
            kwh=self.og.leerEnteroPos("canidad de energia")
            kM3=self.og.leerEnteroPos("canidad de agua")
            kMin=self.og.leerEnteroPos("canidad minutos telefonia")
            vrKh=kwh*self.__vrKw__(est)*ctvD
            vrM3=kwh*self.__vrM3__(est)*ctvD
            vrTel=kwh*self.__vrTel__(est)*ctvD
            vrAPag=vrKh+vrM3+vrTel
            rpta="/nCodigo de instalacion: ",codInst,"/nEnergia: ",vrKh,
            "/nAgua:",vrM3,"/nTelefoni: ",vrTel,
            "/nTotal a pagar: ",vrAPag   
            self.og.Mensaje(rpta) 
            codInst=self.og.leerEntero("ingrese el codigo de la instalacon  0 vr <=0 para terminar")
            kFac+=1
            vrTotfac+=vrAPag

          else:
             self.og.Mensaje("estrato no valido reintentar")
        
        self.og.Mensaje("finalizo")
xx=servPublic()