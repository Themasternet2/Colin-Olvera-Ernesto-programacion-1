##Ejercicio 1##
numero = 7
par= numero % 2 ==0
print("El mumero(",par,")es par")
## Se especifica cada variable y primero es par y luego el numero%2 )

##Ejercicio 2##
numero="5"
numero2="3"
sumatexto= numero + numero2
print(f"sin convertir: {numero} + {numero2} = {sumatexto}")
resultado_con_numero=int(numero)+int(numero2)
print(f"resultado de la suma es {resultado_con_numero}")
##La diferencia entre la version sin convertir y la version con numero es que la primera version al tener los numeros entre "" python los detecta como texto y los agrupa en vez de sumarlos y int lo que hace es que python los detecte como numeros##

##Ejercicio 3##
nombre = "Ernesto"
Edad = 18
Estatura = 1.71
es_estudiante = True
print("Reporte")
print("Nombre:", nombre, type(nombre))
print("Edad:", Edad, type(Edad))
print("Estatura:", Estatura, type(Estatura))
print("Es estudiante:", es_estudiante, type(es_estudiante))
##Extra##
mensaje = "hola soy " + nombre + " y tengo " + str(Edad) + " años y mido " + str(Estatura)
print(mensaje)
##note que si pones un 0 en un numero entero python no lo detecta y solo te suelta los numeros del 1 en adelante##

##Ejercicio 4##
v1 = 5
v2 = 5
print(f" {v1}+{v2} es {v1+v2}")
print(f" {v1}-{v2} es {v1-v2}")
print(f" {v1}*{v2} es {v1*v2}")
print(f" {v1}/{v2} es {v1/v2}")
## las operaciones de dos variables se tienen que usar print(f"etc)si no solo imprimira el texto dentro de los parentesis

##Ejercicio 5##



