#QuickSort es uno de los ordenamientos mas rapidos y eficientes.

'''
- Utiliza la estrategia de divide y venceras.
- Utililiza un pivote a partir del cual vamos a dividir los elementos menores a ese pivote 
y los mayores a ese pivote
- Cualquier elemento puede servir como pivote aunque se utiliza comunmente el primer elemento 
de la lista
- se ponen los menores del lado izquierdo y los mayores del lado derecho
- caso base, es cuando la lista tiene solo un elemento 
'''
#QUICKSORT VERSION SIMPLE CON LISTAS AUXILIARES

lista = [8,12,3,11,5,9,10,4,15,7]


def particionado(lista):
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1,len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
        
    return menores, pivote, mayores

def quicksort(lista):

    if len(lista) < 2:
        return lista

    menores, pivote, mayores = particionado(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort(lista))

#VERSION CON PARTICIONADO HOARE

'''
- Se utilizan dos punteros, uno va a estar a la par del pivote y otro al final de la lista
- intercambia los lugares sin utilizar listas, para eso sirven los punteros

'''


def particionado(lista,menor,mayor):
    pivote = lista[menor]
    izq = menor + 1 
    der = mayor

    while True:
        while izq <= der and lista[izq] <= pivote:
            izq +=1 #movemos puntero una posicion hacia la derecha
        while izq <= der and lista[der] >= pivote:
            der -=1 #movemos el puntero una posocion haia la izquierda

        if der < izq:
            break
        else:
            lista[izq], lista[der] = lista[der], lista[izq]
    lista[menor], lista[der] = lista[der], lista[menor] #hacemos cambio de pivote por el elemento
    #del puntero derecho

    return der #devuelve el puntero derecho, porque a partir de este puntero es donde
    #se parte lalista en dos


def quicksort(lista,menor,mayor):

    if menor < mayor: #lista tiene mas de un elemento
        pivote = particionado(lista,menor,mayor)
        quicksort(lista,menor,pivote-1)
        quicksort(lista,pivote+1,mayor)

lista = [ 7,5,3,12,9,2,10,4,15,8]
print('*****QUICKSORT PARTICIONADO HOARE*******')
print(lista)
quicksort(lista, 0,len(lista)-1)
print(lista)
