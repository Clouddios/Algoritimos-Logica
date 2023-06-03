total_pessoas = 20
pesos = []
alturas = []

for i in range(total_pessoas):
    peso = float(input(f"Digite o peso da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))

    pesos.append(peso)
    alturas.append(altura)

peso_medio = sum(pesos) / total_pessoas
altura_medio = sum(alturas) / total_pessoas

imcs = []
for i in range(total_pessoas):
    imc = pesos[i] / (alturas[i] ** 2)
    imcs.append(imc)

maior_imc = max(imcs)
menor_imc = min(imcs)

print(f"Peso médio: {peso_medio:.2f}")
print(f"Altura média: {altura_medio:.2f}")
print(f"Maior IMC: {maior_imc:.2f}")
print(f"Menor IMC: {menor_imc:.2f}")