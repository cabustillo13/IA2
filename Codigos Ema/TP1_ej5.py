from TP1_ej3 import generate_map,search_position_of,Nodo
import numpy as np
from time import time
import random as rd
import math

def simulated_annealing(map,n_rows,n_columns,start,end,T):
    start_node = Nodo(None,start)
    Nodo.calculate_h(start_node,end)
    current = start_node
    time=0
    while(True):
        temp = T[time]        
        if temp<math.exp(-50) or time == len(T)-1:
            return current.pos
        
        neighbours_pos = [(current.pos[0]+a[0], current.pos[1]+a[1]) for a in [(-1,0), (1,0), (0,-1), (0,1)] if ((0 <= current.pos[0]+a[0] < n_rows) and (0 <= current.pos[1]+a[1] < n_columns)) and map[current.pos[0]+a[0], current.pos[1]+a[1]]==0]
        neighbours = []

        for i in neighbours_pos:
            neighbours.append(Nodo(current,i))
        
        next = neighbours[rd.randint(0,len(neighbours)-1)] #vecino aleatorio
        Nodo.calculate_h(current,end) 
        Nodo.calculate_h(next,end) 
        delta_E = next.h - current.h
        value = rd.random() #nro aleatorio entre 0 and 1
        
        if delta_E < 0:
            current = next
        elif value < math.exp(-delta_E/temp):
            current = next
        time+=1
        
def main():
    print("Ejercicio 5:") 
    rd.seed(None)
    map=generate_map()
    t_prom = 0 #para calcular el promedio de 100 temple simulado

    products_list = [3,45,18,27,35,9] #debe ser aleatoria

    start=search_position_of(min(products_list),map)
    end=search_position_of(max(products_list),map)

    start_node = Nodo(None,start) #admito como nodo inicial el minimo. Aca supongo que el despacho se encuentra cercano al numero 1
        
    Nodo.calculate_h(start_node,end)
    min_h = start_node.h
    for i in products_list:
        product = search_position_of(i,map)
        if product != start_node.pos:
            Nodo.calculate_h(start_node,product)
            if start_node.h<min_h:
                min_h = start_node.h
                end = product
    end_node = Nodo(None,end)
    print(end_node.pos)

    t = 300 #temperatura inicial
    T = []
    solution_list = []
    for x in range(1000):
        T.append(t)
        t=t*0.9 #func exponencial de T decreciente en el tiempo
    for i in range(20):
        t1 = time()
        #solution_list.append(simulated_annealing(map,start,end,T))
        t2 = time()
        t_prom = t_prom+t2-t1 #redondeo a 8 decimales    
    #primero hice una lista de soluciones y luego elijo la que
    # se encuentra mayor cantidad de veces en la lista de soluciones
    max_sol=0
    for sol in solution_list: #solution list es una lista de tuplas de posiciones 
        counter = solution_list.count(sol)
        if counter > max_sol:
            max_sol = counter
            solution = sol
    

if __name__ == "__main__":
    main()