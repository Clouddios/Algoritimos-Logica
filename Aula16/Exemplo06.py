def entrada():
    try:
        num = int(input("informe um número: "))
    except:
        return None
    else:
        return num
    finally:
        print("Fim da execução... ")

a = entrada()
print(a)