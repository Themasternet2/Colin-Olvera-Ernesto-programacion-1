"""""
precio = 100
descuento =0.10
iva = 0.16
total = (precio - precio) * descuento + precio * iva
print(total)

edad_texto = input("edad:")
edad = int(edad_texto)
print(edad+1) 

edad = input("Edad:")
print(type(edad))
#<class ´str´> - aunque el usuario escriba numeros

nombre = "ana"
print("hola,", nombre)

precio = 19.5
print("precio: $" + str(precio))

precio = 19.5
print(f"precio: ${precio}")

total = 149.6789
print(f"total: $ {total:.1f}")
#total: $ 149.68 - dos decimales

nombre = "ana"
nota = 95
print(f"alumno:{nombre}- nota:{nota}")

total = 149.999
print(f"total: ${total:.2f}")

print("a", "b")   #a,b
print("a", "b", sep="*")  #a-b

print("cargando",end="")
print("...listo")
#cargando...listo (una sola linea)

edad = int((input("edad:")))
suma = (edad + 1)
print("el proximo año tendras", edad + 1,"años")

nombre = input("como te llamas:")
print(f"hola, {nombre}")

##int sirve para guardar datos numericos y no los guarde como texto/variable 

nombre = "ana" 
print("hola,", nombre)

##p2f funciona para controlar los decimales de lo que imprimas
##strip elimina los espacios extraq al inicio y fin de un texto

dato = input("escribe un numero: ")
print(dato.isdigit())

##esto controla que el usuario ingrese un numero

dato = input("tu nombre: ")
print(len(dato) > 0)

## len revisa la longitud de las respuestas
print("7".isdigit()) #true
print("siete".isdigit()) #false
print("-7".isdigit()) #false

#.isdigit() revisa si es verdadero o falso y si es digito o no
115/2
print(115/2)
115%2
print(115%2)

dato = input("escribe un numero par: ")
print(int(dato) % 2 == 0)

dato = int(input("escribe tu edad: "))
es_valida = len(str(dato)) > 0 and str(dato).isdigit() and dato < 100 and dato > 0
print(f"¿edad válida? {es_valida}")
"""""
##if=si entonces
##else = si no
##elif = si y no entonces
## ejemplo:

x=10.1
if x > 10:
    print("x es mayor que y")
else:
    print("x no es mayor que y")

##elif ejemplo

x= 5
y= 5
if x >y:
    print("x es mayor")
elif x < y:
    print("y es mayor")
else:
    print("son iguales")

##90 o mas = a
##70 0 mas = b
##menos de 70 =c

nota = 67
if nota > 90:
    print("A")
elif nota > 70:
    print("B")
else:
    print("C")

z = 11
c=0 >= z >=10
print(c)

## 0 <= x <=10 es igual a x >= 0 and x <= 10

temp= 67
if temp < 10:
    print("frio")
elif temp <25:
    print("templado")
else:
    print("calor")


cantidad2 = 150
if cantidad2 > 100:
    print("20% de descuento")
elif cantidad2 > 50:
    print("10% de descuento")
else:
    print("sin descuento")

cantidad = int(input("ingrese cantidad: "))
if cantidad > 100:
    print("20% de descuento  ")
    precio_des= cantidad*0.20 
    precio_final= cantidad-precio_des
    print(precio_final)
elif cantidad > 50:
    print("10% de descuento  ")
    precio_des = cantidad*0.10
    precio_final = cantidad-precio_des
    print(precio_final)
else:
    print("sin descuento")
