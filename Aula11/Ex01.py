elementos = []
for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    elementos.append(elemento)


tupla_invertida = tuple(elementos[::-1])

print("Tupla invertida:", tupla_invertida)