from math import sqrt, pow

numero=float(input("Numero: "))

if numero > 0:
    print(f"Quadrado:  {pow(numero,2)}")
    print(f"Cubo: {pow(numero,3)}")
    print(f"Raiz²: {sqrt(numero)}")
else:
    print("Numero MENOR que 0")
