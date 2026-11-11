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
"""""

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
