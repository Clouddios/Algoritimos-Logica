valor=float(input("Entre com a hora: "))
hora = int(valor)
minutos = (valor - hora)*100
minutos_totais = (hora*60) + minutos
print(minutos_totais)