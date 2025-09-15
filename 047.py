cont = True
while cont == True:
    usuario = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite sua senha: "))
    if senha == usuario:
        print("A sua senha não pode ser igual ao nome de usuário, digite novamente")
    else:
        cont =  False
        print("Senha e usuário cadrastadas com sucesso!")