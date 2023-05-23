ra = str(input("Digite seu RA: "))
soma = 0
produto = 1
for num in ra:
    soma += int(num)
    produto *= int(num)
    
print(f"\nMultiplicação = {produto}\nSoma = {soma}")