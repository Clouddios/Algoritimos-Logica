a=float(input("Digite Lado A: "))
b=float(input("Digite Lado B: "))
c=float(input("Digite Lado C: "))

if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Os lados formam um Triangulo")
    if (a == b == c):
        print("EQUILÁTERO")
    elif(a==b) or (a==c) or (b==c):
            print("ISÓSELES")
    else:
            print("ESCALENO")
else:
    print("Não e triangulo")
