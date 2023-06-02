palavras = []
for i in range(20):
    palavra = input("Digite uma palavra (até 10 caracteres): ")
    palavras.append(palavra)

palavras_invertidas = []
for palavra in palavras:
    palavra_invertida = palavra[::-1]
    palavras_invertidas.append(palavra_invertida)