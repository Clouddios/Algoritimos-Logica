somaalt=0
somapeso=0
altura=0
peso=0
imc=0
imcmaior=0
imcmenor=0

for i in range(1,3):
    altura = float(input(f"Digite a {i}a. Altura:"))
    peso = float(input(f"Digite a {i}a. Peso:"))
    
    imc = (altura*altura)/peso
    somaalt=somaalt + altura
    somapeso = somapeso + peso
    
    if imc >= imcmaior:
        imcmaior = imc
    if imc <= imcmenor:
        imcmenor = imc

print(f"Media da altura é {somaalt/i}")
print(f"Media da peso é {somapeso/i}")
print(f"Maior IMC é {imcmaior}, Menor IMC é {imcmenor}")
