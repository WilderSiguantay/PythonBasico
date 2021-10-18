#creacion de funcion
#def nombre_funcion(_parametros):
    #bloque de codigo
#palabra reservada def, seguido del nombre la funcion y entre paréntesis
#los parametros (si es que se solicitan)

def funcion1():
    #pass #instruccino que puede ser utilizada cuando querramos una sentencia sintacticamente pero en realidad no hace nada.
    print('Hola Function!')

#llamada a funcion
#funcion1()

#Funcion que recibe un parámetro
def saludar(nombre):
    print('Hola ' + nombre + '!')

#saludar('Wilder')
#saludar('Luis')

#Funcion que recibe dos parametros
def concatenarNombre(nombre, apellido):
    print(nombre + ' ' + apellido)

#concatenarNombre('Wilder', 'Siguantay')

#Error porque falta un parámetro o argumento
# concatenarNombre('Wilder')

#Funciones con argumento por palabra clave

def alumnos(alumno1, alumno2, alumno3):
    print('Alumno 1: ', alumno1)
    print('Alumno 2: ', alumno2)
    print('Alumno 3: ', alumno3)

#alumnos(alumno3='Efrain', alumno2='Karen',alumno1='Josué' )

#Funcion con retorno

def sumar_retorno(n1, n2):
    resultado = 0
    resultado = n1 + n2
    return resultado

respuesta = sumar_retorno(2,6)
print('La suma es: ' , respuesta)

def areaCuadrado(lado):
    return lado**2

print('El area del cuadrado es: ' ,areaCuadrado(5))

def areaRectangulo(x,y):
    area = 0
    area = x * y
    print('El área del rectángulo es: ',area)

def areaTriangulo(b,h):
    return b*h/2


areaRectangulo(2,3)





