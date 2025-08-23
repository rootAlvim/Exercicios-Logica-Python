salario = float(input("Digite o valor do seu salário: "))
if salario == 280.00 :
    aumento = salario * 0.20
    salario2 = salario + aumento
    print(f"O salário antes do reajuste era de {salario}")
    print(f"O percentual do aumento e de 20% ")
    print(f"O valor do aumento e de: {aumento}")
    print(f"O novo salário e:  {salario2}")
elif salario > 280.00 and salario <= 700.00:
    aumento = salario * 0.15
    salario2 = salario + aumento
    print(f"O salário antes do reajuste era de {salario}")
    print(f"O percentual do aumento e de 15% ")
    print(f"O valor do aumento e de: {aumento}")
    print(f"O novo salário e:  {salario2}")
elif salario > 700.00 and salario <= 1500.00:
    aumento = salario * 0.10
    salario2 = salario + aumento
    print(f"O salário antes do reajuste era de {salario}")
    print(f"O percentual do aumento e de 10% ")
    print(f"O valor do aumento e de: {aumento}")
    print(f"O novo salário e:  {salario2}")
elif salario > 1500.00:
    aumento = salario * 0.05
    salario2 = salario + aumento
    print(f"O salário antes do reajuste era de {salario}")
    print(f"O percentual do aumento e de 5% ")
    print(f"O valor do aumento e de: {aumento}")
    print(f"O novo salário e:  {salario2}")
