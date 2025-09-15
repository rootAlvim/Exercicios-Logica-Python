print("--------- Hipermercado Tabajara ---------")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")

opcao = int(input("Escolha o tipo de carne (1-3): "))
kg = float(input("Digite a quantidade (kg): "))
pagamento = input("Pagamento será no cartão Tabajara? (S/N): ").strip().upper()

tipo_carne = ""
preco_kg = 0

if opcao == 1:
    tipo_carne = "File Duplo"
    if kg <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
elif opcao == 2:
    tipo_carne = "Alcatra"
    if kg <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
elif opcao == 3:
    tipo_carne = "Picanha"
    if kg <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80
else:
    print("Opção inválida!")
    exit()

# Cálculos
total = kg * preco_kg
desconto = 0

if pagamento == "S":
    desconto = total * 0.05

total_final = total - desconto
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {kg:.2f} Kg")
print(f"Preço total: R$ {total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if pagamento == 'S' else 'Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {total_final:.2f}")
