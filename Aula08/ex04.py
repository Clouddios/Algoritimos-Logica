frase = input("Digite uma frase: ")

contador = 0

for caractere in frase:
    if caractere.lower() in "aeiou":
        contador += 1

print("Número de vogais na frase:", contador)