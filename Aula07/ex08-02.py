numero = int(input("Digite um número inteiro maior que 1: "))

divisor = 2
while divisor < numero:
    if numero % divisor == 0:
        print(f"O número {numero} não é primo.")
        break
    divisor += 1
else:
    print(f"O número {numero} é primo.")