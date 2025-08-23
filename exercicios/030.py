# Folha de Pagamento

# Entrada de dados
valor_hora = float(input("Digite o valor da sua hora: "))
horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Cálculo do salário bruto
salario_bruto = valor_hora * horas

# Cálculo do IR conforme a tabela
if salario_bruto <= 900:
    ir = 0
    ir_perc = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    ir_perc = 5
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
    ir_perc = 10
else:
    ir = salario_bruto * 0.20
    ir_perc = 20


inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11  # não desconta do salário
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

# Saída formatada
print(f"Salário Bruto: ({valor_hora:.2f} * {horas})      : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_perc}%){' ' * (23 - len(str(ir_perc)))}: R$ {ir:8.2f}")
print(f"(-) INSS (10%){' ' * 18}: R$ {inss:8.2f}")
print(f"FGTS (11%){' ' * 20}: R$ {fgts:8.2f}")
print(f"Total de descontos{' ' * 11}: R$ {total_descontos:8.2f}")
print(f"Salário Líquido{' ' * 14}: R$ {salario_liquido:8.2f}")
