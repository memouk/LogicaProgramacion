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