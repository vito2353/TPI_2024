import random 

# Función para el juego del Ahorcado
def jugar_ahorcado():
    
    #El jugador debe adivinar una palabra letra por letra antes de alcanzar el límite de errores
    
    print("¡Bienvenido al juego del Ahorcado!")
    palabra = input("Escribe la palabra secreta").lower()
    print("\n" * 50)  # Limpia la pantalla para ocultar la palabra ingresada
    errores_permitidos = 5
    intentos = 0
    cadenanueva_guiones = "_" * len(palabra)  # Cadena con guiones bajos que representa las letras no descubiertas
    descubierta = list(cadenanueva_guiones)  # Lista mutable de la palabra oculta

    while intentos < errores_permitidos:
        print(f"Palabra: {''.join(descubierta)}")
        letra = input("Escribe una letra: ").lower()

        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    descubierta[i] = letra  # Reemplaza los guiones por la letra correcta
            print("¡Adivinaste una letra!")
        else:
            intentos += 1
            print(f"Letra incorrecta. Te quedan {errores_permitidos - intentos} intentos.")

        # Verificar si se adivinó toda la palabra
        if "_" not in descubierta:
            print(f"¡Felicidades! Adivinaste la palabra: {''.join(descubierta)}")
            return

    # Si se se acaban los intentos
    print(f"Lo siento, perdiste. La palabra era: {palabra}")


# Función para el juego del Número Secreto
def jugar_numero_secreto():

    #El jugador debe adivinar un número entre 1 y 100
    
    print("¡Bienvenido al juego del Número Secreto!")
    print("Adivina un número aleatorio entre 1 y 100")
    numero_secreto = random.randint(1, 100)

    while True:
        intento = input("Ingresa tu número (o escribe 'salir' para terminar): ")

        if intento.lower() == "salir":
            print(f"El número secreto era {numero_secreto}. ¡Gracias por jugar!")
            break

        try:
            intento = int(intento)
            if intento < numero_secreto:
                print("El número secreto es mayor.")
            elif intento > numero_secreto:
                print("El número secreto es menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Menú principal
def menu_principal():
    
   #Permite al jugadro elegir a que juego jugar o salirse
    
    while True:
        print("""
**************************************
         ¡Bienvenido a .learn!
**************************************
Elige el juego que quieres jugar:
1 - Ahorcado
2 - Número Secreto
3 - Salir
**************************************
        """)
        opcion = input("Ingresa tu opción: ")

        if opcion == "1":
            jugar_ahorcado()
        elif opcion == "2":
            jugar_numero_secreto()
        elif opcion == "3":
            print("¡Gracias por jugar con Play.in!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
