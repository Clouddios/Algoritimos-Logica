sexo=input("Sexo (F) FEMENINO | (M) MASCULINO : ")
altura=float(input("Digite a ALTURA: "))

if sexo.upper()=="M":
    peso=(72.7*altura)-58
else:
    peso=(62.1*altura)-44.7

print(f"Peso ideal é:{peso:.2f}kg")