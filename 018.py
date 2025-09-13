mb = float(input("Qual tamanho do arquivo em MB? "))
mbps = float(input("Qual a velocidade do link em Mbps? "))
tempo = (mb*8)/mbps
horas = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60
print(f" A velocidade do seu dowload será: {horas}h {minutos}min {segundos}s")
