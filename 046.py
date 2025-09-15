cont = True
while cont == True:
    n1 = float(input("Digite sua nota: "))
    if n1 < 0 or n1 > 10:
        print("Nota invalida digite novamente!")
    else:
        print("Nota valida!")
        cont = False