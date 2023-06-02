vetor = input("Digite os elementos do vetor separados por espaço: ").split()

e_palindromo = vetor == vetor[::-1]

if e_palindromo:
    print("O vetor é um palíndromo.")
else:
    print("O vetor não é um palíndromo.")