from Generales.captura import clsGenerales
import math
#encabezado
#Para el mensaje
#A partir de la clase: messagebox, creamos un objeto llamado: msj
from tkinter import messagebox as msj 

#Para la captura de info
#A partir de la clase: simpledialog, creamos un objeto llamado:  win
from tkinter import simpledialog
win = simpledialog   

#Cuerpo
class clsGenerales:
#Constructor
    def __init__ ( self )
        pass  #para aquellos casos en que la sintaxis requiera una instrucción, pero no queramos que se emplee.

#Base
    def Mensaje ( self, texto ):
        msj.showinfo( title = "Aviso", message = texto )
        # https://recursospython.com/guias-y-manuales/cuadros-de-dialogo-messagebox-en-tkinter/
    #Captura
    def leerEntero ( self, texto ):
        x = win.askinteger ("Captura de dato: Entero", str( texto ) ) 
        #Se puede adicionar, por ejemplo:  minvalue=0, maxvalue=100
        #https://pythonguides.com/python-tkinter-messagebox/
        return x

    def leerReal ( self, texto ):
        x = win.askfloat ("Captura de dato: Real", str( texto )) #, parent = frm )
        return x

    def leerCadena ( self, texto ):
        x = win.askstring ("Captura de dato: Cadena", str( texto )) #, parent = frm )
        return x
    
    def gradosARad(self,x):
        return 180/(math.pi*x)
    
    def radAGrados(self,x):
        return math.pi/(180*x)
    
    def main(self):
        og=clsGenerales()
      #  og.Mensaje("hola Gonorrea")
        grad=og.leerEntero("ingrese los grados")
        rad=og.leerReal("ingrese los radianes")
        rt=str(gradosARad(grad));
        og.Mensaje(grad,"los grados",rt)

memo=clsGenerales()