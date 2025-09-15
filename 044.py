kg_maça = float(input(f"Digite a quantidade em kg comprada em maças: "))
kg_morango  = float(input(f"Digite a quantidade em kg comprada em morangos: "))
valor_total = 0
valor_total2 = 0
if kg_maça <= 5:
    valor_total = kg_maça*1.80
elif kg_maça > 5:
    valor_total = kg_maça*1.50

if kg_maça > 8 or valor_total2 > 25.00:
    valor_total  *= 0.9

if kg_morango <= 5:
    valor_total2 = kg_morango*2.50
elif kg_morango > 5:
    valor_total2 = kg_morango*2.20

if kg_morango > 8 or valor_total2 > 25.00:
    valor_total2  *= 0.9

print(f"Valor total da compra de maças: {round(valor_total,2)}")
print(f"Valor total da compra de morango: {round(valor_total2,2)}")