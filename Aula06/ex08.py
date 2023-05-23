import math

comprimento=float(input("Digite o comprimento: "))
largura=float(input("Digite o largura: "))
tamanhoDaLata=float(input("Digite o tamanho da lata de tinta: "))

metros=2*((comprimento*2.8)+(largura*2.8))-(0.8*2.1)

litros=metros/3

latas=math.ceil(litros/tamanhoDaLata)

print(f"Seu ambiente mede {metros:.2f} voçê vai precisar de {int(latas)} latas para pintar")
