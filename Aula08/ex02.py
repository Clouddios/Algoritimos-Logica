data = input("Digite a DATA: ")
separador = "/"

data = data.split('/')
data = data[::-1]

data = separador.join(data)

print(data)