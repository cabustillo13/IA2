import numpy as np
from time import time
import random as rd
import math

class Nodo:
    def __init__(self,padre=None,pos=None):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,end): #a es un nodo. Heuristica entre nodo current y final
        self.h = abs(self.pos[0]-end[0])+abs(self.pos[1]-end[1])
    def calculate_g(self): #camino recorrido
        self.g = self.g + 1
    def calculate_f(self): 
        self.f = self.g+self.h

def generate_map(cant_rows_shelves,cant_columns_shelves,n_rows,n_columns):
    #map generico de un almacen con estantes de 8 espacios
    x=1
    row=1
    column=1
    pasillo = 3 #nro de column q esta el 1er pasillo
    m = 1
    map = np.zeros((n_rows,n_columns),int)
    while(x<=8*cant_columns_shelves*cant_rows_shelves):
        map[row][column] = x
        if x%2==0: #x es par
            row += 1
            column -= 1
        else:
            column += 1
        if x%8==0:
            row+=1
        x +=1
        if x==(8*cant_rows_shelves*m)+1:
            row = 1
            column = pasillo+1
            pasillo += 3 
            m += 1 #para recorrer cada column de shelves
    print(map)
    return(map)

def search_position_of(value,map):
    for index,row in enumerate(map):
        if value in row: #row es la fila entera. index es el numero de la fila donde esta el value buscado         
            f = np.ndarray.tolist(row) #row es del tipo numpy.ndarray y no tiene atributo index. con esta linea arreglo eso
            column = f.index(value)
            if map[index][column-1] == 0:
                column -= 1
            elif map[index][column+1] == 0:
                column += 1
            return (index,column)

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
    n_rows_shelves = 3     
    n_columns_shelves = 3  
    n_rows = 5*n_rows_shelves+1
    n_columns = 3*n_columns_shelves+1
    t_prom = 0 #para calcular el promedio de 100 temple simulado
    map = generate_map(n_rows_shelves,n_columns_shelves,n_rows,n_columns)

    products_list = [3,45,18,27,35,9]

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
                print(i," product is in ",product, " with H= ",start_node.h)
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
        solution_list.append(simulated_annealing(map,n_rows,n_columns,start,end,T))
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
    #"Pintar" solucion con unos
    print("\nPosicion final: ", solution)
    map[solution[0]][solution[1]] = 1
    print("\n",map,"\n\nTiempo de ejecucion promedio de Temple Simulado: ",str(round(t_prom/100,8)))

if __name__ == "__main__":
    main()