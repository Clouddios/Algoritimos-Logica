v = float(input("Digite o valor da compra: "))

if v >= 5000:
    desc = 0.3
elif v < 1000:
    desc = 0.1
else:
    desc = 0.2

print(f"Valor do desconto R$ {v*desc:.2f}. Valor final R$ {v-(v*desc):.2f}")