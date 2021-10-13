#Ejemplo de If

'''
a = 300
b = 200

if a < b:
    print('A es mayor que B')
    print('A es igual a: ' , a)
    print('B es igual a: ' , b)
    


print('Bloque 0')

#IDENTACION EN PYTHON
#Python utiliza la sangría o identacino para indicar un bloque de código.

#Bloque 0
if 5 > 2:
    #Bloque 1 adentro del bloque 0
    print('5 es mayor a 2')

    #Bloque 2 adentro del bloque 0
    if 3 < 2 :
        #Bloque 1 adentro del bloque 2 del bloque 0
        print('Hola desde el bloque 1, del bloque 2 que está adentro del bloque 0')

    #Bloque 3 adentro del bloque 0
    print('Hola desde el bloque 3 adentro del bloque 0')

#Bloque 1
print('Hola desde el bloque 1')


#ELIF

a = 40
b = 50

if a > b:
    print('A es mayor que B')
elif a == b:
    print('A es igual a B')
elif a < b:
    print('A es menor a B')

b = 3 > 4 #devuelve true
print(b)

tengoSueno = True

if tengoSueno:
    print('Tengo sueño')


#Ejemplos de ELSE

x = 23
y = 23

if x < y:
    print('Y es mayor que X')
elif x > y:
    print('Y es menor que X')
else:
    print('Y es igual que X')
'''

#Ejemplos de AND


'''
El AND FUNCIONA COMO LA MULTIPLICACION
0 * 0 = 0
0 * 1 = 0
1 * 0 = 0
1 * 1 = 1
------------
1 = true
0 = false
------------
'''

x = 20
y = 20
z = 20
'''

print('-------CONDICION AND --------')
if x == y and x != z: # true -- # false
    print('Esta condición se cumple')
else:
    print('Esta condición no se cumple') 

'''

#EJEMPLOS DE OR

'''
EL OR FUNCIONA COMO LA SUMA
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 1
------------
1 = true
0 = false
------------
'''

print('------------CONDICION OR-------------')
x = 20
y = 20
z = 20

''' 
if x > y or x != z: # false -- # false
    print('Esta condición se cumple')
else:
    print('Esta condición no se cumple') 


'''

#IF ANIDADOS

tengoCovid = True
tengoFiebre = True
grados = 38

if tengoCovid:
    print('No salir de casa')

    if tengoFiebre:
        print('Guardar Reposo')
        if grados > 37:
            print('Tomar Medicina')
    
    else: 
        print('Cuidar temperatura')
else:
    print('Debo cuidarme')
    if tengoFiebre:
        print('Probablemente tengo sintomas de covid')
        if grados > 37:
            print('Tomar Ibuprofeno')
    else:
        print('Sigue Cuidandote')