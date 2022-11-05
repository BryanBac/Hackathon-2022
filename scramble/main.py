def comparar_cadenas(cadena1: str, cadena2: str):
    if len(cadena1) != len(cadena2):
        return False
    for letra in cadena1:
        esta = cadena2.rfind(letra)
        if esta == -1:
            return False
    return True

