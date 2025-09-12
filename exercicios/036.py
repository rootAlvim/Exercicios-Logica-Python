print("Me informe uma data qualquer no formato dd/mm/aaaa ")
dia = int(input("Digite o dia:"))
mês = int(input("Digite o mês:"))
ano = str(input("Digite o ano:"))
if dia > 31:
    print("A data informada e inválida!")
elif mês > 12:
    print("A data informada e inválida!")
elif ano[0] == '0':
     print("A data informada e inválida!")
else:
     print("A data informada e válida!")



