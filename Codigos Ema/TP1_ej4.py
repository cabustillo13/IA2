import TP1_ej3 as A_star
from time import time
import random as rd
import math

def simulated_annealing(map,n_rows,n_columns,start,end,T):
    start_node = A_star.Nodo(None,start)
    A_star.Nodo.calculate_h(start_node,end)
    current = start_node
    time=0
    while(True):
        temp = T[time]        
        if temp<math.exp(-50) or time == len(T)-1:
            return current.pos
        
        neighbours_pos = [(current.pos[0]+a[0], current.pos[1]+a[1]) for a in [(-1,0), (1,0), (0,-1), (0,1)] if ((0 <= current.pos[0]+a[0] < n_rows) and (0 <= current.pos[1]+a[1] < n_columns)) and map[current.pos[0]+a[0], current.pos[1]+a[1]]==0]
        neighbours = []

        for i in neighbours_pos:
            neighbours.append(A_star.Nodo(current,i))
        
        next = neighbours[rd.randint(0,len(neighbours)-1)] #vecino aleatorio
        A_star.Nodo.calculate_h(current,end) 
        A_star.Nodo.calculate_h(next,end) 
        delta_E = next.h - current.h
        value = rd.random() #nro aleatorio entre 0 y 1
        
        if delta_E < 0:
            current = next
        elif value < math.exp(-delta_E/temp):
            current = next
        time+=1
        

def main():
    print("Ejercicio 4:") 
    rd.seed(None)
    n_rows_shelves = 3     
    n_columns_shelves = 3  
    n_rows = 5*n_rows_shelves+1
    n_columns = 3*n_columns_shelves+1
    t_prom = 0 #para calcular el promedio de 50 temple simulado
    map = A_star.generate_map(n_rows_shelves,n_columns_shelves,n_rows,n_columns)

    start = A_star.search_position_of(1,map) 
    end = A_star.search_position_of(72,map)  
    
    t = 300 #temperatura inicial
    T = []
    solution_list = []
    for x in range(1000):
        T.append(t)
        t=t*0.9 #func exponencial de T decreciente en el tiempo
    
    for i in range(50):
        t1 = time()
        solution_list.append(simulated_annealing(map,n_rows,n_columns,start,end,T))
        t2 = time()
        t_prom = t_prom+t2-t1 
    #print(solution_list) 
    #primero hice una lista de soluciones y luego elijo la que
    # se encuentra mayor cantidad de veces en la lista de soluciones
    max_sol=0
    for sol in solution_list: #solution list es una lista de tuplas de posiciones 
        counter = solution_list.count(sol)
        if counter > max_sol:
            max_sol = counter
            solution = sol
    #"Pintar" solucion con un uno
    print("\nPosicion final: ", solution)
    map[solution[0]][solution[1]] = 1
    print("\n",map,"\n\nTiempo de ejecucion promedio de Temple Simulado: ",str(round(t_prom/20,8)))

if __name__ == "__main__":
    main()