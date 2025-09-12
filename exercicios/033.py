lado1 = float(input("Digite o 1º lado do triângulo: "))
lado2 = float(input("Digite o 2º lado do triângulo: "))
lado3 = float(input("Digite o 3º lado do triângulo: "))
if (lado1 + lado2) > 3  and   (lado1 + lado3) > lado2 and  (lado2 + lado3) > lado1:
    print("Os três lados podem formar um triângulo")
    if (lado1 == lado2) and (lado2 == lado3):
        print("Esse triângulo é escaleno")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
          print("Esse triângulo é isósceles")
    else:
         print("Esse triângulo é escaleno")
else:
    print("Os três lados não podem formar um triângulo")