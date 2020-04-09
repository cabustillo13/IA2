from random import randint
import math
import numpy as np
import TP1_ej3 as A_estrella
from time import time

def distancia_solucion(a,b,map):
    if (a < b):
        #map = A_estrella.generate_map() #pueden pasarse 2 parametros, fila y columnas de estaterias
        start = A_estrella.Nodo(None,A_estrella.search_position_of(a,map)) #nodos en vez de tuplas
        end = A_estrella.Nodo(None,A_estrella.search_position_of(b,map))
        solution = A_estrella.a_star(map,start,end)    
        if (a != b):
            return (len(solution))
        else:
            return 0
    else:
        return 0

def simulated_annealing(picking_list,order,want_to_print): 
    #tener como parametro una lista y el mapa
    map = A_estrella.generate_map(order) #pueden pasarse 2 parametros, fila y columnas de estaterias
    
    #k-2 representa la cantidad de paradas que se va a hacer en el picking
    k=len(picking_list)+2
    ubi= np.zeros(k,int)
    ubi_min = np.zeros(k,int)
    ubi2 = np.zeros(k,int)
    
    for i in range(1,k-1):
        ubi[i] = picking_list[i-1]
    
    distancia,distancia2,distancia_min = 0,0,0 #Forma de asignar valores para evitar el "cant assign to literal" en una sola linea de codigo
            
    for i in range(0,k):
        ubi_min[i]=ubi[i]
    for i in range(1,k):
        #Aca se va sumando el costo del recorrido / es una especie de valor semilla
        distancia_min = distancia_min + distancia_solucion(ubi_min[i],ubi_min[i-1],map)
    
    it=0
    ITMAX = 1500 #Cantidad de iteraciones maximas
    
    while (it != ITMAX):
        it+=1
        distancia=0
        distancia2=0
        T = (ITMAX)/it #Es arbitrario, se puede poner alguna otra funcion para definir T
        
        for i in range(0,k):
            ubi2[i]=ubi[i]
            
        for i in range(1,k):
            distancia = distancia + distancia_solucion(ubi[i],ubi[i-1],map)
        
        #Obtencion de un vecino
        swap1= randint(1, k-2)
        swap2= randint(1, k-2)
        
        while (swap1==swap2):
            swap2= randint(1, k-2)
            
        aux2 = ubi2[swap1] #Lo guardo para no perder el dato
        ubi2[swap1] = ubi2[swap2]
        ubi2[swap2] = aux2
        
        #Calculo de la calidad del vecino - Temple simulado
        for i in range(1,k):
            distancia2 = distancia2 + distancia_solucion(ubi2[i], ubi2[i-1],map)
            
        if (distancia2 < distancia):
            for i in range (0,k):
                ubi[i] = ubi2[i] 
        else: #Cuando distancia2 > distancia, la probabilidad que lo acepte segun el temple simulado esta dado de esta manera
            if((randint(0,100)/100) < math.exp(distancia - distancia2)/T):
                for i in range (0,k):
                    ubi[i] = ubi2[i] 
                
        if (distancia2 < distancia_min):
            for i in range(0,k):
                ubi_min[i]= ubi2[i]
                distancia_min= distancia2
    if want_to_print:
        print("Disposicion de posiciones de la solucion:")
        for i in range(len(picking_list)+2):
            print(ubi_min[i])
        print("Distancia minima lograda con esa disposicion:", distancia_min)
    
    return distancia_min
    
def main():
    print("Ejercicio 5")
    order = []
    for i in range(48):
        order.append(i+1)
    lista_picking = [16,48,25,1,2,37,16,17,21,24]
    t1 = time()
    simulated_annealing(lista_picking,order,True)
    t2 = time()
    print("Tiempo de ejecucion:",round(t2-t1,2),"segundos")
    
if __name__ == "__main__":
    main()