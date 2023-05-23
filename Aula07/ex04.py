soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número (0 para encerrar): "))

    if numero % 2 == 0:
        if numero == 0:
            break

        soma += numero
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos números pares é: {media:.2f}")
else:
    print("Nenhum número par foi fornecido.")