def parimpar(n):
    return (n % 2 == 0)


n = int(input("Digite um numero: "))
if parimpar(n):
    print("Numero é Par")
else:
    print("Numero é Impar")