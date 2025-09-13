numero = int(input("Digite um número inteiro entre 1 e 999: "))

if numero <= 0 or numero >= 1000:
    print("Número inválido!")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    # Centenas
    if centenas > 0:
        partes.append(f"{centenas} {'centena' if centenas == 1 else 'centenas'}")

    # Dezenas
    if dezenas > 0:
        partes.append(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}")

    # Unidades
    if unidades > 0:
        partes.append(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}")

    # Monta a frase com vírgulas e "e"
    if len(partes) == 1:
        resultado = partes[0]
    elif len(partes) == 2:
        resultado = " e ".join(partes)
    else:
        resultado = ", ".join(partes[:-1]) + " e " + partes[-1]

    print(resultado)
