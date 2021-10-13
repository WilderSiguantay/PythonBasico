#Esto es un comentario de una linea

'''
Este es un comentario
de 
varias
lineas
'''

#La funcion print se usa a menudo para imprimir variables

print('Hola')

#Python no tiene ningun comando para declarar variables
mivariable = 0
x = 5.10
y = 'Hola Mundo'
x1= 5
y2 = 'David'

#Las variables incluso pueden cambiarse de tipo de datos despues de haberle establecido anteriormente.
x = 5
x = 'Wilder'

print(x)

#Los datos de tipo string o cadena se pueden declarar utilizando comillas simples o comillas dobles.
nombre = 'Wilder'
nombre2 = "Wilder"

print('Nombre 1: ' + nombre + " Nombre 2: " +  nombre2)

#podemos asignar valores a variables multiples en una misma linea
x, y, z = 'Naranja', 'Amarillo', 'Rojo'


#podemos asignar el mismo valor a multiples variables.

x = y = z = 'Naranja'
print(x," ", y," ", z)

#Para combinar texto y variables

print('Nombre 1: ' + nombre + " Nombre 2: " +  nombre2)
print(x," ", y," ", z)

#Si tenemos variables de tipo numero 

x = 5
y = 10

#Si combinamos texto y numero

y = 'Wilder'

#print(x + y)

#Si utilizamos el caracter "," nos permite combinar enteros y texto
print(x,y)

z = "lo que sea"

#cadena = y + " " + str(x) + " " + z

print( y + " " + str(x) + " " + z)


#TIPOS DE DATOS
x = 5

print(x, type(x))

y = 'Wilder'

print(y, type(y))

#Esta es una variable string que luego la cambiamos a tipo int
z = int("5")
print(z, type(z))


#OPERADORES

#operadores aritmeticos
print("------------Operadores Aritméticos---------")
x = 1+1
print(x)
x = 1-1
print(x)
x = 3**2
print(x)
x = 16**(1/2)
print(x)

#Operadores de asignacion
print('--------Operadores de Asignacion--------')

x = 4
print(x)

x +=2
print(x)

x *=3
print(x)

x /=9
print(x)

#Operadores de comparacion

print('--------------Operadores de comparación-----------')

y = 5 > 8
print(y)

x = 1 == 1
print(x)

x = 1 != 1
print(x)

#Operadores Lógicos
print('--------Operadores Lógicos-----')

y = 5 < 8 and 1 == 1
print(y)

y = 5>8 or 1 == 1
print(y)

y  = not(1 != 1)
print(y)

#Funciones nativas de python

x = input('Digite un valor para x: ')

print(x, type(x))
print('El valor que el usuario nos ingresa es: ' + x)




