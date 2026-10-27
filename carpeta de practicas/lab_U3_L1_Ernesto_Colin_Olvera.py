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


##Ejercicio 6

compra = int(input("Ingrese el precio del producto "))

if compra > 499:
    print("El articulo tiene 20% de descuento")
    precio_des = compra*0.20
    precio_final = compra-precio_des
    print("El precio des articulo seria ",precio_final)
elif compra >199:
    print("El articulo tiene 10% de descuento")
    precio_des = compra*0.10
    precio_final = compra-precio_des
    print("El precio des articulo seria ",precio_final)
else:
    
    print("En este precio no hay descuento asi que el precio seria ",compra)


##Ejercicio 7

numero = int(input("Ingrese un numero "))

if 1<= numero <=100:
    print("El numero  esta en el rango aceptado ")
else:
    print("El numero no esta en el rango aceptado")


##Ejercicio 8
print("IMPORTANTE")
print("INGRESE LOS DATOS SOLO EN NUMEROS ")
peso = float(input("Ingrese su peso en kg "))
estatura = float(input("ingrese su estatura en metros "))
imc = peso/estatura**2

if imc > 29:
    print("Usted tiene obesidad ,le recomendamos bajar de peso,su imc es ",imc)
elif imc > 24.9 and imc <30:
    print("usted tiene sobrepeso,le recomendamos bajar de peso,su imc es ",imc)
elif imc > 18.5 and imc <25:
    print("usted tiene un peso normal,siga con su forma de vida saludable,su imc es ",imc)
else:
    print("usted tiene bajo peso,le recomendamos que mejore sus habitos alimenticios,su imc es ",imc)
"""

##Ejercicio 9

consumo = float(input("Ingrese el consumo mensual de electricidad en kwh "))

if consumo <150:
    costo=consumo*1.20
elif consumo < 300:
    costo = 150*1.20+(consumo-150)*1.80
else:
     costo = 150 * 1.20 + 150 * 1.80 + (consumo - 300) * 2.50
print("consumo es ",consumo ,"kwh")
print("El costo total es de", costo )