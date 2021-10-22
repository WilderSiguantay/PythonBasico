lista = [5,7,9,2,4,3,1,6,8]
comparaciones = 0
for i in range(len(lista) -1): #recorre la lista
    for j in range(len(lista)-1): #sirve para comparar los elementos de la lista
        #print('Comparando: ' , lista[j], "con ", lista[j+1])
        if(lista[j] > lista[j+1]):
            #lista[j], lista[j+1] = lista[j+1] , lista[j]
            comparaciones += 1
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
            #print("Intecambiando: ", lista[j], "por ", lista[j+1])        
        print(lista)
print(lista)

#OPTIMIZAR CODIGO
#CONCENTINELA
lista = [5,7,9,2,4,3,1,6,8]
comparaciones = 0
hay_cambios = True
while hay_cambios: #recorre la lista
    hay_cambios = False
    for j in range(len(lista)-1): #sirve para comparar los elementos de la lista
        #print('Comparando: ' , lista[j], "con ", lista[j+1])
        comparaciones += 1
        if(lista[j] > lista[j+1]):
            #lista[j], lista[j+1] = lista[j+1] , lista[j]
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
            hay_cambios = True
            #print("Intecambiando: ", lista[j], "por ", lista[j+1])        
        
print(lista)
print(comparaciones)


lista = [5,7,9,2,4,3,1,6,8]
comparaciones = 0
for i in range(len(lista) -1): #recorre la lista
    for j in range(len(lista) - i -1): #sirve para comparar los elementos de la lista
        #print('Comparando: ' , lista[j], "con ", lista[j+1])
        if(lista[j] > lista[j+1]):
            #lista[j], lista[j+1] = lista[j+1] , lista[j]
            comparaciones += 1
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
            print(lista)
            #print("Intecambiando: ", lista[j], "por ", lista[j+1])        
print(lista)
print(comparaciones)





lista = [5,7,9,2,4,3,1,6,8]
comparaciones = 0
hay_cambios = True
i = 0
while hay_cambios and i < len(lista)-1: #recorre la lista
    hay_cambios = False
    for j in range(len(lista) -i -1): #sirve para comparar los elementos de la lista
        #print('Comparando: ' , lista[j], "con ", lista[j+1])
        comparaciones += 1
        if(lista[j] > lista[j+1]):
            #lista[j], lista[j+1] = lista[j+1] , lista[j]
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
            hay_cambios = True
            #print("Intecambiando: ", lista[j], "por ", lista[j+1])        
    i +=1
print(lista)
print(comparaciones)