idades = []
total_pessoas = 0

while True:
    idade = int(input("Digite a idade (ou 0 para sair): "))

    if idade == 0:
        break

    idades.append(idade)
    total_pessoas += 1

if total_pessoas > 0:
    idade_media = sum(idades) / total_pessoas
    print(f"A idade média é: {idade_media:.2f}")
    print(f"O número total de pessoas é: {total_pessoas}")
else:
    print("Nenhum dado foi inserido.")