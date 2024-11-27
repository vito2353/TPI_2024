import random

print("¡Bienvenido a Play.in!")
while True:
    print("1. Jugar Ahorcado")
    print("2. Jugar Número Secreto")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Juego del Ahorcado
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

            if "_" not in descubierta:
                print(f"¡Ganaste! La palabra era: {''.join(descubierta)}")
                break

        if intentos == errores_permitidos:
            print(f"Perdiste. La palabra era: {palabra}")

    elif opcion == "2":
        # Juego del Número Secreto
        print("Estoy pensando en un número entre 1 y 100.")
        numero_secreto = random.randint(1, 100)

        while True:
            intento = int(input("Adivina el número: "))
            if intento < numero_secreto:
                print("El número es mayor.")
            elif intento > numero_secreto:
                print("El número es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                break

    elif opcion == "3":
        print("¡Gracias por jugar! Hasta luego.")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
