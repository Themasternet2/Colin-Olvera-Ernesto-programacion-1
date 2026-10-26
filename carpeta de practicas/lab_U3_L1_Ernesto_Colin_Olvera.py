##Ejercicio 1
##Ernesto Colin Olvera 226150949

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

input("Ingresa el peso del producto en kilogramos" )