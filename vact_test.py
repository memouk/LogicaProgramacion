from Generales.captura import clsGenerales




class vect_test:
    og= clsGenerales()

    def __init__(self) -> None:

        vect= []

        texto="ingrese edad"
        for i in range( 3):
            dato = "[" + str( i ) + "] "+ texto + ": "
            print(dato)
            vect.append(input(dato))
        print(vect)

m=vect_test()