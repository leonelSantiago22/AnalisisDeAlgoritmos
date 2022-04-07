from time import time
import  random
Arreglo = []
#range(inicio, final, salto)
for numeroaInsertar in range(0,30000000,1):
    Arreglo.append(numeroaInsertar) #Appened nos ayuda a insertar dentro de la lista
tamanoArreglo = len(Arreglo) #Obtenemos el tanamo del arreglo
key=0 #Declaracion de la llave que nos va a ayudar 
j=0
tiempoInicialdeEjecucion = time()
#en este codigo lo primero que se nota como 1 es el inicio, el tamano se denota como el final y el siguiente uno 
# se denota de cuento en cuanto va a ir sumando
'''range(inicio,final,salto)'''
for j in range(1,tamanoArreglo,1): #Ciclamos la iteraciones desde j = 2 hasta el tamano del arreglo
    key = Arreglo[j]
    i = j-1
    while (i>=0 and Arreglo[i]>key):
        Arreglo[i+1] = Arreglo[i]
        i = i-1
    Arreglo[i+1] = key #remplazamos la posicion por el numero 
tiempoFinaldeEjecucion = time()
tiempoFinal = tiempoFinaldeEjecucion - tiempoInicialdeEjecucion
print(Arreglo)
#codigo para imprimir posicion por posicion del arreglo

'''for elemento in Arreglo:
    print(elemento)'''
    
print("tiempo de corrida:",tiempoFinal) #imprimimos el tiempo final de ejecucion en Segundos