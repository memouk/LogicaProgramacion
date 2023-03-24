#Para mensaje
from tkinter import messagebox as msj
#Para captura
from tkinter import simpledialog #as win
from tkinter import *
frm = Tk( )
win = simpledialog
t = "350x150"  #alto y ancho
frm.title ( "Captura de datos" )
frm.geometry ( t )
frm.resizable ( 0,0 )  #ancho, alto por default (1.1) =resizable ambos
frm.config ( bg = "light gray" ) 
#https://cafecito.app/programaciondesde0/post/tabla-de-colores-disponibles-en-tkinter-python-hNdzvBSqM


class clsGenerales:
    #Constructor
    def __init__ ( self ) -> None:  #Constructor vacío
        pass  #para aquellos casos en que la sintaxis requiera una instrucción, pero no queramos que se emplee.

#Base
    def leerEnteroPos(self,texto):
        x=win.askinteger("Captura de dato: Entero positivo >=0",str(texto))
        if x<0:
            self.Mensaje("Valor no valido debe ser mayor o  igual a 0")
            return self.leerEnteroPos(texto)
        return x
    def leerEnteroPosMy0(self,texto):
        x=win.askinteger("Captura de dato: Entero positivo >0",str(texto))
        if x<=0:
            self.Mensaje("Valor no valido debe ser mayor a 0")
            return self.leerEnteroPosMy0(texto)
        return x
    def leerEnteroNeg(self,texto):
        x=win.askinteger("Captura de dato: Entero positivo >0",str(texto))
        if x>=0:
            self.Mensaje("Valor no valido debe ser menor o igual a 0")
            return self.leerEnteroNeg(texto)
        return x
    def leerRealPos(self,texto):
        x=win.askfloat("Captura de dato: Entero positivo >0",str(texto))
        if x<0:
            self.Mensaje("Valor no valido debe ser mayo o igual a 0")
            return self.leerRealPos(texto)
        return x
    
    def leerRealPosMy0(self,texto):
        x=win.askfloat("Captura de dato: Entero positivo >0",str(texto))
        if x<=0:
            self.Mensaje("Valor no valido debe ser mayor a 0")
            return self.leerRealPosMy0(texto)
        return x
    def leerRealNegativo(self,texto):
        x=win.askfloat("Captura de dato: Entero positivo >0",str(texto))
        if x>0:
            self.Mensaje("Valor no valido debe ser menor a 0")
            return self.leerRealNegativo(texto)
        return x
    
    def leerCadena2(self,texto):
        x=win.askstring("Captura de dato: Entero positivo >0",str(texto))
        if "".__eq__(x.strip()):
            self.Mensaje("Valor no valido debe contener una cadena")
            return self.leerCadena2(texto)
        return x.strip()
    
    def leerNota_05(self,texto):
        x=win.askstring("Captura de dato: Entero positivo >0",str(texto))
        if x<0 or x>5:
            self.Mensaje("la nota debe estar entre 0 y 5")
            return self.leerNota_05(texto)
        return x


    def Mensaje ( self, texto ):
        msj.showinfo ( title = "Aviso", message = texto )
        # https://recursospython.com/guias-y-manuales/cuadros-de-dialogo-messagebox-en-tkinter/

    def leerEntero ( self, texto ):
        x = win.askinteger ("Captura de dato: Entero", str( texto ), parent = frm ) 
        #frm es la ventana creada desde Tk
        #Se puede adicionar, por ejemplo:  minvalue=0, maxvalue=100
        #https://pythonguides.com/python-tkinter-messagebox/
        return x

    def leerReal ( self, texto ):
        x = win.askfloat ("Captura de dato: Real", str( texto ), parent = frm )
        return x

    def leerCadena ( self, texto ):
        x = win.askstring ("Captura de dato: Cadena", str( texto ), parent = frm )
        return x