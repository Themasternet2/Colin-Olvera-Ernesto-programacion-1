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


for fila in range(3):       #columna hace 3 iteraciones y fila hace las mismas 3 interacciones
    for columna in range(3):
        print("*", end="")                #end="" evita que se haga un salto de linea 
    print()

