from TP1_ej3 import generate_map,search_position_of,Nodo,a_star
import numpy as np
from time import time
import random as rd
import math
import matplotlib.pyplot as plt
def fitness(P_list,map): #calcula el fitness de cierto orden de una lista
    aux = P_list[:]
    f_total = 0
    aux.insert(0,0) #posicion inicial y final son (0,0), es lo que devuelve search_position_of al pasarle un 0
    aux.insert(len(aux),0)
    for j in range(len(aux)-1):
        f_total += len(a_star(map,aux[j],aux[j+1]))
    return f_total

def swap_positions(current):
    swap1 = rd.choice(current)
    swap2 = rd.choice(current)
    while swap1 == swap2:
        swap2 = rd.choice(current) #por si coinciden
    next=current[:]
    a, b = next.index(swap1), next.index(swap2)
    next[b], next[a] = next[a], next[b]
    return next

def plot_solution(time_list,prob_list):
    import matplotlib
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(time_list, prob_list)
    ax.set(xlabel='Tiempo', ylabel='Probabilidad')
    ax.grid()
    plt.show()      

def simulated_annealing(picking_list,order,want_to_print,T):
    map=generate_map(order)
    time=1
    max_time = T #= 1000 #coincide con la T inicial
    prob_list = [] #para plotear
    time_list = [] #para plotear
    current = picking_list[:]
    if want_to_print:
        print("Distancia inicial:",fitness(picking_list,map),"con lista:",picking_list)
    #-----------------Inicializando variables-------------
    while True:
        T = T/2 #math.exp(1/time) #max_time-0.9*time #decrecimiento lineal
        if T<0.1 or time > max_time:
            dist_min = fitness(current,map)
            if want_to_print:
                #plot_solution(time_list,prob_list)
                print("Distancia minima:",dist_min,"con lista:",current)
                mejora=(fitness(picking_list,map)-dist_min)/(fitness(picking_list,map))
                print("Mejora: ", mejora)
            return dist_min, mejora
        
        next = swap_positions(current) #vecino random 
        
        f_next = fitness(next,map)
        f_current = fitness(current,map)
        delta_E = f_next - f_current 

        value = rd.random() #nro aleatorio entre 0 and 1
        prob = math.exp(-delta_E/(1*T)) #0.10 para abajo es conveniente
        if delta_E <= 0:
            current = next
        elif value < prob:
            current = next
            prob_list.append(prob)
            time_list.append(time)
        time+=1

def main():
    print("Ejercicio 5:") 
    rd.seed(None)
    picking_list = [37, 47, 11, 48, 24]
    order = [12, 3, 20, 36, 32, 37, 1, 2, 4, 23, 39, 9, 19, 40, 46, 29, 27, 35, 45, 13, 16, 14, 24, 11, 48, 6, 7, 25, 5, 47, 15, 41, 43, 22, 8, 34, 26, 42, 38, 21, 33, 31, 30, 28, 17, 18, 10, 44]   
    #T=1000
    #t1=time()
    #simulated_annealing(picking_list,order,T,True)
    #t2=time()
    #print("Tiempo de ejecucion:",round(t2-t1,4),"segundos")
    T = 250
    Tiempo=[]
    mejora=[]
    #for i in range (0,100):
    while T<5000:
        dist, change = simulated_annealing(picking_list,order,T,True)
        mejora.append(change)
        Tiempo.append(T)
        T +=250
    plt.plot(Tiempo, mejora, 'b')
    plt.xscale('log')
    plt.show()
if __name__ == "__main__":
    main()