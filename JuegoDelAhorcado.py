import random


def jugar_ahorcado():
    palabras = ["python", "computadora", "programacion", "algoritmo"]
    palabra = random.choice(palabras)

    vidas = 6
    letras_correctas = []
    letras_incorrectas = []

    print("🎮 Bienvenido al juego del Ahorcado 🎮")

    while vidas > 0:

        # Mostrar palabra oculta
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_correctas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "

        print("\nPalabra:", palabra_mostrada)
        print("Vidas:", vidas)
        print("Letras incorrectas:", letras_incorrectas)

        # Verificar si ganó
        if "_" not in palabra_mostrada:
            print("🎉 ¡Ganaste!")
            return

        intento = input("Ingresa una letra: ").lower()

        # Validación básica
        if len(intento) != 1 or not intento.isalpha():
            print("⚠ Ingresa solo una letra válida")
            continue

        # Si ya la escribió
        if intento in letras_correctas or intento in letras_incorrectas:
            print("⚠ Ya usaste esa letra")
            continue

        # Verificar si está en la palabra
        if intento in palabra:
            print("✅ ¡Letra correcta!")
            letras_correctas.append(intento)
        else:
            print("❌ Letra incorrecta")
            letras_incorrectas.append(intento)
            vidas -= 1

    print("\n💀 Perdiste. La palabra era:", palabra)


jugar_ahorcado()

