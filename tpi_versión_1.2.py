import random

def jugar_ahorcado():
    """Juego del Ahorcado. Adivina la palabra secreta letra por letra."""
    palabra = input("Escribe la palabra secreta: ").lower()
    print("\n" * 50)
    descubierta = ["_" for _ in palabra]
    intentos = 0
    errores_permitidos = 5

    while intentos < errores_permitidos:
        print(f"Palabra: {' '.join(descubierta)}")
        letra = input("Escribe una letra: ").lower()

        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    descubierta[i] = letra
        else:
            intentos += 1
            print(f"Letra incorrecta. Intentos restantes: {errores_permitidos - intentos}")

        if "_" not in descubierta:
            print(f"¡Ganaste! La palabra era: {''.join(descubierta)}")
            return

    print(f"Perdiste. La palabra era: {palabra}")

def jugar_numero_secreto():
    """Juego del Número Secreto. Adivina un número entre 1 y 100."""
    print("Estoy pensando en un número entre 1 y 100.")
    numero_secreto = random.randint(1, 100)

    while True:
        try:
            intento = int(input("Adivina el número: "))
            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

def menu_principal():
    """Menú principal para elegir los juegos."""
    while True:
        print("""
        1. Jugar Ahorcado
        2. Jugar Número Secreto
        3. Salir
        """)
        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar_ahorcado()
        elif opcion == "2":
            jugar_numero_secreto()
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

menu_principal()
