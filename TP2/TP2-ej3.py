#src- python -utc8
from matplotlib import pyplot as plt
from math import cos, sin, pow, pi
import numpy as np

def conjunto_borroso(min, max, center, x, tag):
    '''
    Creación de la partición borrosa, se tuvieron en cuenta 5 conjuntos borrosos'''
    y = []
    for i in x:
        if tag == 'NG':
            if (i<=min):
                z=1
            elif ((i>min) and (i<=max)):
                z=1-(i-min)/(max-min)
            else:
                z=0
            y.append(z)
        if tag == 'PG':
            if (i<=min):
                z=0
            elif((i>min) and (i<max)):
                z=(i-min)/(max-min)
            else:
                z=1
            y.append(z)
        if ((tag!='PG') and (tag!='NG')):
            if ((i>min) and (i<=center)):
                z=(i-min)/(center-min)
            elif ((i>center) and (i<=max)):
                z=1-(i-center)/(max-center)
            else:
                z=0
            y.append(z)
    return(y)
'''
def actualizacion(theta, F, M, m, l, g):
    num=g*sin(theta[0])+cos((-F-m*l*pow(theta[1],2)*sin(theta[0]))/(M+m))
    den=l*((4*3)-((m*pow(cos(theta[0]),2))/(M+m))
    acel=num/den
    theta[2]=num/den
    return (theta[2])
'''


if __name__ == "__main__":
    delta_t=0.001
    x = np.arange(-90, 90, delta_t)
    NP = ('NP', conjunto_borroso(-25, -5, -15, x,'NP'))
    Z = ('Z', conjunto_borroso(-10, 10, 0, x,'Z'))
    PP = ('PP', conjunto_borroso(5, 25, 15, x,'PP'))
    NG = ('NG', conjunto_borroso(-30, -20, 0, x,'NG'))
    PG = ('PG', conjunto_borroso(20, 30, 0, x,'PG'))

    plt.plot(x, NP[1], label="NP")
    plt.plot(x, Z[1], label="Z")
    plt.plot(x, PP[1], label="PP")
    plt.plot(x, PG[1], label="PG")
    plt.plot(x, NG[1], label="NG")
    plt.legend()
    plt.xlabel="Ángulo"
    plt.show()
    #Condiciones iniciales
    theta=[]
    theta[0]=10
    theta[1]=2
    theta[2]=0
    F=0
    g=9.81
    l=1
    m=1
    M=5
    #Reglas de inferencia
     