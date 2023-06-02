number_string = input("Digite nove caracteres numéricos: ")

if len(number_string) != 9:
    print("A string precisa ter nove caracteres numéricos.")
else:
    if not number_string.isdigit():
        print("A string deve conter apenas caracteres numéricos.")
    else:
        number = float(number_string)
        
        integer_part = int(number)
        decimal_part = round((number - integer_part) * 100)

        formatted_string = f"{integer_part:,}.{decimal_part:02}"
        print(formatted_string)