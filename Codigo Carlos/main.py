from random import randint
import math
import numpy as np

import TP1_ej3 as A_estrella

def main():
    
    #k-2 representa la cantidad de paradas que se va a hacer en el picking
    k=10
    ubi= np.zeros(k)
    ubi_min = np.zeros(k)
    
    #distancia: Pertenece al nodo con la menor distancia en su momento / distancia total a recorrer
    #distancia_min: Pertenece a la distancia minima de todos los nodos 
    #distancia2: Es la ditancia que se esta evaluando para cada nodo
    distancia,distancia2,distancia_min = 0,0,0 #Forma de asignar valores para evitar el "cant assign to literal" en una sola linea de codigo
    
    #Defino ubicaciones ubi inicialmente con valores aleatorios
    for i in range(1,k):
        skip = 0
        aux = randint(1,32)
        
        for j in range(0,i):
            if (aux == ubi[j]):
                    skip = 1
                    break
            
        if(skip==0):
            ubi[i] = aux
        else:
            i-=1
        
    #Son las ubicaciones que yo defini arbitrariamente por donde tienen que pasar
    ubi[1],ubi[2],ubi[3],ubi[4],ubi[5],ubi[6],ubi[7],ubi[8] = 10,18,4,29,24,13,23,9
    #NOTA:Como k=10, significa que va a tener 8 paradas(o lugares de picking) y las otras 2 posiciones son donde arranca y termina.
                
    #Se asume que se comienza y termina en uno de los extremos del almacen 
    ubi[0]=0 #Posicion inicial de picking
    ubi[k-1]=0 #Posicion final de picking
    
    for i in range(0,k):
        ubi_min[i]=ubi[i]
    
    for i in range(1,k):
        #Aca se va sumando el costo del recorrido
        distancia_min = distancia_min + A_estrella.Nodo.calculate_h(ubi_min[i],ubi_min[i-1])
    
    it=0 
    ITMAX = 500 #Cantidad de iteraciones maximas
    
    while (it != ITMAX):
        it+=1
        distancia=0
        distancia2=0
        
        #Calculo de la calidad de la solucion
        T = double(ITMAX)/it #Es arbitrario, se puede poner alguna otra funcion para definir T
        
        for i in range(0,k):
            ubi2[i]=ubi[i]
            
        for i in range(1,k):
            distancia = distancia + A_estrella.Nodo.calculate_h(ubi[i],ubi[i-1])
            
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
            distancia2 = distancia2 + A_estrella.Nodo.calculate_h(ubi2[i], ubi2[i-1])
            
        if (distancia2 < distancia):
            for i in range (0,k):
                ubi[i] = ubi2[i] 
        else: #Cuando distancia2 > distancia, la probabilidad que lo acepte segun el temple simulado esta dado de esta manera
            if(double(randint(0,100)/100) < math.exp(double(distancia - distancia2)/T)):
                for i in range (0,k):
                    ubi[i] = ubi2[i] 
                
        if (distancia2 < distancia_min):
            for i in range[0,k]:
                ubi_min[i]= ubi2[i]
                distancia_min= distancia2
                
    
    print("Posiciones finales: ")
    for i in range(0,k):
        print(ubi[i])
    print("Distancia total a recorrer: ", distancia)
    print("Posiciones minimas visitadas: ")
    for i in range(0,k):
        print(ubi_min[i])
    print("Distancia minima lograda: ", distancia_min)
    
if __name__ == "__main__":
    main()
    
