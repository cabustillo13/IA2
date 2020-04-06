from random import randint
import math
import numpy as np

"----------------------------------CODIGO MODIFICADO DEL COLO--------------------------------------------------"
import numpy as np
import time
import math

class Nodo:
    def __init__(self,padre=None,pos=None):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    def calculate_h(self,end): #Heuristica entre nodo actual y final
        self.h = (self.pos[0]-end[0])**2+(self.pos[1]-end[1])**2
    def calculate_g(self,current): #camino recorrido
        self.g = current.g + 1
    def calculate_f(self): 
        self.f = self.g+self.h

def generate_map(n_rows_shelves=3,n_columns_shelves=2): #Polimorfismo por repeticion: Se pueden pasar parametros y que adopte estos pero por defecto es como en el TP
    n_rows = 5*n_rows_shelves+1
    n_columns = 4*n_columns_shelves
    x=1
    row=1
    column=1
    pasillo = 3 #nro de columna que esta el 1er pasillo
    m = 1       #multiplicador para recorrer cada columna de estantes
    map = np.zeros((n_rows,n_columns),int) #crea matriz de n*m de enteros
    while(x<=8*n_columns_shelves*n_rows_shelves):
        map[row][column] = x
        if x%2==0: #x es par
            row += 1
            column -= 1
        else:
            column += 1
        if x%8==0:
            row+=1
        x +=1
        if x==(8*n_rows_shelves*m)+1:
            row = 1
            column = pasillo+2
            pasillo += 4 
            m += 1 
    #print(np.matrix(map))
    return(map)

def search_position_of(value,map):
    for index,row in enumerate(map):
        if value in row: #row es la fila entera. index es el numero de la fila donde esta el valor buscado         
            fila = np.ndarray.tolist(row) #row es del tipo numpy.ndarray y no tiene atributo index. con esta linea arreglo eso. Es un cambio de tipo de variable
            column = fila.index(value)    #columna en la que esta el valor buscado
            if map[index][column-1] == 0:
                column -= 1
            elif map[index][column+1] == 0:
                column += 1
            return (index,column)

def a_star(map,start,end):
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
            return(path[::-1]) #retorna el camino "invertido" porque parte del final al inicio

        neighbours = [] 
        for a in [(1,0),(-1,0),(0,1),(0,-1)]: #para cada tupla de esta lista, guardar los vecinos si es posible
            pos = (a[0] + current.pos[0],a[1] + current.pos[1])
            if (0 <= current.pos[0]+a[0] < len(map)) and (0 <= current.pos[1]+a[1] < len(map[0])) and map[pos]==0:
                neighbours.append(Nodo(current,pos))

        for neighbour in neighbours:
            if neighbour in CLOSED:
                continue 
            Nodo.calculate_g(neighbour, current)
            Nodo.calculate_h(neighbour,end) 
            Nodo.calculate_f(neighbour)
            if neighbour.g < current.g or neighbour not in OPEN: 
                neighbour.padre = current
                if neighbour not in OPEN and neighbour not in CLOSED:
                    OPEN.append(neighbour)
            
def distancia_solucion(a,b):
    
    flag=0
    if(a<b):
        flag=1
    if(a>b):
        auxiliar=b
        b=a
        a=auxiliar
        flag=1
    if (flag==1):
        map = generate_map() #pueden pasarse 2 parametros, fila y columnas de estaterias
        start = search_position_of(a,map) 
        end = search_position_of(b,map)  
        solution = a_star(map,start,end)
        return (len(solution))
    else:
        return 0
"--------------------------------------------------------------FIN CODIGO COLO-----------------------------------------------------------------"

def main():
    
    #k-2 representa la cantidad de paradas que se va a hacer en el picking
    k=10
    ubi= np.zeros(k,int)
    ubi_min = np.zeros(k,int)
    ubi2 = np.zeros(k,int)
    
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
    print("Creacion de las ubi aleatorias")
    #Son los estantes que yo defini arbitrariamente por donde tienen que pasar
    ubi[1],ubi[2],ubi[3],ubi[4],ubi[5],ubi[6],ubi[7],ubi[8] = 10,18,4,29,24,13,23,9
    #NOTA:Como k=10, significa que va a tener 8 paradas(o lugares de picking) y las otras 2 posiciones son donde arranca y termina.
                
    #Se asume que se comienza y termina en uno de los extremos del almacen 
    ubi[0]=0 #Posicion inicial de picking
    ubi[k-1]=0 #Posicion final de picking
    
    for i in range(0,k):
        ubi_min[i]=ubi[i]
    
    for i in range(1,k):
        #Aca se va sumando el costo del recorrido
        distancia_min = distancia_min + distancia_solucion(ubi_min[i],ubi_min[i-1])
    
    it=0 
    ITMAX = 1000 #Cantidad de iteraciones maximas
    
    while (it != ITMAX):
        it+=1
        distancia=0
        distancia2=0
        
        #Calculo de la calidad de la solucion
        T = (ITMAX)/it #Es arbitrario, se puede poner alguna otra funcion para definir T
        
        for i in range(0,k):
            ubi2[i]=ubi[i]
            
        for i in range(1,k):
            distancia = distancia + distancia_solucion(ubi[i],ubi[i-1])
        
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
            distancia2 = distancia2 + distancia_solucion(ubi2[i], ubi2[i-1])
            
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
