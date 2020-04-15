import numpy as np
import math

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
    print(np.matrix(map))
    return(map)

if __name__ == "__main__":
    y = generate_map()
    print (y)
    print(len(y))