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


class clsVectorGral:
    ogv = clsGenerales()
    #Constructor
    def _init_ ( self ) -> None: #Constructor vacio
        pass #para aquellos casos en que la sintaxis requiera una instrucción, pero no queramos que se emplee.
    
    def llenarEnteros ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerEntero ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarEnterosPos ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerEnteroPos ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarEnterosPosMy0 ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerEnteroPosMy0 ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarEnterosNeg ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerEnteroNeg ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarReales ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerReal ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarRealesPos ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerRealPos ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarRealesPosMy0 ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerRealPosMy0 ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarRealesNeg ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerRealNegativo ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarCadenas ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerCadena ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def llenarCadenas2 ( self, vect, texto ):
        if len ( vect ) > 0:
            for i in range( len(vect) ):
                dato = "[" + str( i ) + "] "+ texto + ": "
                vect[ i ] = self.ogv.leerCadena2 ( dato )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
        return vect
    
    def mostrarDatos ( self, vect, texto ):
        if len ( vect ) > 0:
            rpta = "\n" + texto + "\n"
            for i in range( len(vect) ):
                rpta += str(vect[ i ]) + "\t"
            rpta += "\n"
            self.ogv.Mensaje ( rpta )
        else:
            self.ogv.Mensaje ( "Error, vector vacío" )
## comienza matriz
class clsMatrizGral:
    og = clsGenerales( )
    #Constructor
    def __init__ ( self ) -> None: #Constructor vacio 
        pass

    def llenarEnteros (self, mat, texto):
        if len(mat) > 0:
            for i in range(len(mat)):
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerEntero (dato)
        else:
            self.og. Mensaje ("Error, matriz vacía")
        return mat
    
    def llenarEnterosPos ( self, mat, texto):
        if len(mat) > 0:
            for i in range (len(mat)): 
                for j in range (len( mat[i]) ):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerEnteroPos(dato)
        else:
            self.og. Mensaje ("Error, matriz vacía")
        return mat
    
    def llenarEnterosPosMy0( self, mat, texto):
        if len(mat) > 0:
            for i in range (len(mat)): 
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerEnteroPosMy0(dato)
        else:
            self.og.Mensaje ("Error, matriz vacía")
        return mat
    
    def llenarEnterosNeg ( self, mat, texto):
        if len(mat) > 0:
            for i in range (len(mat)): 
                for j in range ( len(mat[i])):
                    dato = "[" + str( i ) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerEnteroNeg(dato)
        else:
            self.og.Mensaje ("Error, matriz vacia")
        return mat

    def llenarReales ( self, mat, texto):
        if len(mat) > 0:
            for i in range (len(mat)):
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerReal(dato)
        else:
            self.og. Mensaje ("Error, matriz vacia")
        return mat
    
    def llenarRealesPos ( self, mat, texto ):
        if len(mat) > 0:
            for i in range (len(mat)): 
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerRealPos(dato)
        else:
            self.og. Mensaje ("Error, matriz vacia")
        return mat
    
    def llenarRealesPosMy ( self, mat, texto ):
        if len(mat) > 0:
            for i in range (len(mat)):
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j]= self.og. leerRealPosMy0 ( dato )
        else:
            self.og. Mensaje ("Error, matriz vacía")
        return mat
    
    def llenarRealesNeg ( self, mat, texto ):
        if len(mat) > 0:
            for i in range (len( mat)):
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerRealNegativo(dato)
        else:
            self.og. Mensaje ("Error, matriz vacía")
        return mat

    def llenarCadenas ( self, mat, texto ):
        if len( mat ) > 0:
            for i in range (len(mat)):
                for j in range (len(mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j]= self.og.leerCadena (dato)
        else:
            self.og. Mensaje ("Error, matriz vacía")
        return mat
    
    def llenarCadenas2 ( self, mat, texto ):
        if len( mat ) > 0:
            for i in range (len(mat)):
                for j in range (len( mat[i])):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerCadena2 (dato)
        else:
            self.og. Mensaje ( "Error, matriz vacía")
        return mat
    
    def mostrarDatosFil( self, mat, texto ):
        out = texto
        for i in range (len(mat)):
            out += '\n'
            for j in range (len(mat[i])):
                out += '{:>6s}'.format(str( mat[i][j]) + '')
            out += '\n'
        self.og. Mensaje (out)

    def mostrarDatosCol( self, mat, texto ):
        out = texto
        for j in range (len(mat[0])):
            out += '\n'
            for i in range (len(mat)):
                out += '{:>6s}'.format(str(mat[i][j]) + '\n')
            self.og. Mensaje ( out )

#fin clase clsMatrizGral
    def __crearMatriz( self, kf, kc):
        m = []
        for i in range( kf ):
            m.append([None] * kc) #Llena con valores nulos (None), lo puede reemplazar por cualquier otro valor
        return m

    def llenarEnteros2 ( self, kf, kc, texto ): #Crear y llenar conociendo el tamaño de las dimensiones
        if kf > 0 and kc > 0:
            mat = self.__crearMatriz( kf, kc )
            for i in range(kf):
                for j in range (kc):
                    dato = "[" + str(i) + "][" + str(j) + "]" + texto + ":"
                    mat[i][j] = self.og.leerEntero(dato)
        else:
            self.og.Mensaje ("Error, Tamaño erróneo")
        return mat