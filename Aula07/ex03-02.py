m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))

somatotal = 0

if m > 0 and n > 0 and m > n:
    for num in range(n, m + 1):
        somatotal += num
else:
    print("Valores inválidos. Certifique-se de que m e n são inteiros positivos e que m é maior que n.")

print(f"A soma dos números entre {m} e {n} é: {somatotal}")