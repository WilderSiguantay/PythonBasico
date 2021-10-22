
'''
1. MERGESORT(MITADIZQUIERDA)
2. MERGESORT(MITADDERECHA)
3. MEZCLAR (MITADIZQUIERDA, MITADDERECHA)

CASO BASE: si la lista tiene solo un elemento
'''

def ordenamientoPorMezcla(unaLista):
    print('Dividir', unaLista)

    if len(unaLista) > 1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad] #Copiar los elementos de la mitad izquierda del arreglo
        mitadDerecha = unaLista[mitad:] #copia los elementos de la mitad derecha del arreglo

        ordenamientoPorMezcla(mitadIzquierda) # ordena la primera mitad
        ordenamientoPorMezcla(mitadDerecha) #ordena la segunda mitad

        mezclar(unaLista,mitadIzquierda, mitadDerecha)

def mezclar(arr, izquierda, derecha):
    indiceIzquierdo = 0
    indiceDerecho = 0 
    indiceArr = 0

    #copiar y ordenar elementos de los arreglos izquierdo y derecho

    while indiceIzquierdo < len(izquierda) and indiceDerecho < len(derecha):
        if izquierda[indiceIzquierdo] < derecha[indiceDerecho]:
            arr[indiceArr] = izquierda[indiceIzquierdo]
            indiceIzquierdo = indiceIzquierdo+1
        else:
            arr[indiceArr] = derecha[indiceDerecho]
            indiceDerecho = indiceDerecho + 1
        indiceArr = indiceArr + 1

    #Verificar si aun hay elementos en alguna de las dos mitades
    while indiceIzquierdo < len(izquierda):
        arr[indiceArr] = izquierda[indiceIzquierdo]
        indiceIzquierdo = indiceIzquierdo+1
        indiceArr = indiceArr+1

    while indiceDerecho < len(derecha):
        arr[indiceArr] = derecha[indiceDerecho]
        indiceDerecho = indiceDerecho + 1
        indiceArr = indiceArr + 1


lista = [ 54,26,93,17,77,31,44,55,20]

ordenamientoPorMezcla(lista)
print(lista)