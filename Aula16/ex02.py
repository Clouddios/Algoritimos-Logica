carros = {}
while True:
    carro = input("Digite o modelo do carro: ")
    if carro == "":
        break
    consumo = int(input("Digite o consumo do carro: "))

    carros[consumo] = carro

print("Comparativo de Consumo de Combustivel ")
item = 0
for consumo, modelo in carros.items():
    item += 1
    print(f"Veiculo {item}")
    print(f"Carro: {modelo}")
    print(f"Km por litro: {consumo}l")
    print("*-------------------------*")

print("Relatorio final")

lista_economico = sorted(carros.items())
print(lista_economico)

item = 0
for consumo, modelo in carros:
    item += 1
    print(f"{item} - {modelo} - {consumo}")