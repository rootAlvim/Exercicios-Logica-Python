p1 = float(input("Digite o preço do 1° produto: "))
p2 = float(input("Digite o preço do 2° produto: "))
p3 = float(input("Digite o preço do 3° produto: "))
if p1 < p2 and p1 <  p3:
    menor = p1
elif p2 < p1 and p2 <  p3:
    menor = p2
elif p3 < p1 and p3 < p2:
    menor = p3
else:
    menor = ' (Qualquer um, todos os valores sao iguais)'
print(f"O produto que devera comprar e o de valor: {menor} ")