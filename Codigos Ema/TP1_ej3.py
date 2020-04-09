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
        self.h = (self.pos[0]-end.pos[0])**2+(self.pos[1]-end.pos[1])**2
    def calculate_g(self,current): #camino recorrido
        self.g = current.g + 1
    def calculate_f(self): 
        self.f = self.g+self.h

def generate_map(order=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],n_rows_shelves=3,n_columns_shelves=2): #Se pueden pasar parametros y que adopte estos pero por defecto es como en el TP
    n_rows = 5*n_rows_shelves+1
    n_columns = 4*n_columns_shelves
    x=1
    row=1
    column=1
    pasillo = 3 #nro de columna que esta el 1er pasillo
    m = 1       #multiplicador para recorrer cada columna de estantes
    map = np.zeros((n_rows,n_columns),int) #crea matriz de n*m de enteros
    while(x<=8*n_columns_shelves*n_rows_shelves):
        map[row][column] = order[x-1]
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

    Nodo.calculate_h(start,end)
    Nodo.calculate_f(start)
    current = start
    OPEN.append(current)

    while current.pos != end.pos:
        current = OPEN[0]
        current_index = 0
        
        for i,aux in enumerate(OPEN):
            if aux.f < current.f:
                current = aux
                current_index = i
        OPEN.pop(current_index) 
        CLOSED.append(current)  

        if current.pos == end.pos:
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
            Nodo.calculate_g(neighbour,current)
            Nodo.calculate_h(neighbour,end) 
            Nodo.calculate_f(neighbour)
            if neighbour.g < current.g or neighbour not in OPEN: 
                neighbour.padre = current
                if neighbour not in OPEN and neighbour not in CLOSED:
                    OPEN.append(neighbour)
            
def main():
    print("Ejercicio 3")
    t_prom = 0 #para calcular el promedio de 5 A*
    n=5
    map = generate_map() #pueden pasarse 3 parametros, orden del almacen,fila y columnas de estaterias
    start = Nodo(None,search_position_of(1,map))
    end = Nodo(None,search_position_of(43,map))
    for i in range(n):
        t1 = time.time()
        solution = a_star(map,start,end)
        t2 = time.time()
        t_prom += t2-t1 
    print("Camino:")
    for pos in solution:
        map[pos] = 1 #"Pintar" solucion con unos
        print(pos)
    print(np.matrix(map),"\n\nTiempo de ejecucion promedio A*: ",str(round(t_prom/n,8)))
    
if __name__ == "__main__":
    main()