import numpy as np
from time import time
import random as rd

class Nodo:
    def __init__(self,padre=None,pos=None):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,end): #Heuristica entre nodo actual y final
        self.h = abs(self.pos[0]-end[0])+abs(self.pos[1]-end[1])+abs(self.pos[2]-end[2])+abs(self.pos[3]-end[3])+abs(self.pos[4]-end[4])+abs(self.pos[5]-end[5])
    def calculate_g(self): #Camino recorrido
        self.g = self.g + 1
    def calculate_f(self): 
        self.f = self.g+self.h

def generate_map(dim):
    map = [[[[[[0 for i in range(dim)] for j in range(dim)] for k in range(dim)] for ii in range(dim)] for jj in range(dim)] for kk in range(dim)]
    return(map)

def generate_obstacles(map,dim):
    n = int((dim**6)/100) #un centesimo del espacio esta ocupado por obstaculos
    print("Hay " + str(dim**6) + " puntos en el espacio articular" + "\nHay " + str(n) + " obstaculos")
    obstacles = []
    x = dim-1
    for i in range(n):
        a = (rd.randint(0,x),rd.randint(0,x),rd.randint(0,x),rd.randint(0,x),rd.randint(0,x),rd.randint(0,x))
        if map[a[0]][a[1]][a[2]][a[3]][a[4]][a[5]] == 0:
            obstacles.append(a)
            map[a[0]][a[1]][a[2]][a[3]][a[4]][a[5]] = 1 #ultimo elemento de la lista obstacles
    return obstacles

def a_star(map,start,end,obstacles,tam): 
    OPEN = []
    CLOSED = []
    start_node = Nodo(None,start)

    Nodo.calculate_h(start_node,end)
    Nodo.calculate_f(start_node)
    current = start_node
    OPEN.append(current)

    while current.pos != end:
        current = OPEN[0]
        current_index = 0
        for i,aux in enumerate(OPEN): 
            if aux.f < current.f:
                current = aux
                current_index = i
        OPEN.pop(current_index) 
        CLOSED.append(current)  
        
        if current.pos == end:
            path = []
            while current is not None:
                path.append(current.pos)
                current = current.padre
            return(path[::-1]) #retorna el camino dado vuelta porque parte del final al inicio
        
        neighbours = [] 
        for a in [(1,0,0,0,0,0),(-1,0,0,0,0,0),(0,1,0,0,0,0),(0,-1,0,0,0,0),(0,0,1,0,0,0),(0,0,-1,0,0,0),(0,0,0,1,0,0),(0,0,0,-1,0,0),(0,0,0,0,1,0),(0,0,0,0,-1,0),(0,0,0,0,0,1),(0,0,0,0,0,-1)]:
            pos = (a[0] + current.pos[0],a[1] + current.pos[1],a[2] + current.pos[2],a[3] + current.pos[3],a[4] + current.pos[4],a[5] + current.pos[5])
            if pos in obstacles:
                continue
            if (0 <= current.pos[0]+a[0] < tam) and (0 <= current.pos[1]+a[1] < tam) and (0 <= current.pos[2]+a[2] < tam) and (0 <= current.pos[3]+a[3] < tam) and (0 <= current.pos[4]+a[4] < tam) and (0 <= current.pos[5]+a[5] < tam):
                neighbours.append(Nodo(current,pos))

        for neighbour in neighbours:
            if neighbour in CLOSED:
                continue 
            Nodo.calculate_g(current)
            Nodo.calculate_h(neighbour,end) 
            Nodo.calculate_f(neighbour)
            if neighbour.g < current.g or neighbour not in OPEN:
                neighbour.padre = current
                if neighbour not in OPEN and neighbour not in CLOSED:
                    OPEN.append(neighbour)
            
def main():
    print("Ejercicio3_Robot_6GDL")
    rd.seed(None)
    tam = 22 #es la cantidad de puntos articulares por cada GDL
    map = generate_map(tam) 
    obstacles = generate_obstacles(map,tam)
    #Funcionamiento de randint(a,b): a<=N<=b (nro aleatorio entre a y b, incluidos estos dos)
    start = (rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1))
    end = (rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1),rd.randint(0,tam-1))

    print("Inicio: ", start, "\nFin:    ", end)
    t1=time()
    path = a_star(map,start,end,obstacles,tam) #camino solucion
    t2 = time()
    print("Camino:")
    for position in path:
        print(position)

    print("Tiempo de ejecucion A*: " + str(t2-t1)) 

if __name__ == "__main__":
    main()
