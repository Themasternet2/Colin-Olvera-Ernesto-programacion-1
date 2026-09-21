import time


def pregunta(texto_pregunta, respuesta_correcta):
    """Bloque personalizado: define Pregunta / Respuesta correcta"""
    respuesta = input(f"{texto_pregunta} ")

    if respuesta_correcta.strip().lower() == respuesta.strip().lower():
        # start sound "Tropical Birds"
        print("[Sonido: Tropical Birds]")

        # clear graphic effects
        color_efecto = 0

        # repeat 10 -> change color effect by 25
        for _ in range(10):
            color_efecto += 25
            # (aquí iría el cambio visual del sprite)

        # next backdrop
        print("[Fondo siguiente]")

        # repeat 10 -> change color effect by -25
        for _ in range(10):
            color_efecto -= 25

        # wait 1 seconds
        time.sleep(1)

        # say "Bien hecho" for 1 seconds
        print("Bien hecho")
        time.sleep(1)

        # say "Muchas gracias por participar en este ejercicio" for 2 seconds
        print("Muchas gracias por participar en este ejercicio")
        time.sleep(2)

    else:
        # say "Error" for 2 seconds
        print("Error")
        time.sleep(2)

        # say "Intentalo de nuevo" for 2 seconds
        print("Intentalo de nuevo")
        time.sleep(2)


def main():
    """Equivalente a: when green flag clicked"""
    # start sound "Seagulls"
    print("[Sonido: Seagulls]")

    # say "Hola" for 2 seconds
    print("Hola")
    time.sleep(2)

    # say "En este ejercicio tendras que contestar una preg..." for 2 seconds
    print("En este ejercicio tendras que contestar una pregunta")
    time.sleep(2)

    # say "Si aciertas pasaremos al siguiente fondo" for 2 seconds
    print("Si aciertas pasaremos al siguiente fondo")
    time.sleep(2)

    # Llamada al bloque personalizado "Pregunta"
    pregunta("Cual es el tiburon mas grande", "Tiburon ballena")


if __name__ == "__main__":
    main()
