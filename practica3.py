from Generales.captura import clsGenerales
import math

class cuerpo:
    def gradosARad(x):
        return 180/(math.pi*x)
    
    def radAGrados(x):
        return math.pi/(180*x)
    
    def main():
        og=clsGenerales()
      #  og.Mensaje("hola Gonorrea")
        grad=og.leerEntero("ingrese los grados")
        rad=og.leerReal("ingrese los radianes")
        rt=str(gradosARad(grad));
        og.Mensaje(grad,"los grados",rt)
        
    

    main()


