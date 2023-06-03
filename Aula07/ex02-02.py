
while True:
    base = float(input("Digite a BASE do Triangulo: "))
    if (base > 0):
        break
    print("Digite somente numeros Maiores que 0 para a base")
    
while True:
    altura = int(input("Digite um ALTURA do Triangulo: "))
    if (altura > 0):
        break
    print("Digite somente numeros Maiores que 0 para a altura")
    
area = (base*altura)/2
print(f"Area do Triangulo é {area}")