import math
print("----------------Bem-vindo a nossa loja--------------------")
area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))

area_com_folga = area * 1.1

litros_necessarios = area_com_folga / 6

litros_lata = 18
preco_lata = 80.00

litros_galao = 3.6
preco_galao = 25.00

qtd_latas = math.ceil(litros_necessarios / litros_lata)
preco_latas = qtd_latas * preco_lata

qtd_galoes = math.ceil(litros_necessarios / litros_galao)
preco_galoes = qtd_galoes * preco_galao

qtd_latas_misto = int(litros_necessarios // litros_lata)
litros_restantes = litros_necessarios - (qtd_latas_misto * litros_lata)
qtd_galoes_misto = math.ceil(litros_restantes / litros_galao)

preco_misto = (qtd_latas_misto * preco_lata) + (qtd_galoes_misto * preco_galao)

print("\n---------------------- Opções de Compra -------------------------")
print(f"1 - Apenas latas de 18 litros: {qtd_latas} lata(s), preço total: R$ {preco_latas:.2f}")
print(f"2 - Apenas galões de 3,6 litros: {qtd_galoes} galão(ões), preço total: R$ {preco_galoes:.2f}")
print(f"3 - Mistura: {qtd_latas_misto} lata(s) e {qtd_galoes_misto} galão(ões), preço total: R$ {preco_misto:.2f}")