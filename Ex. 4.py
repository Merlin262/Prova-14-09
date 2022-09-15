saldo = 0.00

escolhaMenu = 0

while escolhaMenu!=4:
    escolhaMenu = int(input("Escolha 1 para consultar saldo, 2 para saque, 3 para deposito e 4 para sair "))
    if escolhaMenu == 1:
        print("Seu saldo é de " + str(saldo))
    elif escolhaMenu == 2:
        saque = float(input("Informe o valor a ser sacado: "))
        saldo = saldo - saque
        print(saldo)
    elif escolhaMenu == 3:
        deposito = float(input("Informe o valor a ser depositado: ")) 
        saldo = saldo + deposito
        print(saldo)
    elif escolhaMenu<1 or escolhaMenu<4:
        print("Por favor selecione uma opção adequada")

print("Seu saldo final é de " + str(saldo))