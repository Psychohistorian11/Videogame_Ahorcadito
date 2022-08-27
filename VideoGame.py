def Ahorcadito():
    IMAGENES = ('''

        +---+
        |   |
            |
            |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
            |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
        |   |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|   |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
        |   |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
        |   |
       /    |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
        |   |
       / \  |
            =========''', '''
    ''')

    palabra = "picadita"
    palabra_minuscula = palabra.lower()
    error = 0
    lista = []
    l_completa = []
    letras_ingresadas = []
    longitud_palabra = len(palabra)
    output_palabra = ["_"] * longitud_palabra
    espacio = ""

    for x in palabra_minuscula:
        lista.append(x)
        l_completa.append(x)

    while error <= 7:
        print(IMAGENES[error], "\n")
        print(' '.join(map(str, output_palabra)))

        letra_ingresada = input("\n Ingresa una letra: ")

        if letra_ingresada in palabra_minuscula:
            for letra in range(len(l_completa)):
                if letra_ingresada == l_completa[letra]:
                    output_palabra[letra] = l_completa[letra]

            for y in lista:
                if y == letra_ingresada:
                    lista.remove(letra_ingresada)

            letras_ingresadas.append(letra_ingresada)
            print(f"la letra {letra_ingresada} se encuentra en la palabra")

            print(f"La lista de las letras ingresadas es -----> {letras_ingresadas}")
            print(f"La lista de letras faltantes por ingresar es ----->{lista}")
            print(f"la palabra completa en una lista es ----->{l_completa}")




        else:
            error += 1
            print("Esa letra no esta en la palabra")
            print(f"has fallado {error} veces")
            if error == 7:
                print(IMAGENES[error], "\n")
                print(output_palabra, "\n")
                print("Has perdido :(")
                break

        if (set(l_completa) == set(output_palabra)):
            print(IMAGENES[error], "\n")
            print(' '.join(map(str, output_palabra)))
            print("Has completado la palabra :)")
            break
