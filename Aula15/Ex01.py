arquivo = open("disco.txt", encoding="utf-8")
texto = arquivo.read()
lista = texto.split("\n")
linha = []
dic = {}
for items in lista:
    linha = items.split(",")
    dic[linha[0]] = int(linha[1])/(1024*1024)

print("ACME Inc.                    Uso do espaço em disco pelos usuários\n")
print("-------------------------------------------------------------------------")
print("Nr.   Usuario               Espaço ultilizado     % do uso")
item = 0
total = 0

for nome, espaco in dic.items():
    total += espaco

for nome, espaco in dic.items():
    branconome = len(nome)-15
    item += 1
    print(f"{item}     {nome}      {espaco:.2f} MB      {(espaco/total)*100:.2f}%")

print(f"\n\nEspaço total ocupado: {total:.2f}MB")
print(f"Espaço medio ocupado: {total/item:.2f}MB")