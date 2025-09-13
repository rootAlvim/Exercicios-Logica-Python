n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1+n2)/2
if media >= 90 and media <= 10:
    status = "Aprovado"
elif media >= 75  and media < 90:
    status = "Aprovado"
elif media >= 60  and media < 75:
    status = "Aprovado"
elif media >= 40  and media < 60:
    status = "Reprovado"
elif media >= 0  and media < 40:
    status = "Reprovado"

print(f"Sua média foi {media} e voçe está {status} ")