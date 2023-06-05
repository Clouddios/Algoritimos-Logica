def calcular_mdc(a, b):
    if a == 0 or b == 0:
        return max(abs(a), abs(b))
    
    while b != 0:
        resto = a % b
        a = b
        b = resto
    
    return abs(a)

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

mdc = calcular_mdc(numero1, numero2)

print("MDC:", mdc)