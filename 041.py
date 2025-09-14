n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
print("----------------------------")
print("          + - / *           ")
print("----------------------------")
opr = str(input("Qual operação deseja realizar?"))
if opr == "+":
    res = n1+n2
    print(f"A soma é {res}", end=" ")
    if res % 2 == 0:
        print(f"ele e par", end=" ")
    else:
        print(f"ele e impar", end="")

    if res >= 0:
        print(f", positivo", end="")
    else:
        print(f", negativo", end="")

    if res % 1 == 0:
        print(f" e inteiro", end="")
    else:
        print(f" e decimal ", end="")

elif opr == "-":
    res = n1-n2
    print(f"A subtração é {res}", end=" ")
    if res % 2 == 0:
        print(f"ele e par", end=" ")
    else:
        print(f"ele e impar", end="")

    if res >= 0:
        print(f", positivo", end="")
    else:
        print(f", negativo", end="")

    if res % 1 == 0:
        print(f" e inteiro", end="")
    else:
        print(f" e decimal ", end="")

elif opr == "/":
    res = n1/n2
    print(f"A divisão é {res}", end=" ")
    if res % 2 == 0:
        print(f"ele e par", end=" ")
    else:
        print(f"ele e impar", end="")

    if res > 0:
        print(f", positivo", end="")
    else:
        print(f", negativo", end="")

    if res % 1 == 0:
        print(f" e inteiro", end="")
    else:
        print(f" e decimal ", end="")

elif opr == "*":
    res = n1*n2
    print(f"A multiplicação é {res}", end=" ")
    if res % 2 == 0:
        print(f"ele e par", end=" ")
    else:
        print(f"ele e impar", end="")

    if res >= 0:
        print(f", positivo", end="")
    else:
        print(f", negativo", end="")

    if res % 1 == 0:
        print(f" e inteiro", end="")
    else:
        print(f" e decimal ", end="")             
           
                
    