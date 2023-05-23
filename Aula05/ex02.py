nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))

media=(nota1+nota2+nota3)/3

if media>=7.0 or media>10.0:
    print(f"APROVADO, sua media e {media}")

elif media==0 or media<3.0:
    print(f"REPROVADO, sua media e {media}")

else:
    print(f"EXAME, sua media e {media}")
    nota=12-media

    print(f"Você precisa tirar no minimo {nota}")
    exame=float(input("Nota EXAME: "))
    media=(exame+media)/2

    if media>=7.0:
        print(f"APROVADO, Nota {media}")
    else:
        print(f"REPROVADO, Nota {media}")

