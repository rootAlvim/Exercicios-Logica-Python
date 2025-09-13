print("Me informe uma data qualquer no formato dd/mm/aaaa ")

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# quantidade de dias em cada mês (considerando fevereiro = 28)
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# verifica ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes[1] = 29  # fevereiro tem 29 dias

if mes < 1 or mes > 12:
    print("A data informada é inválida! (mês inexistente)")
elif dia < 1 or dia > dias_por_mes[mes-1]:
    print("A data informada é inválida! (dia fora do limite do mês)")
else:
    print("A data informada é válida!")
