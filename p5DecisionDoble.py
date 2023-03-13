from Generales.captura import clsGenerales

class decisionDoble:
    og=clsGenerales()

    def __init__ ( self ):
        print()
        self.hallarPago()

    def hallarPago(self):
         codigo=self.og.leerCadena("ingrese el codigo del empleado")
         nombre=self.og.leerCadena("ingrese el nombre del empleado")
         horasW=self.og.leerEntero("ingrese la cantidad de horas laboradas")
         x=self.og.leerReal("ingrese el valor dela hora normal < 48")
         kDom=self.og.leerEntero("ingrese la cantidad de domicilios")
         vAD=self.og.leerReal("ingrese el valor por domicilio adicional")
         

         #proceso
         if horasW <=48:
              vrHow= horasW *x
         else:
              vrPagNor= 48*x
              hoAd= horasW-48
              vrPadAdi= hoAd * self.valorHora(horasW)
              vrHow= vrPadAdi + vrPagNor

         vrPagDom=self.valorDomic(kDom,vAD)  
         vrTotPag= vrHow *vrPagDom  


         #salida
         rpta="El señor",nombre,"\ncon codigo",codigo
         rpta+="\nel valor horas trabajadas:",vrHow
         rpta+="\nel valor por domicilio:",vrPagDom
         rpta+="\nel valor total a pagar:",vrTotPag,
         self.og.Mensaje("memo")
    
    def valorHora(self,cantH):
        horaAdic=0
        if cantH > 48:
            horaAdic=self.og.leerEntero("ingrese el valor de hora adicional")
        return horaAdic         



    def valorDomic(self,kDom,vrDom): 
           return kDom*vrDom
    
tico=decisionDoble()