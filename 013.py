
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()

peso_ideal_homem = round((72.7 * altura) - 58, 2)
peso_ideal_mulher = round((62.1 * altura) - 44.7, 2)

print("Peso ideal para homens:", peso_ideal_homem, "kg")
print("Peso ideal para mulheres:", peso_ideal_mulher, "kg")