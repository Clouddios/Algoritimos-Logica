deposito = float(input("Deposito: R$"))
juros=float(input("Juros: "))

saldo = deposito+(deposito * (juros/100))
juros = deposito * (juros/100)

print(f"Seu invertimento rendeu R${juros:9.2f} portanto seu total em conta atualmete e de R${saldo:9.2f}")
