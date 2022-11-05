def cambiar_cadenas(cadena1: str, cadena2: str):
    cadenas = []
    cambio = cadena2
    cadena2 = cadena1
    cadena1 = cambio
    cadenas.append(cadena1)
    cadenas.append(cadena2)
    return cadenas


def subsecuencia(cadena1: str, cadena2: str):
    if len(cadena1) > len(cadena2):
        cambio = cambiar_cadenas(cadena1, cadena2)
        cadena1 = cambio[0]
        cadena2 = cambio[1]
    contador = 0
    cadena = ""
    for letra in cadena1:
        if letra == cadena2[contador]:
            cadena = cadena + cadena1[contador]
        contador += 1
    return cadena


print(subsecuencia("fsnutno", "tsmunio"))
print(subsecuencia("nutno", "tsmunio"))
print(subsecuencia("fsnutnoxc", "tsmun"))
print(subsecuencia("byron", "bryan"))
