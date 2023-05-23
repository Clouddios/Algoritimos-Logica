nota = int(input("Digite a nota: "))

if nota <= 49:
    conceito = "D"
elif nota >= 90:
    conceito = "A"
elif nota < 70:
    conceito = "C"
else:
    conceito = "B"

print(f"Conceito: {conceito}")