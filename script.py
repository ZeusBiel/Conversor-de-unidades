valor = float(input("Insira o valor: "))
origem = input("Insira a origem: ")

if   origem == "km":
        destinoM = input("Selecione a unidade de destino: hm, dan, m, dm, cm, mm: ")
        calc = 10**3

elif origem == "hm":
        destinoM = input("Selecione a unidade de destino: km, dan, m, dm, cm, mm: ")
        calc = 10**2

elif origem == "dan":
        destinoM = input("Selecione a unidade de destino: km, hm, m, dm, cm, mm: ")
        calc = 10**1

elif origem == "m":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, dm, cm, mm: ")
        calc = 10**0

elif origem == "dm":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, m, cm, mm: ")
        calc = 1/10**1

elif origem == "cm":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, m, dm, mm: ")
        calc = 1/10**2

elif origem == "mm":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, m, dm, cm: ")
        calc = 1/10**3

if destinoM == "km":
    calc2 = 10**3

elif destinoM == "hm":
    calc2 = 10**2

elif destinoM == "dan":
    calc2 = 10**1

elif destinoM == "m":
    calc2 = 10**0

elif destinoM == "dm":
    calc2 = 1/10**1

elif destinoM == "cm":
    calc2 = 1/10**2

elif destinoM == "mm":
    calc2 = 1/10**3

final = valor *(calc * calc2)

print(f"Resultado: {final}")
