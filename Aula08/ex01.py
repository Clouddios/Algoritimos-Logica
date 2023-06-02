nome1 = input("Digite seu primeiro nome: ")
nome2 = input("Digite seu nome do meio: ")
nome3 = input("Digite seu ultimo nome: ")
nome1c = ''
nome2c = ''
nome3c = ''

#Cifra de Caesar

for i in range(0, len(nome1)):
    
    nome1c = nome1c + chr(ord(nome1[i])+4)

for i in range(0, len(nome2)):
    
    nome2c = nome2c + chr(ord(nome2[i])+4)
    
for i in range(0, len(nome3)):
    
    nome3c = nome3c + chr(ord(nome3[i])+4)
    #nome3c = nome3c + chr(letra + 4)

print(f"Boa noite {nome1} {nome2} {nome3}")
print(f"Seu nome encryptado é : {nome1c} {nome2c} {nome3c}")