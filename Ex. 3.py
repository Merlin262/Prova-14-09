from tkinter import Y


contador = 0
letra = Y

while contador<=4:
    tentativa=input("Informe a letra: ")
    if tentativa == letra:
        print("Parabens!!!!! Você acertou")
        break
    else:
        print("letra errada, tente novamente")
    contador=contador+1