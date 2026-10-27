## Ernesto Colin OLvera##
## mini proyecto 2 caja registradora ##
## codigo de estudiante: 226150949##

print("bienvenido a la caja registradora")
print("AVISO")
print("ingresa el siguiente dato en numero")
numero_productos = (input("ingrese el numero de productos que desea comprar: "))
len(numero_productos) > 0
numero_productos.isdigit()
print(numero_productos.isdigit())

##aqui nos dice cual es el numero de productos a usar y en este ejercicio el codigo esta pensado para que sean dos productos##

nombre_producto = (input("ingrese el nombre del producto: "))
precio_producto = (input("ingrese el precio del producto: "))
cantidad_producto = (input("ingrese la cantidad de producto: "))
precio_producto.isdigit()
print(precio_producto.isdigit())
cantidad_producto.isdigit()
print(cantidad_producto.isdigit())

##el .isdigit nos sirve para determinar si es que el dato ingresado es un numero##

nombre_producto2 = (input("ingrese el nombre del producto: "))
precio_producto2 = (input("ingrese el precio del producto: "))
cantidad_producto2 = (input("ingrese la cantidad de producto: "))
precio_producto2.isdigit()
print(precio_producto2.isdigit())
cantidad_producto2.isdigit()
print(cantidad_producto2.isdigit())
##en esta parte es donde el cliente nos da los datos con los cuales hacemos nuestra operacion y asi sacar el precio final##

subtotal = (float(precio_producto) * int(cantidad_producto)) + (float(precio_producto2) * int(cantidad_producto2))
IVA = subtotal*0.16
precio_total = subtotal + IVA
print(precio_total)
##en esta parte se le suma al precio del subtotal el IVA que seria el 16% de el precio##

##aqui esta el recibo##

total_producto1 = float(precio_producto) * int(cantidad_producto)
total_producto2 = float(precio_producto2) * int(cantidad_producto2)

print("=====================================")
print("            TICKET                   ")
print("            RECIBO DE COMPRA         ")
print("=====================================")
print(f"{cantidad_producto} x {nombre_producto}")
print(f"   Precio unitario: ${float(precio_producto):.2f}")
print(f"   Importe:         ${total_producto1:.2f}")
print("-------------------------------------")
print(f"{cantidad_producto2} x {nombre_producto2}")
print(f"   Precio unitario: ${float(precio_producto2):.2f}")
print(f"   Importe:         ${total_producto2:.2f}")
print("=====================================")
print(f"            SUBTOTAL: ${subtotal:.2f}")
print(f"            IVA (16%): ${IVA:.2f}")
print(f"            TOTAL:    ${precio_total:.2f}")
print("=====================================")
print("        GRACIAS POR SU COMPRA        ")
print("=====================================")
