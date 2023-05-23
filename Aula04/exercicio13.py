salario=float(input("Salario Minimo: R$"))
quilowatts=float(input("Quantidade de Kw: "))

valorkw = salario/8
conta = quilowatts*valorkw
contadesc = conta-(conta*0.15)

print(f"Valor do Kw..............: R$ {valorkw:.2f}")
print(f"Valor total a ser pago...: R$ {conta:.2f}")
print(f"Valor com desconto de 15%: R${contadesc:.2f}")