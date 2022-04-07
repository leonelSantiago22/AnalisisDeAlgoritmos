#Implementacion de quicksort aleatorio 
#por el metodo de particion lomuto's 
import random 
from time import time
_autor_ = 'Leonel Santiago Rosas'
def particion(arreglo, inicio, tope):
    pivote = inicio
    i = inicio +1
    for j in range(inicio+1, tope + 1):
        #si el tamano del elemento es pequeno o igual al pivote 
        #desplaxamos a la derecha la particion 
        if arreglo[j] <= arreglo[pivote]:
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
            i = i+1
    arreglo[pivote], arreglo[i-1] = arreglo[i-1], arreglo[pivote]
    pivote = i - 1
    return (pivote)
#funcion que nos permite obtener el pivote de manera aleatoria
def particionaleatoria(arregloapartir, inicio, tope):
    #Creamos una posicion aleatoria para el pivote
    pivotealeatorio = random.randrange(inicio, tope)
    #Cambiamos de posiciones los arreglos 
    arregloapartir[inicio] , arregloapartir[pivotealeatorio] = arregloapartir[pivotealeatorio], arregloapartir[inicio]
    return particion(arregloapartir, inicio, tope) 
#Definimos el metodo quick sort 
def quicksort(arreglorecibido, inicio, tope):
    #Comprovamos si es necesario el ordenamiento
    if (inicio < tope):
        #mandamos a llamar la funcion que nos permite el uso de un pivote obtenido de manera aleatoria 
        pivote = particionaleatoria(arreglorecibido, inicio, tope)

        quicksort(arreglorecibido, inicio, pivote-1)
        quicksort(arreglorecibido, pivote+1, tope)
    
from random import sample
arreglocreado=sample(range(0,8000000),8000000) #Creamos el arreglo de numeros que no se repiten

tamanodelArreglo = len(arreglocreado) #obtenemos el tamano del arreglo
tiempoInicialDeEjecucion = time() #iniciamos el cronometro
quicksort(arreglocreado, 0, tamanodelArreglo-1) #Mandamos a llamar el metodo quick sort
tiempoFinalDeEjecucion = time()
tiempoFinal = tiempoFinalDeEjecucion - tiempoInicialDeEjecucion #sacamos el tiempo final de jecucion del merge sort
print(arreglocreado)
print("Tiempo del ordenamiento de datos: ", tiempoFinal)
        
