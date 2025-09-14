p1 = str(input(f"Telefonou para a vítima? "))
p2 = str(input(f"Esteve no local do críme? "))
p3 = str(input(f"Mora perto da vítima? "))
p4 = str(input(f"Devia para a vítima? "))
p5 = str(input(f"Ja trabalhou com a vítima? "))
status = 0
p1, p2, p3, p4, p5 = p1.lower(), p2.lower(), p3.lower(), p4.lower(), p5.lower()
if p1 == "sim":
    status += 1
if p2 == "sim":
    status += 1
if p3 == "sim":
    status += 1
if p4 == "sim":
    status += 1
if p5 == "sim":
    status += 1
if status == 2:
    print("Você e considerada suspeita")
elif status >= 3 and status <= 4:
    print("Você e considerada cúmplice")
elif status == 5:
    print("Você e considerada assasina")
else:
    print("Você e considerada inocente")

print(status)