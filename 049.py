cont = True
n = 0
A = 80000
B = 200000
while cont == True:
    n += 1
    C = A * (1.03**n)
    D = B * (1.015**n)
    if C > D:
        cont = False
        print(f"A população A levará {n} anos para ultrapassar a população B! ")

