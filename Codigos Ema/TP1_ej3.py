import numpy as np
from time import time

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
        if value in row: #row es la row entera. index es el numero de la fila donde esta el value buscado         
            f = np.ndarray.tolist(row) #row es del tipo numpy.ndarray y no tiene atributo index. con esta linea arreglo eso
            column = f.index(value)
            if map[index][column-1] == 0:
                column -= 1
            elif map[index][column+1] == 0:
                column += 1
            return (index,column)

def a_star(map,n_rows,n_columns,start,end):
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
        for i,aux in enumerate(OPEN): #1
            if aux.f < current.f:
                current = aux
                current_index = i
        OPEN.pop(current_index) #2
        CLOSED.append(current)  #3
        
        if current.pos == end:
            path = []
            while current is not None:
                path.append(current.pos)
                current = current.padre
            return(path[::-1]) #retorna el camino "invertido" porque parte del final al inicio

        neighbours_pos = [(current.pos[0]+a[0], current.pos[1]+a[1]) for a in [(-1,0), (1,0), (0,-1), (0,1)] if ((0 <= current.pos[0]+a[0] < n_rows) and (0 <= current.pos[1]+a[1] < n_columns)) and map[current.pos[0]+a[0], current.pos[1]+a[1]]==0]
        neighbours = [] #4

        for i in neighbours_pos:
            neighbours.append(Nodo(current,i))

        for neighbour in neighbours:
            if neighbour in CLOSED:
                continue #5
            Nodo.calculate_g(neighbour)
            Nodo.calculate_h(neighbour,end) 
            Nodo.calculate_f(neighbour)
            if neighbour.g < current.g or neighbour not in OPEN: #5
                neighbour.padre = current
                if neighbour not in OPEN and neighbour not in CLOSED:
                    OPEN.append(neighbour)
            
def main():
    n_rows_shelves = 3     
    n_columns_shelves = 3  
    n_rows = 5*n_rows_shelves+1
    n_columns = 3*n_columns_shelves+1
    t_prom = 0 #para calcular el promedio de 100 A*

    map = generate_map(n_rows_shelves,n_columns_shelves,n_rows,n_columns)
    start = search_position_of(1,map) 
    end = search_position_of(72,map)  
    for i in range(20):
        t1 = time()
        solution = a_star(map,n_rows,n_columns,start,end)
        t2 = time()
        t_prom = t_prom+t2-t1 
    #"Pintar" solucion con unos
    print("\nCamino:")
    for pos in solution:
        map[pos] = 1
        print(pos)
    print("\n",map,"\n\nTiempo de ejecucion promedio A*: ",str(round(t_prom/20,8)))

if __name__ == "__main__":
    main()