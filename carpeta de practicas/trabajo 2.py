##Ejercicio 1##
nombre = "belle"
edad = 24
ciudad = "Nueva eridu"
print (nombre,ciudad,edad)
##necesito mas tiradas##

##Ejerecicio 2##
contador=0
contador=contador+1
print(contador)
contador=contador+1
print(contador)
contador=contador+1
print(contador)
contador=contador+1
print(contador)
##5 y solo control c y v##

##Ejercicio 3##
CONSTANTE=2.54
pulgada=10  
print("la medida en cm es:", pulgada*CONSTANTE)
##ojala si este bien##

##Ejercicio 4##
Base=5
Altura=10
Area=Base*Altura
print("El área es:", Area)
##Solo multiplica##

##Ejercicio 5##
IVA=0.16
precio=float(input("Ingrese el precio: "))
preciofinal=precio+(precio*IVA)
print("El precio con IVA es:", preciofinal)
##Input guarda datos##

##Ejercicio 6##
A=7
B=6
temp=A
temp=B
print(A,B)
print(B,A)
##solo era print???##

##Ejercicio 7##
v1=43
v2=17.7
v3= "megumin"
v4=True
int(v4)
float(v2)
str(v3)
bool(v1)
print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

##En los parentesis van las variables ,para print solo es type(variable)##

##Ejercicio 8##
texto = "25"
numero_convertido = int(texto)

print("Texto original:", texto, "->", type(texto))
print("Convertido a entero:", numero_convertido, "->", type(numero_convertido))

# 2. Conversión de entero a texto con str()
numero = 100
texto_convertido = str(numero)

print("Número original:", numero, "->", type(numero))
print("Convertido a texto:", texto_convertido, "->", type(texto_convertido))
##pedir asesoria a la maestra##

##Ejercicio 9 ##
S = 3
C = 4
P = S+C
print(P)
S=3
C=4
class mayor:
	"""Determina si el primer valor es mayor que el segundo."""

	@staticmethod
	def comparar(valor_a, valor_b):
		return valor_a > valor_b


mayor_es_v = mayor.comparar(S, C)
print(mayor_es_v)
##ayuda maestra no entendi##