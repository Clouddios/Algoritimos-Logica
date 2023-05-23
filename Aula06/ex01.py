n = int(input("Digite um numero: "))

if n % 2 == 0:
    x = "Par"
else:
    x = "Impar"

if n > 0:
    y = "Positivo"
else:
    y = "Negativo"

print(f"O numero {n} é {x} e {y}")