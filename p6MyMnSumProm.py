from Generales.captura import *

class p6MyMnSumProm:
    og= clsGenerales()
    om= clsMatrizGral()

    def __init__(self) -> None:
        self.__principal()

    def __principal(self):
        N= self.og.leerEnteroPosMy0("ingrese tamaño de la matriz")
        #Datos = [[None]*N]*N
        Datos = [None]*N
        for i in range(len(Datos)):
             Datos[i]=[None]*N
        Datos = self.om.llenarReales(Datos,"ingrese valor Real")
        self.om.mostrarDatosFil(Datos,"valores Reales po fila")
        my= self.__Mayor(Datos)
        mn=self.__Menor(Datos)

        self.og.Mensaje("el mayo es : "+str(my)+"el menor es "+str(mn))

        self.__sumasPromFil(Datos)
        self.__sumasPromCol(Datos)

    def __Mayor(self,m):
        nro=m[0][0]
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] > nro:
                    nro = m[i][j]
        return nro
    
    def __Menor(self,m):
        nro=m[0][0]
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] < nro:
                    nro = m[i][j]
        return nro
    
    def __sumasPromFil(self,m):
        out= 'sumas y promedio  por filas\n'
        for i in range(len(m)):
            acum=0
            for j in range(len(m[0])):
                acum += m[i][j]
            out += 'Fila: '+str(i)+'suma'+str(acum)+'promedio'+str((acum/len(m[0])))
        self.og.Mensaje(out)



    def __sumasPromCol(self,m):
        out= 'sumas y promedio  por filas\n'
        for j in range(len(m[i])):
            acum=0
            for i in range(len(m)):
                acum += m[i][j]
            out += 'clumna: '+str(j)+'suma'+str(acum)+'promedio'+str((acum/len(m)))
        self.og.Mensaje(out)
        

xx= p6MyMnSumProm()