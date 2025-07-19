import math
print("----------------Bem-vindo a nossa loja--------------------")
area = float(input("Me o tamanho em metros quadrados da área a ser pintada. "))
total = (area/3)/18
valor = math.ceil(total) * 80.00
print(f"Bom você irá prescisar de {math.ceil(total)} latas de tinta , isso da {valor}$ reais!" )