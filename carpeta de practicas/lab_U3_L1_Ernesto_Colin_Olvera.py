##Ejercicio 1
##Ernesto Colin Olvera 226150949

"""""
edad = int(input("Ingrese su edad "))
if edad >18: 
    print("es un adulto ")
elif edad >13:
    print("es un adolecente")
else:
    print("es un niño")

##Ejercico 2


usuario = input("ingrese el usuario  " )
contraseña = input("ingrese la contraseña  " )
if usuario == "net" and contraseña == "sunna":
    print("acceso concedido")
elif usuario == "net" and contraseña != "sunna":
    print("contraseña incorrecta")
else:
    print("usuario no encontrado")

##! se usa para decir que es diferende de !=



##Ejercicio 3

kg=int(input("Ingresa el peso del producto en kilogramos " ))
if kg > 10:
    print("El paquete cuesta $135 por el descuento del 10%")
elif kg > 5:
    print("El paquete cuesta $150")
elif kg >1:
    print("el paquete cuesta $90")
elif kg >0:
    print("el paquete cuesta $50")
else:
    print("dato invalido")


##Ejercicio 4

temperatura = int(input("Ingrese la temperatura del ambiente en grados "))
if temperatura >24:
    print("La temperatura muestra que hace calor")
elif temperatura >9 and temperatura < 25:
    print("La temperatura muestra que esta templado")
elif temperatura < 10:
    print("La temperatura es fria")
else:
    print("Dato invalido")

##Ejercicio 5

calificacion = int(input("ingrese la calificacion "))
if calificacion >89:
    print("La calificacion es A")
elif calificacion > 79:
    print("La calificacion es B")
elif calificacion > 69:
    print("La calificacion es C")
elif calificacion > 59:
    print("La calificacion es D")
else:
    print("La calificacion es F")
"""

##Ejercicio 6

compra = int(input("Ingrese el precio del producto "))

if compra > 499:
    print("El articulo tiene 20% de descuento")
    precio_des = compra*0.20
    precio_final = compra-precio_des
    print("El precio des articulo seria ",precio_final)
