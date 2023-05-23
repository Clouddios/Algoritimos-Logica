def primo(n):
    if n>=1:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True
            
def impprimo(n):
    primos = []
    for i in range(0,n+1):
        if primo(i):
            primos.append(i)
    
    return(primos)
            
n = int(input("Digite um valor: "))

if n > 1:
    if primo(n):
        print(f"{n} é primo")
    else:
        print(f"Não é Primo")

soma = 0

listaprimos = impprimo(n)     
for i in range(0, n+1):
    if primo(i):
        soma += i

print(listaprimos)
print(f"Soma do numeros primos é {soma}")