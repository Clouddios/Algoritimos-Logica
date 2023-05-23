def pesecabecas(cab):
    
    pes = float(cab * 3 + 1)
    
    coelhos = (pes - 2 * cab)/2
    patos = cab - coelhos
    
    return coelhos, patos
      
        
    
cabe = float(input("Digite total de cabeças: "))

coelhos, patos = pesecabecas(cabe)

print(f"Total de {coelhos} coelhos \nTotal de {patos} patos")