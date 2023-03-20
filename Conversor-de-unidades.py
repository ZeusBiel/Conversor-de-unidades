from unittest import result


valor = float(input("Insira o valor: "))
unidade_origem = input("Insira a origem ")
unidade_destino = input("Insira o destino: ")

def converter_unidade(valor, unidade_origem, unidade_destino):
    if unidade_origem == 'km' and unidade_destino == 'mi':
        resultado = valor / 1.60934
    elif unidade_origem == 'mi' and unidade_destino == 'km':
        resultado = valor * 1.60934
    elif unidade_origem == 'kg' and unidade_destino == 'lb':
        resultado = valor * 2.20462
    elif unidade_origem == 'lb' and unidade_destino == 'kg':
        resultado = valor / 2.20462
    elif unidade_origem == 'm' and unidade_destino == 'ft':
        resultado = valor * 3.28084
    elif unidade_origem == 'ft' and unidade_destino == 'm':
        resultado = valor / 3.28084
    else:
        print("Unidades de medida não suportadas.")
        return None
    return resultado

