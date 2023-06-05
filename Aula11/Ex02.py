nomes = {}
soma = 0

for i in range(10):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite o idade da pessoa: "))
    print("------------------------------")
    nomes[nome] = idade

for idade in nomes.values():
    soma += idade

media = soma/len(nomes)

for nome,idade in nomes.items():
    if idade > media:
        print(f"Nome: {nome} Idade: {idade}")