def primo(n):
    cont = 0
    i = 1
    while i <= n:
        if n % i == 0:
            cont += 1
        i += 1
    return cont == 2


# n = int(input("Digite o numero: "))
#
# if primo(n):
#     print("É Primo")
# else:
#     print("Não é Primo")

i = 1
n = 1
while i <= 50:
    if primo(n):
        print(n, end=' ')
        i+=1
    n += 1