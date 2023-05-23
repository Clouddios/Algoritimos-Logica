from datetime import date

data= date.today()
nasc=int(input("Ano de Nascimento: "))
ano= data.year

idade=ano-nasc

print(f"Você tem {idade} anos de vida")
print(f"Você tem {idade*12} meses de vida")
print(f"Você tem {idade*365} dias de vida")
print(f"Você tem {idade*52} semanas de vida")