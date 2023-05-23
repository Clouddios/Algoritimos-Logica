from datetime import date

data= date.today()
nasc=int(input("Ano de Nascimento: "))
ano= data.year

idade=ano-nasc

if idade >= 16:
    print("Pode VOTAR")
else:
    print("Não pode VOTAR")
    
if idade >= 18:
    print("Pode tirar CNH")
else:
    print("Não pode tirar CNH")