import numpy as np
import math

def mapa(): 
    x=1
    fila=1
    columna=1
    cant_filas_estantes = 3
    cant_columnas_estantes = 3
    pasillo = 3 #nro de columna q esta el 1er pasillo
    m = 1
    n_filas = 5*cant_filas_estantes+1
    n_columnas = 3*cant_columnas_estantes+1
    map = np.zeros((n_filas,n_columnas))
    while(x<=8*cant_columnas_estantes*cant_filas_estantes):
        map[fila][columna] = x
        if x%2==0: #x es par
            fila += 1
            columna -= 1
        else:
            columna += 1
        if x%8==0:
            fila+=1
        x +=1
        if x==(8*cant_filas_estantes*m)+1:
            fila = 1
            columna = pasillo+1
            pasillo += 3 
            m += 1 #par(a recorrer cada columna de estantes
    print(map)
    return (map)

if __name__ == "__main__":
    y = mapa()
    print (y)
    print(len(y))