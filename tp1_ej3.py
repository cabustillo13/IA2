#! us/bin/ dev python
import numpy as np
import math
import matplotlib as map
from mapa import mapa

class Node:
#inicio desde un punto x,y,z y especifico el objetivo
    def __init__(self,position):
        self.g = 0
        self.h = getH
        self.f = 0
        self.position = position[:]     
        self.parent = None              #Puntero al padre
        self.successor_current_cost = 0
  
def generate_neighbours(node_current,mapa):
    x = node_current.position
    Neighbours = []

    for a in [(-1,0), (1,0), (0,-1), (0,1)]:
        if (0 <= x[0]+a[0] < (len(mapa))) and (0 <= x[1]+a[1] < (len(mapa[0]))) and mapa[x[0]+a[0], x[1]+a[1]]==0:
            
            neighbours_pos = [x[0]+a[0], x[1]+a[1]]
            Neighbours.append(Node(neighbours_pos))

    return(Neighbours)    

def getH(Node, goal):
    sum = 0
    #Distancia sin considerar caminos diagonales (nro. de pasos)
    for i in range(0, 2):
        sum += np.abs(Node.position[i] - goal.position[i])

    if sum == 0:
        return 0
    return (sum)

def path(nodo):
    camino = [] 
    while (nodo.parent != None): 
       camino.append(nodo)
       nodo = nodo.parent
    camino2 = []
    for i in camino:
        camino2.append(i.position)
    return (camino2)
      

def A_star(start, goal, mapa):            #Algoritmo general
    start = start   
    
    start.g = 0
    start.h = getH(start, goal)                          
    start.f = start.h
    start.parent =  None

    #Nodo objetivo
    goal = goal             
    goal.h = 0

    #Listas Abierta y Cerrada
    OPEN = []
    CLOSED = []

    #Agrego el nodo inicial y sus vecinos OPEN
    OPEN.append(start)

    while (len(OPEN) != 0):
        node_current = OPEN[0]

        #Elección del vecino con menor f
        for vec in OPEN:
            if (vec.f < node_current.f):
                node_current = vec

        if (node_current.position == goal.position):
            print("Solución encontrada")
            CLOSED.append(node_current)

            #Guardar la direccion de cada hijo
            v = path(node_current)
            v.reverse()
            #print(v)
            break

        #Generación de vecinos
        vecinos = generate_neighbours(node_current, mapa)

        for neig in vecinos:
            successor_cost = node_current.g + getH(node_current, neig)

            if neig in OPEN:
                if (neig.g < successor_cost):
                    CLOSED.append(neig)
                    OPEN.remove(neig)
               
            elif neig in CLOSED:
                continue

            else:
                neig.h =getH(neig, goal)
                OPEN.append(neig)
            neig.g = successor_cost
            neig.parent = node_current
            neig.f = neig.g + neig.h

        #Agrego el nodo actual a la lista cerrada
        CLOSED.append(node_current)
        OPEN.remove(node_current)
    if (node_current.position != goal.position):
        print("No se encontró solución. Posición final: ")
        print(node_current.position)
    return v
                             



if __name__ == "__main__":
    mapa=mapa()
    goal = Node([0, 0])
    start = Node([15, 8])
    
    a = A_star(start, goal, mapa)
    print("Camino: ", " ")
    print(a)


    
    