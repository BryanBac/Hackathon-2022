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
        opcion = 0
        cadenas = []
        while opcion == 2:
            print("1. Agregar")
            print("2. Salir")
            opcion = int(input("Ingresu su opcion: "))
            if opcion == 1:
                cadena1 = input("Cadena 1: ")
                cadenas.append(cadena1)
        maximo = int(input("Maximo: "))
        #  aquí va ir tu función
        # Parametros: cadenas, maximo
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

