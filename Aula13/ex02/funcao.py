import random
from time import sleep

def dados():
    print("ROLANDO DADOS")
    j1 = random.randint(1,6)
    print(f"Você tirou {j1}")
    print("Agora e minha vez...")
    
    for i in range(1,4):
        print(".",end="")
        sleep(0.5)
        
    cpu = random.randint(1,6)
    print(f"CPU tirou {cpu}")
    
    if j1 > cpu:
        res = "Ganhou!"
    elif cpu > j1:
        res = "Perdeu!"
    else:
        res = "Empatou"
        
    print(f"Você {res}: Você - {j1} | CPU - {cpu}")
    
    c = input("Deseja jogar novamente ?: s/n ").lower()
    
    if c == 's':
        dados()