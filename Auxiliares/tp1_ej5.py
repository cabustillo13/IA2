#! us/bin/ dev python
import numpy as np
import math
import matplotlib as map
import random as rn
from mapa import generate_map

from tp1_ej3 import A_star, Node

from time import time
import matplotlib.pyplot as plt

#Cambia posición de un item en la lista y obtiene distancia total recorrida
def swap_positions(aux):
    #rn.shuffle(val)
    a = rn.randint(1,(len(val)-3))          #Asi no modifica la primera y ultima posición (inicio-fin) 
    aux[a], aux[a+1] = aux[a+1], aux[a] 
    return aux

def distancia(val, mapa):
    E=0    
    for a in range (0,(len(val)-1)):
        E += len(A_star(Node(val[a]), Node(val[a+1]),mapa))
    return E
        
              
#Función Algoritmo general 
def simulated_annealing(val,mapa, T):
    #Definición de Constantes
    #Ti=100
    
    
    Tf=0.1      #modificar acá


    #c=0.9       #Cte de enfriamiento(entre 0 y 1)
    n=10        #Número de saltos hasta el equilibrio
    #K=1         #Cte de Boltzman: le podemos dar otro valor
    
    #X = swap_positions(val)
    #aux=X[:]
    X = val
    E = distancia(X, mapa)      #E=energía de X (fitness), en este caso es la distancia. Una menor distancia es una mayor Energía
    #T=20
    
    min_E=E
    min_X=X
    #Vector de valores aleatorios de las posiciones que puedo cambiar
    #a=np.random.randint(low=0, high=(len(val)-3), size=n*T).tolist()
    #z=0

    while (Tf<T):
        for i in range(0,n):
            #aux=X[:]
            #a = rn.randint(1,(len(val)-3))          #Asi no modifica la primera y ultima posición (inicio-fin) SWAP_POSITIONS
            
            #ini=time()
            X_aux = swap_positions(X[:])
            #fin=time()
            #print("tiempo swap", fin-ini)
            #inicio=time()
            E_aux = distancia(X_aux, mapa)
            #final=time()
            #print("tiempo distancia", final-inicio)
            
            if E_aux <= E:
                X = X_aux
                E = E_aux
                ###############Observar###########
                if E < min_E:
                    min_E = E_aux
                    min_X = X_aux   

            else:
                N = rn.random()
                if N <  math.exp(-(E_aux-E)/(T)):
                    X = X_aux
                    E = E_aux
            #z +=1
        T = 0.92*T #(c*T) -=1
    print("Solución última: ", X)
    print("Energía: ", E)
    print("Mejor orden: ", min_X)
    print("Menor energía: ", min_E)
    change = ((E-min_E)/E)*100
    return E, change   
   

if __name__ == "__main__":

    #valores= input("Valores a ingresar(como lista): ")          
    mapa = generate_map()
    #Luego de tomar valores, se puede transformar en una lista de posiciones
    
    val = [(0,0),(5,6),(6,3),(9,0),(8,0),(14,3),(9,7),(3,7),(12,7),(0,0)]
    #picking_list = [(0,0),(5,6),(6,3),(9,0),(8,0),(14,3),(9,7),(3,7),(12,7),(0,0)]
    #init=time()
    #a = simulated_annealing(val, mapa)
    #finish=time()
    #print("tiempo del algoritmo: ", (finish-init))
    
    #Aca cambie cosas (hasta plt.show)
    for i in range(1,10):
        T=100
        mejora=[]
        Tiempo=[]
        temple = []
        flag = True
        
        while flag == True:
            dist, change = simulated_annealing(val,mapa, T)
            mejora.append(change)
            Tiempo.append(T)
            if T == 500:
                flag = False
            
            T +=50
        plt.plot(Tiempo, mejora)
        plt.xscale('log')
        plt.suptitle('Mejora de la respuesta en función al tiempo', fontsize = 20)
        plt.xlabel('Temperatura', fontsize = 16)
        plt.ylabel('Mejora %', fontsize = 16)
    plt.show()

    #Tener en cuenta para pasar de número a posicion ya no va a funcionar el análisis anterior
    #Hay que buscar una posición que sea 0 y adyacente al valor ingresado

    #EN VEZ DE GENERAR UN RANDINT EN CADA FUNCION SWAP, HACER UN VECTOR RAND E INGRESARLO AL TEMPLE