lista1 = []
lista2 = []

for i in range(10):
    lista1.append(int(input("Digite numeros da primeira lista: ")))
print("==============================================")
for i in range(10):
    lista1.append(int(input("Digite numeros da segunda lista: ")))

conjunto = set(lista1 + lista2)

print(conjunto)