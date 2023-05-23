import math

n = int(input("Digite numero exponte positivo"))
e = 0

for i in range(1,n+1):
    e = e + math.pow(2, i)
    
print(f"o valor do exponte é {e:.2f}")
    

    