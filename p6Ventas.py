from Generales.captura import *

class matriz2:
    og= clsGenerales()
    i=0
    j=0
    def principal(self):
        zoVe= [None]*2
        M=self.og.leerEnteroPosMy0("ingrese cantidad de vendedores")
        Z=self.og.leerEnteroPosMy0("ingrese cantidad de zonas")
        ventas=[None]*Z
        nomVend= [None]*M
        for i in range (len(ventas)):
            ventas[i]=[None]*M
        
        for j in range(M):
            nomVend[j]=self.og.leerCadena2("nombre del vendedor")
            for i in range(Z):
                ventas[i][j]=self.og.leerEnteroPos("ventas en zona"+str((i+1)))

      #  self.__menorVend(ventas,Z,M,nomVend)
        zoVe=self.__mejorZonaVend(ventas,Z,M)
        self.og.Mensaje("zona de mayor ventas es: " + str((zoVe[0] + 1)) + " y " +  nomVend[zoVe[i]] + " es el de mayor venta en la zona.")
    
    def __menorVend(self,m,kf,kc,n):
        mnVta=0
        
        tmp=[None]*kc
        nom=""
        for j in range(kc):
            acum=0
            for i in range(kf):
                acum+=m[i][j]
            if j==0:
                mnVta=acum
            else:
                if acum < mnVta:
                    mnVta=acum
            tmp[j]=acum
        for j in range(kc):
            if tmp[j]== mnVta:
                nom += n[j]+","
        self.og.Mensaje("Menos venta"+str(mnVta)+"realizada por: "+ nom)

    def __mejorZonaVend(self,m,kf,kc):
        rpta=[]
        kmy=0
        for i in range(kf):
            acum=0
            for j in range(kc):
                acum += m[i][j]
            if j == 0:
                kmy=acum
                imy=i
            elif acum > kmy:
                kmy=acum
                imy=i   
        rpta.append(imy) # indice la primera zona más vendedora

    #vendedor que mas vendió en dicha zona

        izo = imy
        kmy = m[imy][0]
        imy = 0
        for i in range (1, kf):
            if m[izo][j] > kmy:
                kmy = m[izo][j]
                imy = j
        rpta.append(imy) #1 indice del primer vendedor que más vendió en dicha zona 
        return(rpta)

        

        





xx= matriz2()
xx.principal()