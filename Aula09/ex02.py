vetor = []

for i in range(10):
    elemento = int(input("Digite o elemento do vetor: "))
    vetor.append(elemento)

maior_valor = max(vetor)
posicao_maior_valor = vetor.index(maior_valor)

print("Maior valor:", maior_valor)
print("Posição do maior valor:", posicao_maior_valor)