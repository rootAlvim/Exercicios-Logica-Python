maior = float('-inf')
for n in range(1,6):
    
    n1 = int(input(f"Digite o {n}º numero: "))
    if n1 > maior:
        maior = n1
print(f"O maior número é : {maior}")