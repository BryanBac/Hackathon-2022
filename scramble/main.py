def comparar_cadenas(cadena1: str, cadena2: str):
    if len(cadena1) != len(cadena2):
        return False
    for letra in cadena1:
        esta = cadena2.rfind(letra)
        if esta == -1:
            return False
    return True


print(comparar_cadenas("eva", "ae3v"))  # Con más caracteres en la segunda
print(comparar_cadenas("eva", "aev"))  # Cadenas validas
print(comparar_cadenas("eva", "ava"))  # Cadenas no iguales
print(comparar_cadenas("bryan", "byr"))  # Con más caracteres en la primera
