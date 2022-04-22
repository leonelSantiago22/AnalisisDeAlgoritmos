_autor_ = 'Leonel Santiago Rosas '

from operator import le
import random
from statistics import median 
from time import time
from xml.etree.ElementTree import Element
#Particion

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
#Encontramos el pivote aleatorio
def particionaleatoria(arregloapartir, inicio, tope):
    #Creamos una posicion aleatoria para el pivote
    pivotealeatorio = random.randrange(inicio, tope)
    #Cambiamos de posiciones los arreglos 
    arregloapartir[inicio] , arregloapartir[pivotealeatorio] = arregloapartir[pivotealeatorio], arregloapartir[inicio]
    return particion(arregloapartir, inicio, tope) 
#Definicion de random selesct
#Proigramasion del random select

def random_select(Arreglo, primerelemento, ultimoelemento, contador):
    #Si p = q entonces regresamos el arreglo en la primera posicion
    if primerelemento == ultimoelemento:
            print("Elemento optimo : ",Arreglo[primerelemento])
            return Arreglo[primerelemento] 
        
    pivote = particionaleatoria(Arreglo, primerelemento, ultimoelemento) #R toma el valor de un valor aleatroio
    
    k = pivote - primerelemento + 1 
    if contador == k:
        print("Elemento optimo:", Arreglo[pivote])
        return Arreglo[pivote]
    if contador < k :
                random_select(Arreglo, primerelemento, pivote-1, contador)
    else:            
            random_select( Arreglo, pivote+1 , ultimoelemento, contador-k)


            
from statistics import median
def mediana(arreglo):
    valor = median(arreglo)
    #print(valor)
    return valor 
def quicksort(arreglorecibido, inicio, tope):
    #Comprovamos si es necesario el ordenamiento
    if (inicio < tope):
        #mandamos a llamar la funcion que nos permite el uso de un pivote obtenido de manera aleatoria 
        pivote = particionaleatoria(arreglorecibido, inicio, tope)

        quicksort(arreglorecibido, inicio, pivote-1)
        quicksort(arreglorecibido, pivote+1, tope)
        
def particion2(arreglo):
        arregloDeMedianas =[]
        for i in range(0, len(arreglo), 5):
                vectordesalida = arreglo[i:i+5]
                #print(vectordesalida)
                arregloDeMedianas.append (mediana(vectordesalida))
        tamano = len(arregloDeMedianas)
        print("Tamano del vector de las medianas:",tamano)
        #elementoaencontrar = int(input("Ingresa el elemento a buscar:"))
        elemento = random_select(arregloDeMedianas,0, tamano-1, tamano/2)
        return elemento

from random import sample
'''my_filw = open("Vector_A.txt", "r")

data = my_filw.read()

arreglocreado = data.split("   ")'''

arreglocreado=sample(range(0,20),20) 
#print(arreglocreado)

print(arreglocreado)
tamanoArreglo = len(arreglocreado)
print("Tamano del arreglo: ", tamanoArreglo)
particion2(arreglocreado)
quicksort(arreglocreado, 0, tamanoArreglo-1) 
print(arreglocreado)