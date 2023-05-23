opc = int(input("Digite a opção desejada: "))
a = int(input("Digite PRIMEIRO numero: "))
b = int(input("Digite SEGUNDO numero: "))

if opc == 1:
    print(f"MEDIA: {(a+b)/2}")
elif opc == 2:
    print(f"DIFERENÇA: {a-b}")
elif opc == 3:
    print(f"PRODUTO: {a*b}")
elif opc == 4:
    print(f"DIVISÃO: {a/b}")
else:
    print("Opção INVALIDA")        

