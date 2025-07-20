n1 = int(input("Digite o 1° valor: "))
n2 = int(input("Digite o 2° valor: "))
n3 = int(input("Digite o 3° valor: "))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
else:
    maior = ' (Nenhum , todos os valores sao iguais)'
print(f"O maior valor é {maior}")
