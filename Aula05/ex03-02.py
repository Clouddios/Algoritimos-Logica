opc = int(input("Digite o CODIGO de ORIGEM: "))
x = float(input("Digite VALOR: "))

if opc == 1:
    p = "SUL"
    x += (x*0.11)
elif opc == 2:
    p = "NORTE"
    x += (x*0.13)
elif opc == 3:
    p = "NORDESTE"
    x += (x*0.09)
elif opc == 4:
    p = "CENTRO-OESTE"
    x += (x*0.12)
elif opc == 5:
    p = "SULDESTE"
    x += (x*0.18)
else:
    print("Opção INVALIDA") 
    
print(f"Procedência {p}, Valor com IMPOSTO: R${x:.2f}")