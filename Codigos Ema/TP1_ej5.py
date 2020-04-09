from TP1_ej3 import generate_map,search_position_of,Nodo,a_star
import numpy as np
from time import time
import random as rd
import math

def fitness(P_list,map): #calcula el fitness de cierto orden de una lista
    aux = P_list[:]
    f_total = 0
    aux.insert(0,0)
    aux.insert(len(aux)-1,0)
    for i in range(len(aux)):
        aux[i] = Nodo(None,search_position_of(aux[i],map))
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

def simulated_annealing(picking_list,order,want_to_print):
    map=generate_map(order)
    time=1
    max_time = T = 1000 #coincide con la T inicial
    prob_list = [] #para plotear
    time_list = [] #para plotear
    current = picking_list[:]
    if want_to_print:
        print("Distancia inicial:",fitness(picking_list,map),"con lista:",picking_list)
    #-----------------Inicializando variables-------------
    while True:
        T -= 1 #math.exp(1/time) #max_time-0.9*time #decrecimiento lineal
        if T<math.exp(-10) or time > max_time:
            dist_min = fitness(current,map)
            if want_to_print:
                #plot_solution(time_list,prob_list)
                print("Distancia minima:",dist_min,"con lista:",current)
            return dist_min
        
        next = swap_positions(current) #vecino random 
        
        f_next = fitness(next,map)
        f_current = fitness(current,map)
        delta_E = f_next - f_current 

        value = rd.random() #nro aleatorio entre 0 and 1
        prob = math.exp(-delta_E/(0.02*T)) #0.10 para abajo es conveniente
        if delta_E <= 0:
            current = next
        elif value < prob:
            current = next
            prob_list.append(prob)
            time_list.append(time)
            #print(f_next,f_current,round(prob,2),round(value,2),delta_E,round(T,1))
        
        time+=1

def main():
    print("Ejercicio 5:") 
    rd.seed(None)
    picking_list = [45, 1, 6, 8, 24, 39, 17, 18,2]
    order = []
    for k in range(1,49):
        order.append(k)
    
    t1=time()
    simulated_annealing(picking_list,order,True)
    t2=time()
    print("Tiempo de ejecucion:",round(t2-t1,4),"segundos")

if __name__ == "__main__":
    main()