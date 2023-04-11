while True:
    try:
        x=int(input("ingrese un numero entre 50y 70: "))

    except:
        print("dato no valido")

    else:
        if (x>=50 and x<=70):
            break
        else:
            print("el numero ingresado no es valido")
print(x)

            