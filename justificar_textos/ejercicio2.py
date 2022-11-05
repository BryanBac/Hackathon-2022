import math

def justificar_textos(cadena, maximo):
    for enunciado in cadena:
        solo_palabras = enunciado.split()
        # print(solo_palabras)
        letras_por_palabra = 0
        for i in solo_palabras: 
            letras_por_palabra = letras_por_palabra + len(i)
        espacios_faltantes = maximo - letras_por_palabra
        espacios = math.ceil(espacios_faltantes / len(solo_palabras))
        print(espacios_faltantes / len(solo_palabras))
        print(espacios)
        nueva_cadena = ''
        for i in range(0,len(solo_palabras)):
            if i != len(solo_palabras) - 1:
                nueva_cadena = nueva_cadena
                espacios_a_agregar = ''
                for conteo in range(0,espacios):
                    espacios_a_agregar = espacios_a_agregar + ' ' 
                solo_palabras[i] = solo_palabras[i] + espacios_a_agregar
                nueva_cadena = nueva_cadena + solo_palabras[i]
            else:
                nueva_cadena = nueva_cadena + solo_palabras[i]
        print(nueva_cadena)



    
justificar_textos(["hola amigos mundo","malos dias"], 20)