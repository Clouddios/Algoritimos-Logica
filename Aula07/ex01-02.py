b = int(input("Digite um numero B: "))
N = int(input("Digite um numero N: "))

E=0

for i in range(1, N+1):
    E += b**i

print(E)