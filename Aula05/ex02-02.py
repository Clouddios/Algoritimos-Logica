idade = int(input("Digite a idade do nadador: "))

if idade > 30:
    print("Sênior")
elif idade <= 7:
    print("Infantil")
elif idade <= 10:
    print("Juvenil")
elif idade <= 15:
    print("Adolescente")
else:
    print("Adulto")
