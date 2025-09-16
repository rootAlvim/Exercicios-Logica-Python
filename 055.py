n1 = int(input("Digite o 1º número inteiro "))
n2 = int(input("Digite o 2º número inteiro "))
if n1 < n2:
    for n in range(n1+1,n2):
        print(n, end=" ")
elif n1 > n2:
    for n in range(n1-1, n2, -1):
        print(n, end=" ")