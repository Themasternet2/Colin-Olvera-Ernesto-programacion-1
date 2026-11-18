"""""
notas = [8,9,7,6] 
notas.append(10)                             #inserta al final
notas.remove(6)                           #elimina la reprobatoria
print(7 in notas)                        #busca si existe en la lista
print(notas)

salon =[                                  #derecha = columna izquierda = fila

    ["ana","luis"],
    ["eva","ivan"]

]
print(salon)
print(salon[1][0])                     #fila 1, columna 0
salon[0][1] = "carla"                  #reemplaza un alumno
print(salon)


for fila in range(3):  
    for columna in range(3): 
        print("*", end="")                                   #end="" evita que se haga un salto de linea 
    print()

for fila in range(1, 3):
    for columna in range(1, 3):
        print(fila,columna)

for i in range(1, 4):
    for j in range(1, 4):
        resultado = i * j
        print(i, "x", j, "=", resultado)


numeros = [4,9,-2,7,-5]
for n in numeros:
    if n < 0:
        print("encontrado:", n)
        break

for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n)

alumno = {"nombre": "Ana","edad":20,"carrera":"creatividad"}
print(alumno["nombre"])  #claves
alumno["edad"]=21  #alumno
print(alumno)
alumno["promedio"]=9.5 #inserta
del alumno["carrera"]  #elimina
print(alumno)

"""""
def es_mayor_de_edad(edad):   ##def se usa para para deficinir una funcion como si fuera una constante 
    return edad >= 18
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))

board = [[" " for _ in range(3)] for _ in range(3)]
def print_board(board):
    print("\n")
    for row in board:
        print("|".join(row))
        print("-"*5)

print_board(board)

def duplicar(numero):
    return numero *2

resultado = duplicar(5)
print(resultado)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] ==
player for i in range(3)):
        return True
    return False


import random 
numero = random.randint(1, 10)
print(numero)

import math

print(math.sqrt(16))

from random import choice

opciones = ["piedra", "papel", "tijeras"]
print(choice(opciones))

import random

numero_secreto = random.randint(1, 137500)
print("adivina un numero entre 1 y 137500")
print(numero_secreto)

import math

radio = 5
area = math.pi * radio **2
print(f"area del circulo:{area:.2f}") 
# buscar la documentacion de python en su pagina