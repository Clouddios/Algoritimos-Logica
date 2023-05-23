comb = {"A":1.7997, "D":0.9798, "G":2.1009}

tipo = input("Digite o tipo de combustivel A-Álcool D - Diesel G – Gasolina : ")
litros = float(input("Digite a quantidade de LITROS: "))

valor = litros * comb[tipo.upper()]

print(f"Valor total: R$ {valor:.2f}")