try:
    len(9.4)
except TypeError as erro1:
    print(f"A aplicação gerou o erro {erro1}.")
except NameError as erro2:
    print(f"A aplicação gerou o erro {erro2}.")
except:
    print("Erro diferente, liga pro programador...(11) 99567-7878")