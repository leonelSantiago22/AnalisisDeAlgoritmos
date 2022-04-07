from pprint import pprint
import random
from time import time #inportamos la libreria que nos permite medir el tiempo 
_autor_ = 'Leonel Santiago Rosas '
#Algoritmo merge de ordenamiento 
def merge_sort(sort_list): #sort_list es el algoritmo que vamos a arreglar
    #print("Desplegando", sort_list);
    if len(sort_list)>1:
        mitadDelArreglo = len(sort_list)//2 #
        mitadIzquierda  = sort_list[:mitadDelArreglo] #De esta manera podemos escojer la mitad que queremos ordenar
        mitadDerecha    = sort_list[mitadDelArreglo:] #En este caso arreglamos la mitad izquierda del arreglo
        
        merge_sort(mitadIzquierda) 
        merge_sort(mitadDerecha) #mandamos a llamar al arreglo de manera recusiva mandando las mitades 
        
        i = 0 
        j = 0 
        k = 0
        #en este caso tomamos como valores las mitades de los arreglos, tomando en cuenta que el recorrido 
        #tiene que ser menor o mayor
        while i <len(mitadIzquierda) and j <len(mitadDerecha):
            if(mitadIzquierda[i]) < mitadDerecha[j]:
                sort_list[k] = mitadIzquierda[i] #mandamos a traer lo que tenemos en la mitad izquierda del arreglo para ordenar
                i = i + 1 
            else :
                sort_list[k] = mitadDerecha[j] #Vamos acomodando la lista de nuevo
                j = j + 1 #mandamos a llamar a la siguiente posicion del arreglo 
            k = k + 1
        #recorremos y ordenamos la mitad izquierda del arreglo    
        while i < len(mitadIzquierda):
            sort_list[k] = mitadIzquierda[i]
            i = i + 1 
            k = k + 1
        #recorremos y ordenamos la mitad derecha del arreglo 
        while j < len(mitadDerecha):
            sort_list[k] = mitadDerecha[j]
            j = j + 1
            k = k + 1
    return sort_list

#Scrypt del programa    
#range(inicio, final, salto)
'''for numeroaInsertar in range(0,1000,1):
    #Arreglo.append(random.randint(0,10000000))
    Arreglo.append(numeroaInsertar) #Appened nos ayuda a insertar dentro de la lista
'''
from random import sample
Arreglo=sample(range(0,8000000),8000000) 

tiempoInicialdeEjecucionDelmerge = time()
Arreglo = merge_sort(Arreglo) #mandamos a llamar lo que es el algoritmo de ordenamiento 
tiempoFinalDeEjecucionDelMerge = time()

tiempoFinal = tiempoFinalDeEjecucionDelMerge - tiempoInicialdeEjecucionDelmerge
print(Arreglo)
print("Tiempo de corrida en total ", tiempoFinal)