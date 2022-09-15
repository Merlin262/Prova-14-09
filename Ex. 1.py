contador = 0

while contador<=2:
    numero = int(input("Informe um valor: "))
    maior = numero
    if numero>maior:
        maior = numero
    contador=contador+1

print(maior)