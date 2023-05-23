def calcular_fatorial(x):
    fatorial = 1

    for i in range(1, x + 1):
        fatorial *= i

    return fatorial

x = int(input("Digite um número inteiro: "))

if x >= 0:
    resultado = calcular_fatorial(x)

    print(f"O fatorial de {x} é: {resultado}")
else:
    print("O fatorial é definido apenas para números não negativos.")
