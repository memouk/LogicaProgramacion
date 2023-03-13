from Generales.Captura import clsGenerales
class deciDoble2:
    og = clsGenerales()

    def __init__(self):
        self.decidir( )
    def cumplimiento ( self, sumaAB, vrC ):
        if(sumaAB >= vrC * (1-5.5/100)and sumaAB <= vrC *(1+5.5/100)):
            return True
        else:
            return False
    def decidir( self ):
        A = self.og.leerEntero("ingrese el valor de A :")
        B = self.og.leerEntero("ingrese el valor de B :")
        C = self.og.leerEntero("ingrese el valor de C :")
        if  self.cumplimiento ((A+B), C): #A =10 B =20
            self.og.Mensaje("si cumple conmdiciones")
        else:
            self.og.Mensaje("no cumple condiciones")
        self.cumplimiento()
Tocp = deciDoble2()