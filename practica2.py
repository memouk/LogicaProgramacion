import math
from art import *
from 
# class HallarSalario:
#     def nuevoSalario():
#         #entrada
#         nombre= input("ingrese el nombre: ")
#         salAct= float(input("ingrese el salario anterio "))
#         porcAum= float(input("ingrese el % del aumento "))
#         #proceso
#         valAum= salAct*porcAum/100
#         salNew= valAum+salAct
#         #salida
#         print("hola",nombre,"su nuevo salario es \n",salNew)

#     nuevoSalario()

# class calculos:
#     def volumenArea():
#         #entrada
#         lado=float(input("ingrese el valor para el lado"))
#         #proceso
#         volumen=lado**3*2**(1/2)/12
#         vol2=pow(lado,3)*math.sqrt(2)/12
#         altura=lado*6**(1/2)/3
#         alt2=lado*math.sqrt(6)/3
        
#         #salida
#         print("el valor del alt1",altura)
#         print("el valor del alt2",alt2)
#         print("el valor del vol1",volumen)
#         print("el valor del vol2",vol2)


#     volumenArea()


class Nomina:
    def principal():
        #entada
        tprint("gonorreas24")
        decor("barcode1")
        cod=int(input("ingrese el codigo\n"))
        salMes=float(input("Cual es su salario\n"))
        KHE=float(input("cuantashoras extras\n"))
        KHN=float(input("cuantas horas laboro\n"))
        vrVtas=float(input("valor de las ventas\n"))
        porcComVtas=float(input("por compras\n"))
        

        #proceso
        vrH= (salMes/30)/8
        vrxHExt=vrH*1.35*KHE
        vrSB=vrH*KHN+vrxHExt
        vrRete=vrSB*8/100
        vrCom= vrVtas* porcComVtas/100
        vrSN=vrSB-vrRete+vrCom

        #salida
        print("el codifo #",cod,"con un valor por horas de",vrH )       

    principal()