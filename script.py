# Variáveis usadas
valor = input("Insira o valor: ")
while not valor.replace('.', '', 1).isdigit():
    print("Valor inválido, insira apenas números.")
    valor = input("Insira novamente o valor: ")
valor = float(valor)
calc = 0
calc2 = 0
final = 0
destinoM = "Undefined"
origem = "Undefined"

# Lista de unidades de medida válidas
unidades_validas = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

# Loop para verificar a unidade de medida de origem
origem = input("Insira a unidade de medida de origem: ")
while origem not in unidades_validas:
    print("Unidade de medida não suportada.")
    origem = input("Insira novamente a unidade de medida de origem: ")

# Loop para verificar a unidade de medida de destino
destinoM = input(f"Insira a unidade de medida de destino: {', '.join([unidade for unidade in unidades_validas if unidade != origem])}: ")
while destinoM not in unidades_validas or destinoM == origem:
    print("Unidade de medida não suportada ou igual à unidade de medida de origem.")
    destinoM = input(f"Insira novamente a unidade de medida de destino {', '.join([unidade for unidade in unidades_validas if unidade != origem])}: ")

# Atribuição dos valores para o cálculo final
if origem == "km":
    calc = 3
elif origem == "hm":
    calc = 2
elif origem == "dam":
    calc = 1
elif origem == "m":
    calc = 0
elif origem == "dm":
    calc = -1
elif origem == "cm":
    calc = -2
elif origem == "mm":
    calc = -3

# Atribuição dos valores para a segunda parte do cálculo final
if destinoM == "km":
    calc2 = 3
elif destinoM == "hm":
    calc2 = 2
elif destinoM == "dam":
    calc2 = 1
elif destinoM == "m":
    calc2 = 0
elif destinoM == "dm":
    calc2 = -1
elif destinoM == "cm":
    calc2 = -2
elif destinoM == "mm":
    calc2 = -3

# Cálculo final
if calc > calc2:
    final = valor * (10**(calc - calc2))
elif calc < calc2:
    final = valor / (10**(calc2 - calc))

print(f"Resultado: {final} {destinoM}")
