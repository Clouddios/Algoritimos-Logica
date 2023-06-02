vetor1 = []
vetor2 = []

print("Digite os elementos do vetor 1:")
for i in range(10):
    elemento = int(input(f"Elemento {i+1}: "))
    vetor1.append(elemento)

print("\nDigite os elementos do vetor 2:")
for i in range(10):
    elemento = int(input(f"Elemento {i+1}: "))
    vetor2.append(elemento)

vetor_resultante = []
for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])

print("\nVetor resultante da intercalação:")
for elemento in vetor_resultante:
    print(elemento)