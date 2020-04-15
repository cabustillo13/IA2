#! us/bin/ dev python
import numpy as np
import math
import matplotlib as map
import random as rn
from mapa import generate_map

from tp1_ej3 import A_star, Node

from time import time

#Cambia posición de un item en la lista y obtiene distancia total recorrida
def swap_positions(aux):
    #rn.shuffle(val)
    #aux= val[:]
    a = rn.randint(1,(len(val)-3))          #Asi no modifica la primera y ultima posición(inicio-fin)
    aux[a], aux[a+1] = aux[a+1], aux[a] 
    return aux

def distancia(val, mapa):
    E=0    
    for a in range (0,(len(val)-1)):
        E += len(A_star(Node(val[a]), Node(val[a+1]),mapa))
    return E
        
              
#Función Algoritmo general 
def simulated_annealing(val,mapa):
    #Definición de Constantes
    Ti=200
    Tf=0
    c=0.9       #Cte de enfriamiento(entre 0 y 1)
    n=20        #Número de saltos hasta el equilibrio
    K=1         #Cte de Boltzman: le podemos dar otro valor
    
    X = swap_positions(val)
    #aux=X[:]
    E = distancia(X, mapa)      #E=energía de X (fitness), en este caso es la distancia. Una menor distancia es una mayor Energía
    T=Ti

    min_E=E
    min_X=X

    while (Tf<T):
        for i in range(0,n):
            aux=X[:]
            X_aux = swap_positions(aux)
            E_aux = distancia(X_aux, mapa)
            if E_aux <= E:
                X = X_aux
                E = E_aux
                ###############Observar###########
                if E < min_E:
                    min_E = E_aux
                    min_X = X_aux   

            else:
                N = rn.random()
                if N <  math.exp(-(E_aux-E)/(K*T)):
                    X = X_aux
                    E = E_aux

        T -= 1 #(c*T)
    print("Solución última: ", X)
    print("Energía: ", E)
    #posicion_mejor = Best_path[0] 
    print("Mejor orden: ", min_X)
    #energia_mejor = Best_path[1]
    print("Menor energía: ", min_E)   
   

if __name__ == "__main__":

    #valores= input("Valores a ingresar(como lista): ")          
    mapa = generate_map()
    #Luego de tomar valores, se puede transformar en una lista de posiciones
    
    val = [(0,0),(5,6),(6,3),(9,0),(8,0),(14,3),(9,7),(3,7),(12,7),(0,0)]
    init=time()
    a = simulated_annealing(val, mapa)
    finish=time()
    print("tiempo del algoritmo: ", (finish-init))
    #Tener en cuenta para pasar de número a posicion ya no va a funcionar el análisis anterior
    #Hay que buscar una posición que sea 0 y adyacente al valor ingresado

