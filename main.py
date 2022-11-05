from cadenas_subsecuentes.main import subsecuencia
from scramble.main import comparar_cadenas
from abuela.ejercicio4 import give_cookies


menu: int = 0
while menu != 5:
    print("#### Menu ####")
    print("1. Scramble")
    print("2. Justificador de Texto")
    print("3. Cadenas Subsecuentes")
    print("4. Abuela Binaria")
    print("5. Salir")
    menu = int(input("Ingrese su opcion: "))
    if menu == 1:
        cadena1 = input("Cadena 1: ")
        cadena2 = input("Cadena 2: ")
        print(f"¿Son cadenas con los mismos caracteres? \n {comparar_cadenas(cadena1, cadena2)}")
    elif menu == 2:
        print("###")
    elif menu == 3:
        cadena1 = input("Cadena 1: ")
        cadena2 = input("Cadena 2: ")
        print(f"Su cadena subsecuente es: {subsecuencia(cadena1, cadena2)}")
    elif menu == 4:
        total = int(input("Total: "))
        numero1 = int(input("Numero 1: "))
        numero2 = int(input("Numero 2: "))
        give_cookies(total, numero1, numero2)
    elif menu == 5:
        print("Se me cuidan")
    else:
        print("Ingrese una opción valida")

