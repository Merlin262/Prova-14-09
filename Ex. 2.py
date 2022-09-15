tempoServ = int(input("Informe o tempo de serviço "))
idade = int(input("Informe sua idade "))

if idade>=65:
    print("Pode se aposentar")
elif tempoServ>=30:
    print("Pode se aposentar")
elif idade>=60 and tempoServ>=25:
    print("Pode se aposentar")
else:
    print("Aposentadoria Negada")
