arquivo = open("frutas.txt", encoding="utf-8")
texto = arquivo.read().strip()
lista = texto.split("\n")
print(lista)
arquivo.close()
arquivo = open("frutas.txt", "a", encoding="utf-8")
while True:
    fruta = input("Digite uma Fruta: ")
    if fruta == '':
        break
    if fruta in lista:
        print("Fruta repetida!!")
    else:
        arquivo.write(fruta+"\n")

