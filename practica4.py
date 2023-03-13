from Generales.captura import clsGenerales as og


class desicionSimple1:
    

    def __init__ ( self ):
        self.hallarValor()


    def FnX(self,v1,v2):
        x=og.leerReal(self,"ingrese el valor de x")
        fx=0
        if  x > v1*v2:
            fx= (3*v1**2)/(2*v2)
        return fx
    def hallarValor(self):
        
        a=og.leerReal(self,"ingrese e valor de a:")
        b=og.leerReal(self,"ingrese e valor de b:")

        x=self.FnX(a,b)
        og.Mensaje(self,"fx ="+ str(x))

ms= desicionSimple1()
