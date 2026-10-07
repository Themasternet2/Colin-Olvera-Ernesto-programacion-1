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