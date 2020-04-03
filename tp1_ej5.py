#! us/bin/ dev python
import numpy as np
import math
import matplotlib as map
import random as rn
from mapa import mapa
import tp1_ej3 as star
#import change_position
'''
def coordenadas(mapa, val):
    mapa = mapa
    auxiliar = []
    for i in range (0, len(mapa)):              #filas  
        for j in range(len(mapa[0])):           #columnas
            if mapa[i][j] in val:
                auxiliar.append(mapa[i][j])
    return (auxiliar)            
'''

#Cambia posición de un item en la lista y obtiene distancia total recorrida
def swap_positions(val,mapa):
    pos = round((rn.randrange(len(val)-1)))   #round((rn.random()*10))
    val[pos], val[pos+1] = val[pos+1], val[pos]
    return val

def distancia(val, mapa):
    E_sum = 0    
    for a in range (0,(len(val)-1)):
        E = star.A_star(star.Node(val[a]),star.Node(val[a+1]),mapa)
        print(E)
        E_sum += len(E)
    return E_sum
        

def posiciones(valores,mapa):
    '''
    for i in range(0, (len(valores))):
        if i in mapa:
            posiciones.append(i)
    '''
    posiciones = []
    auxiliar = []
    for i in range(0, len(mapa)):
        for j in range(0,len(mapa[0])):
            if mapa[i][j] in valores:  
                auxiliar.append(valores.index(mapa[i][j])) #Agrego la posicion del vector
                #puedo hacer tupla con posicion y valor
                
                
#Función Algoritmo general 
def simulated_annealing(val,mapa):
    #Definición de Constantes
    Ti=200
    Tf=0
    c=0.9       #Cte de enfriamiento(entre 0 y 1)
    n=20        #Número de saltos hasta el equilibrio
    K=1         #Cte de Boltzman: le podemos dar otro valor

    #Tomar muestra de los valores de h de A* para cada punto
    #rn.shuffle(val)             #puede ser : X = muestrear(val)
    X = swap_positions(val, mapa)
    E = distancia(X, mapa)      #E=energía de X (fitness), en este caso es la distancia. Una menor distancia es una mayor Energía

        ##La funcion A_star devuelve un v (camino, hacer E = len(v))
    T=Ti

    
    while (Tf<T):
        for i in range(0,20):
            X_aux = swap_positions(X, mapa)
            E_aux = distancia(X, mapa)
            if E_aux< E:
                X = X_aux
                E = E_aux
            else:
                N = np.random([0,1])
                if N <  math.exp(-(E_aux-E)/(K*T)):
                    X = X_aux
                    E = E_aux
        T -= 1 #(c*T)
    print("Solución: ")
    print(X)            
            
#Puedo tratar de guardar cada x sucesor en una cadena para mostrar el camino
#Primero hacer una cadena e ir cambiando las posiciones hasta lograr una, guardarla e ir haciendo otro
#

if __name__ == "__main__":

    #valores= input("Valores a ingresar(como lista): ")          
    mapa = mapa()
    #Luego de tomar valores, se puede transformar en una lista de posiciones
    val = [[0,0],[5,3],[3,6],[9,0],[6,7]]
    a = simulated_annealing(val, mapa)

    #Tener en cuenta para pasar de número a posicion ya no va a funcionar el análisis anterior
    #Hay que buscar una posición que sea 0 y adyacente al valor ingresado

