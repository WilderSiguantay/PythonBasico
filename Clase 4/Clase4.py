# Ejemplos del FOR

''' - Java - C# - C++
for (int i=0; i < 10 ; i++){
  //declareaciones o bloques de codigo
}
'''

#Sintaxis
#for objetoiterativo in secuencia:
    #declaraciones (if, for, while, metodos, print, funciones)


#Pasos
#1. for
#2. variable que va manejar las iteraciones
#3. secuencia a iterar o recorrer
#4. el area de declaracion, donde se va a manejar cada elemento de la secuencia.

# Ciclo FOR noraml
estudiantes = ["Luis", "Andres", "Andy","Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    print(nombre)

profesor = 'Wilder'

for letra in profesor:
    print(letra)

'''


#The Break
#Detiene toda la iteracion del ciclo.
estudiantes = ["Luis", "Andres", "Andy","Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    if nombre == "Angel":
        break
    
    print(nombre)


'''
#Continue
#detiene la iteracion en curso y si existe otra iteracion continua.
'''
for nombre in estudiantes:
    if nombre == 'Angel':
        continue
    print(nombre)

'''

#Else
#ejecuta un bloque de codigo al finalizar la iteracion del ciclo
estudiantes = ["Luis", "Andres", "Andy","Angel", "Mateo", "Hector", "Sebastian"]

for nombre in reversed(estudiantes):
    print(nombre)
else:
    print('Fin del ciclo!')



#Funcion Range() 

#Itera la cantidad de veces que definamos en el rango empezando desde 0


#print('------SIN LIMITES-------')
#for x in range(5):
 #   print(x)

#Range(limiteinferior, limite superior)
#print('------LIMITE SUPERIOR E INFERIOR-------')
#for x in range(4,5):
 #   print(x)
#print('------LIMITE SUPERIOR, INFERIOR Y PASO-------')
#range(limiteinferior, limiteSuperior,pasoDeIteracion)

#for x in range(2, 30, 5):
 #   print(x)

#ciclos anidados


nombres = ["Luis", "Andres", "Andy",
           "Angel", "Mateo", "Hector", "Sebastian"]

apellidos = ["De Leon", "Peñate", "Monroy",
             "Torcelli", "Hernandez", "Chaclan", "Solares"]
'''
print('------CICLOS ANIDADOS-----')
for nombre in nombres:
    for apellido in apellidos:
        print(nombre, apellido)

'''


#CICLO WHILE

i =1

while i < 6:
    print(i)
    i += 1

#sentencia break

i = 1

print('-----break-----')
while i <6:
    print(i)
    if i ==3:
        break
    i +=1

#sentecia continue

i = 0
print('-----continue-----')
while i <6:
    i +=1
    if i ==3:
        continue
    print(i)
    
#sentencia ELSE

print('--------ELSE--------')

i = 0

while i< 6:
    print(i)
    i +=1
else:
    print('i es mayor que 6')

#While anidados

i=0
j=0

print('-------WHILE ANIDADOS-------')
while i <3:
    while j<3:
        print(i,j)
        j +=1
    i +=1
    j=0


#PARA QUIEN PREGUNTÓ SI SE PUEDE RECORRER EN FORMA INVERSA LES DEJO EL SIGUIENTE ENLACE PARA QUE PUEDAN CHECARLO. 
#https://www.delftstack.com/es/howto/python/python-iterate-list-backwards/