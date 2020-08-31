#src- python -utc8
from matplotlib import pyplot as plt
from math import cos, sin, pow, pi
import numpy as np

class Theta:

    def __init__(self, valor):
        self.NG=[]
        self.NP=[]
        self.Z=[]
        self.PP=[]
        self.PG=[]
        self.valor=valor                                        #valor actual cambia en cada iteracion (de abcisa)
        self.mu = {'NG': 0,'NP': 0,'Z': 0,'PP': 0,'PG': 0}      #valor de mu en cada particion SE QUEDA CON EL ULTIMO
        self.center={'NG': 0,'NP': 0,'Z': 0,'PP': 0,'PG': 0}

#quiero poner el valor (posicion de cada tita o tita-punto) -> obtener cada mu (para cada particion)
    def calcula_funcion(self, inicio, conjunto, delta_t):
        self.valor=conjunto
        #MODIFICAR: el 90 es para un solo dominio, si cambio debo usar mas general
        #valor de la ordenada deseada sumandole 90 que es desde donde empieza el vector y dividiendo por los pasos
        inicio=abs(inicio)
        self.mu['NG'] = self.NG[int((conjunto+inicio)/delta_t)]
        self.mu['NP'] = self.NP[int((conjunto+inicio)/delta_t)]
        self.mu['Z'] = self.Z[int((conjunto+inicio)/delta_t)]
        self.mu['PP'] = self.PP[int((conjunto+inicio)/delta_t)]
        self.mu['PG'] = self.PG[int((conjunto+inicio)/delta_t)]

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

def simular(theta_0, v_0, a_0, F):
   
    theta = (theta_0 * np.pi) / 180
    v = v_0
    a = a_0

    a = calcula_aceleracion(theta, v, F)
    v = v + a * delta_t
    theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2

    return theta, v, a
    
# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, F):
    
    #Condiciones iniciales
    M = 2 # Masa del carro
    m = 1 # Masa de la pertiga
    l = 1 # Longitud de la pertiga
    g=9.81
    numerador = g * np.sin(theta) + np.cos(theta) * ((-F - m * l * np.power(v, 2) * np.sin(theta)) / (M + m))
    denominador = l * (4/3 - (m * np.power(np.cos(theta), 2) / (M + m)))
    return (numerador / float (denominador))

if __name__ == "__main__":
    delta_t = 0.01                           #0.001    
                                        #en simular cambiar los parametros por variables y poner los iniciales arriba del for
    #Condiciones iniciales
    F=0
    ang=60
    vel=-20
    acel=10
    y=[]
    y1=[]
    y2=[]

#Variable:angulo
    in_theta=-90
    x = np.arange(in_theta, 90, delta_t)         #Cambiar parámetros, para los conj borrosos hacer igual pero con otro dominio
    #Partición Borrosa de Theta
    NP = ['NP', conjunto_borroso(-25, -5, -15, x,'NP'), -15]
    Z = ['Z', conjunto_borroso(-10, 10, 0, x,'Z'), 0]
    PP = ['PP', conjunto_borroso(5, 25, 15, x,'PP'), 15]
    NG = ['NG', conjunto_borroso(-30, -20, 0, x,'NG'), -20]
    PG = ['PG', conjunto_borroso(20, 30, 0, x,'PG'), 20]

    theta = Theta(1)
    theta.NG=NG[1]
    theta.NP=NP[1]
    theta.Z=Z[1]
    theta.PP=PP[1]
    theta.PG=PG[1]

    #Centro de cada conjunto borroso theta
    theta.center['NG']=NG[2]
    theta.center['NP']=NP[2]
    theta.center['Z']=Z[2]
    theta.center['PP']=PP[2]
    theta.center['PG']=PG[2]    

