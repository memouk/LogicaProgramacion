from Generales.captura import *

class paises:

    og=clsGenerales()
    ov=clsVectorGral()
    om=clsMatrizGral()


    def __init__(self) -> None:
        N=self.og.leerEnteroPosMy0("Cuantos paises desea ingresar")#kc
        M=self.og.leerEnteroPosMy0("Cuantas ciudades va ingresar por pais")#kf

        paises= [None]*N
        Ciudades=[None]*M
        Poblac=[None]*M
        
        for i in range(len(Ciudades)):
           Ciudades[i]=[None]*M
           Poblac[i]=[None]*M
           #paises[i]=self.og.leerCadena2("ingrese el pais "+str(i+1))
        for j in range(N):
            paises[j]=self.og.leerCadena2("ingrese el pais "+str(j+1))               
            for i in range(M):
                Ciudades[i][j]=self.og.leerCadena2("ingrese la ciudad # "+str(i+1)+"del pais = "+paises[j])
                Poblac[i][j]=self.og.leerRealPosMy0("ingrese la poblacion de la ciudad #"+str(i+1)+"del pais "+paises[j])
        #paises=self.ov.llenarCadenas2(paises,"ingrese paises")
        #Ciudades=self.om.llenarCadenas2(Ciudades,"ingrese la ciudad")
        # print(paises)
        # print("\n")
        # print(Ciudades)
        # print("\n")
        # print(Poblac)
        #self.om.mostrarDatosFil(Ciudades,"las cuidades ingresada")
        #self.om.mostrarDatosFil(Poblac,"las poblaciones con")
        #self.__puntoA(paises,Ciudades,Poblac)
        self.__puntoB(paises,Ciudades,Poblac)

    def __puntoA(self,pa,ciu,po):
        myp=0
        for j in range(len(pa)):
            for i in range(len(ciu)):
                if myp < po[i][j]:
                    myp=po[i][j]
                    mypC=ciu[i][j]
                    mypP=pa[j]
        print(myp,mypC,mypP)
    def __puntoB(self,pa,ciu,po):
        myp=0
        
        for j in range(len(pa)):
            acum=0
            for i in range(len(ciu)):
                acum +=acum+(po[i][j])
            if acum > myp:
                myp=acum
        print(myp)




xx=paises()
