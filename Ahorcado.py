# AHORCADO
# Librerías
import random

# FUNCIONES
# Función "clear", necesitaba una función que hiciese parecer que se borra la consola
def clear():
    # Realiza un 10000 saltos de línea
    print ("\n" * 10000)

# Función para revelar los caracteres de puntuación y las letras adivinadas
def caracteres_conseguidos():
    palabra_guiones = "" # String al que añadiremos la frase "cifrada"
    for i in range(len(frase)): # Un "for" que se repite el mismo número de veces que la longitud de la frase
        if frase[i] in ["¡","!","¿","?",":",";","-",".",","," ","@","<",">","'",'"',"%","(",")"] or frase[i] in letras_adivinadas: # Si en la posición [i] hay un caracter de puntuación o una letra dentro de nuestra base de datos
            palabra_guiones = palabra_guiones + frase[i] # Añadiremos el carácter a la frase
        else:
            palabra_guiones = palabra_guiones + "_" # En caso contrario esconderemos el carácter con "_"
    
    return palabra_guiones # Devolvemos la frase cifrando los carácteres que aun no se han descubierto

# Función para calcular el número de carácteres que faltan por descubrir
def caracteres_faltantes():
    count_caracteres_faltantes = 0

    for i in range(len(frase)): # Se repetiré el mismo número de veces que la longitud de la frase
        if caracteres_conseguidos()[i] == "_": # Utilizando la anterior función, si hay una "_" se sumará "1" a la variable
            count_caracteres_faltantes = count_caracteres_faltantes + 1

    return count_caracteres_faltantes # Devolvemos el número de caracteres sin descubrir

# Función para no tener que poner los monigotes en mitad del código
def monigote(vidas):
    if vidas == 6:
        dibujo = " ___________\n| /\n|/\n|\n|"
    elif vidas == 5:
        dibujo = " ___________\n| /        😵\n|/\n|\n|"
    elif vidas == 4:
        dibujo = " ___________\n| /        😵\n|/         👙\n|\n|"
    elif vidas == 3:
        dibujo = " ___________\n| /        😵\n|/       💪👙\n|\n|"
    elif vidas == 2:
        dibujo = " ___________\n| /        😵\n|/       💪👙💅\n|\n|"
    elif vidas == 1:
        dibujo = " ___________\n| /        😵\n|/       💪👙💅\n|           👠\n|"
    elif vidas == 0:
        dibujo = " ___________\n| /        😵\n|/       💪👙💅\n|         🔧👠\n|"
    return dibujo

# Array con frases
lista_frases = ["mi entretenimiento favorito es ir donde nunca he estado.","cuando se te ofrezca una gran aventura, no la rechaces.","siempre son los aventureros los que consiguen grandes cosas.","no hagas planes pequeños. no tienen magia... haz planes grandes, apunta alto con esperanza y trabajo.","hay lugares donde uno se queda y lugares que quedan en uno.","la cura para todo es siempre agua salada: el sudor, las lagrimas o el mar.","ve mundo. es mucho mas fantastico que cualquier sueño","viajar te deja sin palabras y despues te convierte en un narrador de historias.","la vida, o es una aventura o no es nada.","siempre nos encontraremos a nosotros mismos en el mar.","no viajamos para escapar de la vida, sino para que la vida escape de nosotros.","no soy la misma despues de haber visto la luna brillar en el otro lado del mundo.","si piensas que la aventura es peligrosa, prueba la rutina. es mortal."]

decision_fin = 1
while decision_fin == 1: # Mientras esta variable no cambie, el juego se repetirá infinitamente (Al final del código se puede cambiar)
    # Variables globales
    vidas = 6 # Vidas del jugador
    letras_adivinadas = [] # Una array donde guardaremos las letras que el jugador va probando
    fin = False # Necesario para poder usar la opción 3 más abajo
    
    clear()
    
    decision = 0
    while decision not in [1,2,3]: # Mientras no elija una de las 3 opciones, se repetirá infinitamente
        #Menú
        print("=========================")
        print("   Juego del ahorcado    ")
        print("=========================")
        print("1. Pulsa 1 si quieres escribir tu la frase.")
        print("2. Pulsa 2 si prefieres usar una frase aleatoria de la base de datos.")
        print("3. Pulsa 3 si quieres cerrar el programa.")

        #Decisiones
        decision = int(input("Tu decisión es: "))
        if decision == 1:
            frase = input("Escribe la frase que deseas usar: ")
            lista_frases = lista_frases + [frase] # Se guardará la frase en el array de frases

        elif decision == 2:
            frase = lista_frases[random.randint(0, len(lista_frases))]

        elif decision == 3:
            print("Nos vemos.")
            fin = True
            frase = "Nada" # Necesario para que no salte un error
            decision_fin = 2
        else:
            print("ERROR, solo existen las opciones 1, 2 y 3.")
            fin = True # Necesario para poder usar la opción 3

    clear()
    #Main
    # Mientras se haya escogido la opción 1 o 2, no se hayan descubierto todos los carácteres y el jugador tenga vidas.
    while fin == False and caracteres_faltantes() > 0 and vidas > 0:

        # Información sobre la partida
        print("Tienes",vidas,"vidas. \nQuedan",caracteres_faltantes(),"carácteres. \nLetras utilizadas:",letras_adivinadas)
        print(monigote(vidas))
        print(" ",caracteres_conseguidos())

        letra = input("Introduce una letra: ")
        clear()

        if letra not in letras_adivinadas: # Si la letra no está en el array que las almacena
        
            i = 0
            while i < len(frase): # Recorremos cada carácter de la frase, utilizo un "while" porque si encuentra el carácter puede parar de buscar, lo añado al array y así minimizaré la carga
                if frase[i] == letra: # Si el caracter de la frase y la letra son el mismo
                    letras_adivinadas = letras_adivinadas + [letra] # Se añade la letra al array
                    i = len(frase) # Cerramos el "while"
                    print("Letra encontrada.\n")
                i = i + 1
                
            if letra not in letras_adivinadas: # Si no se ha encontrado la letra en el "while" anterior, y por lo tanto no se ha añadido al array
                vidas = vidas - 1 # Se le descuenta 1 vida al jugador
                letras_adivinadas = letras_adivinadas + [letra] # Se añade la letra al array para que el jugador no la repita
                print("Has fallado.\n")
        else: # En caso de que repita letra mostrará este mensaje
            print("Ya has utilizado esta letra. Escribe una diferente.\n")

    print(monigote(vidas),"\n")
    if caracteres_faltantes() == 0: # Si no quedan caracteres por descubrir
        print("======================================")
        print("Felicidades, has descubierto la frase:",caracteres_conseguidos())
        print("======================================\n")
        

    elif vidas == 0: # Si se a quedado sin vidas
        print("===================================")
        print("No lo has conseguido. La frase era:",frase)
        print("===================================\n")        

    if decision_fin != 2:
        decision_fin = 0
        while decision_fin not in [1,2]: # Mientras no se escoja la opción 1 o 2, se repetirá infinitamente
            print("Quieres volver a jugar?")
            print("1. Pulsa 1 si quieres volver a jugar.")
            print("2. Pulsa 2 si quieres cerrar el juego.")

            decision_fin = int(input("Tu decisión es: "))
            clear()

            if decision_fin not in [1,2]:
                print("ERROR, solo existen las opciones 1 y 2.\n")
