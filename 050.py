cont = True
while cont:
    A = float(input("Digite o tamanho da população A: "))
    B = float(input("Digite o tamanho da população B: "))
    porcent = float(input("Digite o crescimento percentual de A: "))
    porcent2 = float(input("Digite o crescimento percentual de B: "))
    n = 0
    while True:
        n += 1
        C = A *  (((porcent/100) + 1)**n)
        D = B *  (((porcent2/100) + 1)**n)
    
        if C >= D:
            print(f"A população A levará {n} anos para ultrapassar ou igualar a população B! ")
            print(f"A cidade a tem {int(C)} habitantes e B {int(D)}")
            break

    opc = str(input("Deseja continuar (S/N)? "))
    opc = opc.upper()
    if opc == "S":
        cont = True
    elif opc == "N":
        cont = False

