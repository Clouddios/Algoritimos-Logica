vetor = []

for i in range(10):
    elemento = int(input("Digite o elemento do vetor: "))
    vetor.append(elemento)

print("Vetor na ordem inversa:")
for elemento in reversed(vetor):
    print(elemento)