#Variable: velocidad angular
    in_vel=-300
    x = np.arange(in_vel, 300, delta_t)        
    #Partición Borrosa de velocidad angular
    NG = ['NG', conjunto_borroso(-240, -100, 0, x,'NG'), -100]    
    NP = ['NP', conjunto_borroso(-200, 0, 100, x,'NP'), -100]
    Z = ['Z', conjunto_borroso(-100, 100, 0, x,'Z'), 0]
    PP = ['PP', conjunto_borroso(0, 200, 100, x,'PP'), 100]
    PG = ['PG', conjunto_borroso(100, 240, 0, x,'PG'), 100]

    velocidad = Theta(1)
    velocidad.NG=NG[1]
    velocidad.NP=NP[1]
    velocidad.Z=Z[1]
    velocidad.PP=PP[1]
    velocidad.PG=PG[1]
    #Centro de cada conjunto borroso v. angular
    
    velocidad.center['NG']=NG[2]
    velocidad.center['NP']=NP[2]
    velocidad.center['Z']=Z[2]
    velocidad.center['PP']=PP[2]
    velocidad.center['PG']=PG[2]    

    #Conjunto borroso de Fuerza
    #creacion de Particion Borrosa
    NP = ['NP', conjunto_borroso(-25, -5, -15, x,'NP'), -15]
    Z = ['Z', conjunto_borroso(-10, 10, 0, x,'Z'), 1]
    PP = ['PP', conjunto_borroso(5, 25, 15, x,'PP'), 15]
    NG = ['NG', conjunto_borroso(-30, -20, 0, x,'NG'), -20]
    PG = ['PG', conjunto_borroso(20, 30, 0, x,'PG'), 20]
    
    fuerza= Theta(1)

    fuerza.NG=NG[1]
    fuerza.NP=NP[1]
    fuerza.Z=Z[1]
    fuerza.PP=PP[1]
    fuerza.PG=PG[1]
    #Centro de cada conjunto borroso Fuerza
    
    fuerza.center['NG']=NG[2]
    fuerza.center['NP']=NP[2]
    fuerza.center['Z']=Z[2]
    fuerza.center['PP']=PP[2]
    fuerza.center['PG']=PG[2]

    #Vector para guardar cosas para el grafico
   
    dominio = np.arange(0, 30, delta_t) 

    #Aca hacer el for-> ver While y tomar una tolerancia (guardar en un vector base)->primero crear los objetos y despues solo cambiar atributos
    for t in dominio:
        ang, vel, acel = simular(ang, vel, acel, F)
        
        y.append(ang)
        y1.append(vel)
        y2.append(acel)

        #fuerza.calcula_funcion(F,delta_t)         #SE PODRIA BORRAR
        theta.calcula_funcion(in_theta,ang,delta_t)
        velocidad.calcula_funcion(in_vel,vel,delta_t)
        
        #Reglas de inferencia
        fuerza.mu['NG']=max(min(theta.mu['NG'],velocidad.mu['NG']),min(theta.mu['NP'],velocidad.mu['NG']), min(theta.mu['Z'],velocidad.mu['NG']), min(theta.mu['NG'],velocidad.mu['NP']), min(theta.mu['NP'],velocidad.mu['NP']), min(theta.mu['NG'],velocidad.mu['Z']))
        fuerza.mu['NP']=max(min(theta.mu['PP'],velocidad.mu['NG']), min(theta.mu['Z'],velocidad.mu['NP']), min(theta.mu['NP'],velocidad.mu['Z']), min(theta.mu['NG'],velocidad.mu['PP']))
        fuerza.mu['Z']=max(min(theta.mu['PG'],velocidad.mu['NG']), min(theta.mu['PP'],velocidad.mu['NP']), min(theta.mu['Z'],velocidad.mu['Z']), min(theta.mu['NP'],velocidad.mu['PP']), min(theta.mu['NG'],velocidad.mu['PG']))
        fuerza.mu['PP']=max(min(theta.mu['PG'],velocidad.mu['NP']), min(theta.mu['PP'],velocidad.mu['Z']), min(theta.mu['Z'],velocidad.mu['PP']), min(theta.mu['NP'],velocidad.mu['PG']))
        fuerza.mu['PG']=max(min(theta.mu['PG'],velocidad.mu['Z']), min(theta.mu['PG'],velocidad.mu['PP']), min(theta.mu['PG'],velocidad.mu['PG']), min(theta.mu['PP'],velocidad.mu['PP']), min(theta.mu['PP'],velocidad.mu['PG']), min(theta.mu['Z'],velocidad.mu['PG']))

    #OBTENER LA POSICION DE F (DESBORROSIFICAR)->Función aparte
        num=0
        den=0
        for index, i in fuerza.mu.items():
            num += i*fuerza.center[index]
            den += i
        
        F= (num/float (den))

    print(y)

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




    
    