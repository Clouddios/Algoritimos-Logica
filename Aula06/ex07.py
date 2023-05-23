pontos_necessarios = float(input("Digite a quantidade de pontos necessários (em mil unidades): "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))

valor_dolar = pontos_necessarios / 1.5

valor_reais = valor_dolar * cotacao_dolar

print(f"Você precisará gastar R$ {valor_reais:.2f} para obter {pontos_necessarios:.0f} mil pontos.")
