a = float(input("Digite o valor de a: "))
if a == 0:
    print("Sua equação não e do segundo grau")
else:
    b = float(input("Digite o valor de b:"))
    c = float(input("Digite o valor de c:"))
    delta = (b*b)-4*a*c
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        print("A equação  possui apenas uma raiz real")
    elif delta > 0:
        print("A equação  possui duas raízes reais")
