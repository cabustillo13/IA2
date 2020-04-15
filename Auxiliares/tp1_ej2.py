#usr/bin/env python

import matplotlib as map
import numpy as np
import math
#from platform import node

class Node:
#inicio desde un punto x,y,z y especifico el objetivo
    def __init__(self,position):
        self.g = getG
        self.h = getH
        #self.f = getF
        self.position = position[:]     #Por que no anda la posicion
        self.parent = None              #Los hijos que va a tener el nodo (Ver si es necesario)
        #self.state = state[:]
        self.successor_current_cost = 0

#Función para agregar vecinos a la lista de Abiertos (se hace después)
def setNeighbours(Node, OPEN, CLOSED):
    pass
    #return (Neighbours, OPEN, CLOSED)

def getG(Node1, Node2): 

    g = 0    
    ###########################ARREGLAR la posicion del padre
    ###########################DEBO AGREGAR EL OBSTÁCULO################################
    #while (Node.parent != None):
    while (Node1.position[0] != Node2.position[0] and Node1.position[1] != Node2.position[1] and Node1.position[2] != Node2.position[2]):
    
        cont = 0        #Mov. 1 plano: 1(10), 2 planos: 2(14), 3 planos: 3(17)
    #debo hacer la distancia entre el nodo y start    
        if Node1.position[0] != Node2.position[0]: 
            if Node1.position[0] < Node2.position[0]:
                Node1.position[0] += 1         
                cont += 1
        
            else:
                Node1.position[0] -= 1
                cont += 1
                        #Retroceder -1 position -=[1 0 0]    
                
        if Node1.position[1] != Node2.position[1]: 
            if Node1.position[1] < Node2.position[1]:
                Node1.position[1] += 1         
                cont += 1
                        #Avanzar +1 position +=[0 1 0]
                        # y guardar que avanzo para sumar 14 y eso    
            else:
                Node1.position[1] -= 1
                cont += 1
                        #Retroceder -1 position -=[0 1 0]
                        # 
        if Node1.position[2] != Node2.position[2]: 
            if Node1.position[2] < Node.position[2]:
                Node1.position[2] += 1         
                cont += 1
                        #Avanzar +1 position +=[1 0 0]
                        # y guardar que avanzo para sumar 14 y eso    
            else:
                Node1.position[2] -= 1
                cont += 1
                        #Retroceder -1 position -=[1 0 0]  
        if cont == 1:
            G = 10
        elif cont ==2:
            G = 14
        else:
            G = 17

                #Guardo el G
        g += G    
    return(g)

def getH(Node, goal):
    sum = 0
    for i in range(0, 3):
        sum += math.pow((Node.position[i] - goal.position[i]), 2)
    
    if sum == 0:
        return 0
    
    return (math.sqrt(sum))
    

#START es un nodo y goal es una posición
def A_star(Node, goal):
    start = Node            #([2, 2, 2])
    OPEN = []
    CLOSED = []
    #Creo nodo objetivo
    goal = goal             #([0, 0, 0])
    #start.position = [2, 2, 2]
    start.g = 0
    start.h = getH(start, goal)                          
    start.f = start.h
    start.parent =  None                    #Ver si hace falta ponerlo o se puede sacar
    OPEN.append(start)
    
    while (len(OPEN) != 0):
        current = OPEN[0]  
        OPEN.remove(current)                #ACÁ ESTÁ EL ERROR  
                         #Verificar
        #Control para obtener el estado final
        if current.position == goal.position:
            print("Solución encontrada")
            return (reconstruct_path(current)), True


        #Genero vecinos             ESTE ES EL PROBLEMA, NO GENERA VECINOS
        #Neighbours = setNeighbours(current, OPEN, CLOSED)#deberia hacer una lista del otro lado
        Neighbours=[]
        Neighbours.append(current)
        i=0
        
        for x in range((current.position[0] - 1), 3):
            for y in range((current.position[1] - 1), 3):
                for z in range((current.position[2] - 1), 3):
                    
                    Neighbours.append(Node(i, None))
                    Neighbours[i].position= [x, y, z]
    #Si no está en la lista de abiertos, lo agrega
                    if (Neighbours[i] in CLOSED):
                        continue                            #Ver si usar continue o pass
                    elif (Neighbours[i] not in OPEN):
                        OPEN.append(Node)
                    i +=1                 #MAL: hay que agregar nodos nuevos (verificar)
        #def make_nodes(n):
        #    nodes = []
        #    nodes.append(Node(0,None))    # head node
        #    for i in range(1, n):
        #        nodes.append(Node(i, None))
        #        nodes[i-1].next = nodes[i]    #somehow link them          
        #    return nodes

        #    nodes = make_nodes()
        #    head = nodes[0]
        #    second = nodes[1]
        #    last = nodes[-1]



        #Agrego características a los vecinos
        for i in range(0, len(Neighbours)):                     #Ver si está bien planteado (posiciones)
            Neighbours[i].g = getG(Neighbours[i],start)
            Neighbours[i].h = getH(Neighbours[i], goal)
            Neighbours[i].f = Neighbours[i].g + Neighbours[i].h
            Neighbours[i].parent = current                  #CORREGIR
            Neighbours[i].successor_current_cost = Neighbours[i].g + getH(current, Neighbours[i])
        #corregir

        for i in range (0, len(Neighbours)):
            if Neighbours[i] in OPEN:                
                if Neighbours[i].g <= Neighbours[i].successor_current_cost:
                    CLOSED.append(Neighbours[i])
            elif Neighbours[i] in CLOSED:
                if Neighbours[i].g <= Neighbours[i].successor_current_cost:
                    CLOSED.remove(Neighbours[i])
                    OPEN.append(Neighbours[i])
            else:
                OPEN.append(Neighbours[i])
         
        #Agrego vecinos a la lista abierta (sucesores)
        #OPEN.append(Neighbours)
                 #Nodo inicial como el actual, luego se modifica
        

        for i in range(0, len(Neighbours)):
            if (Neighbours[i].f < current.f):
                current = Neighbours[i]
        #Saco el nodo inicial de la lista abierta y lo mando a la cerrada
        CLOSED.append(current)
    
    #Camino recorrido
    #camino = []                             #Lista auxiliar para guardar el camino
    #actual = current

#Hacer funcion externa: esta funcion es para obtener el recorrido 
    #while (actual.parent != None): 
    #    camino.append(actual)
    #    actual = actual.parent

    #print ("Camino, CLOSED")

    #return (camino, CLOSED)

        
# [INDEPENDIENTE DEL PROBLEMA]
def reconstruct_path(ans):
    """
    Función interna de la implementación del algoritmo. Recibe como parámetro un nodo clase Node, objetivo del problema; y la función vuelve hacia atrás con la propiedad node.cameFrom, construyendo la respuesta.
    La función devuelve la solución del problema: una lista con la secuencia de nodos.
    """

    total_path = []

    while (ans.parent != None):
        total_path.append(ans.parent)
        ans = ans.parent

    return total_path
#    Sino podrías decirle
#while(actual.posicion != posicion_inicial)

if __name__ == "__main__":
    goal = Node([0, 0, 0])
    nodo = Node([5, 5, 5])
    a = A_star(nodo, goal)
    b = reconstruct_path(goal)
    print("Total path")
    print(b)
    
