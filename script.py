valor = float(input("Insira o valor: "))
origem = input("Insira a origem: ")

if   origem == "km":
        destinoM = input("Selecione a unidade de destino: hm, dan, m, dm, cm, mm: ")
        calc = 3

elif origem == "hm":
        destinoM = input("Selecione a unidade de destino: km, dan, m, dm, cm, mm: ")
        calc = 2

elif origem == "dan":
        destinoM = input("Selecione a unidade de destino: km, hm, m, dm, cm, mm: ")
        calc = 1

elif origem == "m":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, dm, cm, mm: ")
        calc = 0

elif origem == "dm":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, m, cm, mm: ")
        calc = -1

elif origem == "cm":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, m, dm, mm: ")
        calc = -2

elif origem == "mm":
        destinoM = input("Selecione a unidade de destino: km, hm, dan, m, dm, cm: ")
        calc = -3

else: print("Unidade de media não suportada: ")

if destinoM == "km":
    calc2 = 3

elif destinoM == "hm":
    calc2 = 2

elif destinoM == "dan":
    calc2 = 1

elif destinoM == "m":
    calc2 = 0

elif destinoM == "dm":
    calc2 = -1

elif destinoM == "cm":
    calc2 = -2

elif destinoM == "mm":
    calc2 = -3

else: print("Unidade de medida não suportada: ")

if calc > calc2:
    final = valor * (10**(calc - calc2))

elif calc < calc2:
    final = valor / (10**(calc + calc2))

print(f"Resultado: {final} {destinoM}")
