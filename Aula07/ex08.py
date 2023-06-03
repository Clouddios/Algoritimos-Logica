def primo(n):
    if n>=1:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True
            
n = int(input("Digite um valor: "))

if n > 1:
    if primo(n):
        print(f"{n} é primo")
    else:
        print(f"{n} não é Primo")