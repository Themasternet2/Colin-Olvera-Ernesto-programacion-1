##Proyecto Final de Programación 
## Integrantes:
## - Mercado Rodriguez Braulio Sebastian 222452258
## Colin Olvera Ernesto 
##Aclaraciones pertinentes: EL proyecto fue realizado en conjunto, el tema de la trivia se basa en el videojuego ZENLESS ZONE ZERO, el cual es un juego de rol de acción desarrollado por miHoYo. La trivia contiene preguntas relacionadas con la historia, personajes y mecánicas del juego. 

##CODIGO FUENTE DEL PROYECTO DE TRIVIA DE ZENLESS ZONE ZERO:

import pgzrun
from pygame import Rect ##Necesario para ejecutar el juego ya que asi le decimos a python que vamos a usar la libreria pgzrun (no lo olvides net)

##Resolucion de la pantalla del juego:
WIDTH = 800 ##800p como prueba tecnica
HEIGHT = 600 ##600p como prueba tecnica

pantalla = "inicio" ##Creo que asi es mas facil de entender que aqui inicia.

# Rect se usa para crear los botones.
boton_jugar = Rect((300, 350), (200, 70))


def dibujar_inicio():
    screen.draw.text("Trivia de Zenless Zone Zero CUGDL",
                     center=(WIDTH / 2, 200), fontsize=56, color="white")
    screen.draw.filled_rect(boton_jugar, "orange")
    screen.draw.text("JUGAR",
                     center=boton_jugar.center, fontsize=40, color="black")


def dibujar_pregunta():
    screen.draw.text("Aquí irá la primera pregunta",
                     center=(WIDTH / 2, HEIGHT / 2), fontsize=40, color="white")


def draw():
    screen.clear()

    if pantalla == "inicio":
        dibujar_inicio()
    elif pantalla == "pregunta":
        dibujar_pregunta()


def on_mouse_down(pos):
    global pantalla

    if pantalla == "inicio" and boton_jugar.collidepoint(pos):
        pantalla = "pregunta"

pgzrun.go()  ##Inicia el juego