import math


def justificar_textos(cadena, maximo):
    contador = 0
    # print(len(cadena))
    for enunciado in cadena:
        solo_palabras = enunciado.split()
        if contador != (len(cadena)-1):
            # print(solo_palabras)
            contador += 1
            letras_por_palabra = 0
            for i in solo_palabras:
                letras_por_palabra = letras_por_palabra + len(i)
            espacios_faltantes = maximo - letras_por_palabra
            espacios = math.ceil(espacios_faltantes / len(solo_palabras))
            # print(espacios_faltantes / len(solo_palabras))
            # print(espacios)
            nueva_cadena = ''
            if len(solo_palabras) == 2:
                espacios_a_agregar = ""
                for conteo in range(1, espacios*2):
                    espacios_a_agregar = espacios_a_agregar + ' '
                nueva_cadena = solo_palabras[0] + \
                    espacios_a_agregar + solo_palabras[1]
            elif len(solo_palabras) == 1:
                espacios_a_agregar = ""
                for conteo in range(0, espacios):
                    espacios_a_agregar = espacios_a_agregar + ' '
                nueva_cadena = solo_palabras[0] + \
                    espacios_a_agregar
            else:
                for i in range(0, len(solo_palabras)):
                    if i != len(solo_palabras) - 1:
                        nueva_cadena = nueva_cadena
                        espacios_a_agregar = ''
                        for conteo in range(0, espacios):
                            espacios_a_agregar = espacios_a_agregar + ' '
                        solo_palabras[i] = solo_palabras[i] + \
                            espacios_a_agregar
                        nueva_cadena = nueva_cadena + solo_palabras[i]
                    else:
                        nueva_cadena = nueva_cadena + solo_palabras[i].rjust(6, ' ') 
        else:
            nueva_cadena = ""
            for palabra in solo_palabras:
                nueva_cadena = nueva_cadena + palabra

        print(nueva_cadena)
        
        


justificar_textos(
    ["hola amigos mundo", "uno", "como les va a todos", "malos dias", "aquí va otra"], 20)
