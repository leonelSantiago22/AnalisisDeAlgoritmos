import random
from time import time
_autor_ = 'Leonel Santiago Rosas'
#El metodo nos ayuda a particionar el arreglo de caracteres, mandando asi al metodo
def particion(arreglo, bajo, alto): #definimos la particion 
    i = (bajo - 1 ) #tratamos de encontrar la particion
    pivote = arreglo[alto]
    for j in range(bajo, alto):
        #If el elemento en corriente es mas pequeno o igual al pivote 
        if arreglo[j] <= pivote:
            i = i +1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i] #intercambiamos lo valores que esta en la cola 
    arreglo[i+1], arreglo[alto] = arreglo[alto], arreglo[i+1]
    return(i+1)
#Definimos el metodo de arreglo para el llamado recursivo del quick sort
def quick_sort(arreglo, bajo, alto):
    if len(arreglo) == 1: #si el largo del arreglo es 1 retornamos el arreglo como esta
        return arreglo
    if bajo < alto:
        ParticionHecha = particion(arreglo, bajo, alto)
        quick_sort(arreglo, bajo, ParticionHecha-1)
        quick_sort(arreglo,ParticionHecha+1, alto)

#Scrypt del programa    
Arreglo = []
#range(inicio, final, salto)
for numeroaInsertar in range(0,10000,1):
    Arreglo.append(random.randint(0,1000))
    #Arreglo.append(numeroaInsertar) #Appened nos ayuda a insertar dentro de la lista

tamanoDelArreglo = len(Arreglo) #obtenemos el tamano del arreglo
tiempoInicialDeEjecucion = time() #iniciamos el cronometro
quick_sort(Arreglo, 1, tamanoDelArreglo-1)#mandamos a llamar el metodo de ordenamiento
tiempoFinalDeEjecucion = time()
tiempoFinal = tiempoFinalDeEjecucion - tiempoInicialDeEjecucion #sacamos el tiempo final de jecucion del merge sort

print(Arreglo)
print(tiempoFinal)