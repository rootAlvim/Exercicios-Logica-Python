cont = True
while cont:
    erros = []  
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário bruto: "))
    sexo = input("Digite seu sexo (f/m): ").lower()
    ec = input("Digite seu estado civil (s/c/v/d): ").lower()

    if len(nome) < 3:
        erros.append("Seu nome deve conter mais de 3 caracteres.")
    if idade < 0 or idade > 150:
        erros.append("Idade inválida!")
    if salario < 0:
        erros.append("Salário inválido!")
    if sexo not in ["f", "m"]:
        erros.append("Sexo inválido!")
    if ec not in ["s", "c", "v", "d"]:
        erros.append("Estado civil inválido!")

    if erros:
        print("\nErros encontrados:")
        for e in erros:
            print("-", e)
        print("Por favor, digite novamente.\n")
        cont = True
    else:
        cont = False

print("\nCadastro realizado com sucesso!")
