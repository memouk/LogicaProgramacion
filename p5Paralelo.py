from Generales.captura import *

class p5Paralelo:
    og=clsGenerales()
    ov=clsVectorGral()

    def __init__(self) -> None:
        self.__hallarDatos__()

    def __hallarDatos__(self):
        M = self.og.leerEnteroPosMy0("Ingrese la cantidad de personas: ")  
        vNombre=[None]*M
        vGenero=[None]*M
        vEdad=[None]*M

        for h in range(M):
            vNombre[h]=self.og.leerCadena2("Nombre # "+str(h+1))
            while True:
                gen= self.og.leerCadena2("ingrese el genero (M/F/T/NB) ").lower().strip()                
                if gen != 'f' and gen != 'm' and gen != 't' and gen != 'nb':
                    self.og.Mensaje("error, genero no valido")
                else:
                    break
            vGenero[h]=gen
            vEdad[h]=self.og.leerEnteroPos("Ingrese la edad de "+vNombre[h]+":")
            

       ## self.__mostrarInfo__(vNombre,vGenero,vEdad)
        prom= self.__prom__(vEdad)

        ##self.og.Mensaje("el numero de mujeres y transnon: "+str(self.__puntoA__(vGenero,vEdad,prom)))

        xs=self.__puntoB__(vNombre,vEdad)

    def __mostrarB__(self,xs):
        for i in range(len(xs)):
            rpta += xs[i]+'\n'
        self.og.Mensaje(rpta)   




    def __mostrarInfo__(self,nom,gen,ed):
        rpta="personas ingresadas\n"
        for i in range(len(nom)):
            rpta += nom[i]+'\t'+ gen[i]+'\t'+ str(ed[i])+'\n'
        self.og.Mensaje(rpta)

    def __puntoA__(self,gen,ed,prom):
        k=0
        for i in range(len(ed)):
            if ed[i] < prom and (gen[i]=='t' or gen[i]=='f'):
                k+=1
        if k >0:
            return k
        else:
            return -1  
    def __prom__(self,ed):
        acum=0
        for i in range(len(ed)):
            acum+=ed[i]
        return acum/len(ed)
    

    def __puntoB__(self,nom,ed):
        vrpta =[]
        for i in range(len(ed)):
            if ed[i] < 18:
                vrpta.append(nom[i])
        if len(vrpta):
            return vrpta["Ningun menor en la lista"]
        return vrpta    

xx=p5Paralelo()