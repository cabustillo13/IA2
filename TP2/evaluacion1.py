#src- python -utc8
from matplotlib import pyplot as plt
from math import cos, sin, pow, pi
import numpy as np



#puede ser un metodo tambien
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

    
# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, F):
    
    #Condiciones iniciales
    M = 2 # Masa del carro
    m = 1 # Masa de la pertiga
    l = 1 # Longitud de la pertiga
    g=9.81
    #CAMBIE EL SIGNO DE F
    numerador = g * np.sin(theta) + np.cos(theta) * ((F - m * l * np.power(v, 2) * np.sin(theta)) / (M + m))
    denominador = l * (4/3 - (m * np.power(np.cos(theta), 2) / (M + m)))
    return (numerador / float (denominador))

if __name__ == "__main__":
    delta_t = 0.01                           #0.001    
    #Condiciones iniciales
    F=0
    angulo=60
    vel=-20
    acel=10
    
    
    ang = (angulo * np.pi) / 180

    ang0=ang
    vel0=vel
    acel0=acel

    y=[]
    y1=[]
    y2=[]

    z=[]
    z1=[]
    z2=[]
#Variable:angulo
    in_theta=-90
    x = np.arange(in_theta, 90, delta_t)         #Cambiar parámetros, para los conj borrosos hacer igual pero con otro dominio
    #Partición Borrosa de Theta
    

#Variable: velocidad angular
    

    #Vector para guardar cosas para el grafico
   
    dominio = np.arange(0, 30, delta_t) 

    #Aca hacer el for-> ver While y tomar una tolerancia (guardar en un vector base)->primero crear los objetos y despues solo cambiar atributos
    for t in dominio:
    #    ang0, vel0, acel0= simular (delta_t,(theta_0), v_0, 0, 0)
     
        acel0 = calcula_aceleracion(ang0, vel0, 0)
        vel0 = vel0 + acel0 * delta_t
        ang0 = ang0 + vel0 * delta_t + acel0 * np.power(delta_t, 2) / 2

        z.append(ang0)
        z1.append(vel0)
        z2.append(acel0) 
        
    #    ang, vel, acel = simular(delta_t, ang, vel, acel, F)
        

        F=0
        acel = calcula_aceleracion(ang, vel, F)
        vel = vel + acel * delta_t
            ang = ang + vel * delta_t + acel * np.power(delta_t, 2) / 2
    
        y.append(ang)
        y1.append(vel)
        y2.append(acel)        
       

    fig0 = plt.figure(1)
    plt.plot(dominio, z) 
    #fig0.set(title='Vibraciones libres')

    fig, (ax, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 5))
    ax.plot(dominio, y)

    ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
    ax.grid()
    
    ax1.plot(dominio, y1)
    ax1.set(xlabel='time (s)', ylabel='rad/s', title='Delta t = ' + str(delta_t) + " s")
    ax1.grid()

    ax2.plot(dominio, y2)
    ax2.set(xlabel='time (s)', ylabel='aceleracion', title='Delta t = ' + str(delta_t) + " s")
    ax2.grid()
    
    plt.show()
