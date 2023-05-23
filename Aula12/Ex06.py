def segundos(h=0,m=0,s=0):
    return (h*3600 + m*60 + s)

horas = list(map(int,input().split(":")))

h,m,s = horas[0],horas[1],horas[2]

print(segundos(h,m,s))