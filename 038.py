# Pergunta o valor do saque
valor = int(input("Digite o valor do saque (10 a 600): "))

# Verifica se está dentro do limite
if valor < 10 or valor > 600:
    print("Valor inválido! O saque deve ser entre 10 e 600 reais.")
else:
    restante = valor

    notas_100 = restante // 100
    restante = restante % 100

    notas_50 = restante // 50
    restante = restante % 50

    notas_10 = restante // 10
    restante = restante % 10

    notas_5 = restante // 5
    restante = restante % 5

    notas_1 = restante

    # Monta a lista de notas para exibir, ignorando as que são zero
    resultado = []
    if notas_100 > 0:
        resultado.append(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100")
    if notas_50 > 0:
        resultado.append(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50")
    if notas_10 > 0:
        resultado.append(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10")
    if notas_5 > 0:
        resultado.append(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5")
    if notas_1 > 0:
        resultado.append(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1")

    # Formata a saída com vírgula e "e"
    if len(resultado) == 1:
        print(resultado[0])
    elif len(resultado) == 2:
        print(" e ".join(resultado))
    else:
        print(", ".join(resultado[:-1]) + " e " + resultado[-1])
