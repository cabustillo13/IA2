#src- python -utc8
from matplotlib import pyplot as plt
from math import cos, sin, pow, pi
import numpy as np

class Theta:

    def __init__(self, valor,ng_center,np_center,z_center,pp_center,pg_center):
        self.NG=[]
        self.NP=[]
        self.Z=[]
        self.PP=[]
        self.PG=[]
        self.valor=valor                                        #valor actual cambia en cada iteracion (de abcisa)
        self.center = {'NG': 0,'NP': 0,'Z': 0,'PP': 0,'PG': 0}
        self.mu = {'NG': 0,'NP': 0,'Z': 0,'PP': 0,'PG': 0}      #valor de mu en cada particion SE QUEDA CON EL ULTIMO

#quiero poner el valor (posicion de cada tita o tita-punto) -> obtener cada mu (para cada particion)
    def calcula_funcion(self, conjunto, delta_t):
        self.valor=conjunto
        #valor de la ordenada deseada sumandole 90 que es desde donde empieza el vector y dividiendo por los pasos
        self.mu['NG'] = self.NG[int((conjunto+90)/delta_t)]
        self.mu['NP'] = self.NP[int((conjunto+90)/delta_t)]
        self.mu['Z'] = self.Z[int((conjunto+90)/delta_t)]
        self.mu['PP'] = self.PP[int((conjunto+90)/delta_t)]
        self.mu['PG'] = self.PG[int((conjunto+90)/delta_t)]
        




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

def simular(t_max, delta_t, theta_0, v_0, a_0):
   
    theta = (theta_0 * np.pi) / 180
    v = v_0
    a = a_0
    y = []
    x = np.arange(0, t_max, delta_t)
    for t in x:
        a = calcula_aceleracion(theta, v, 0)
        v = v + a * delta_t
        theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
        y.append(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
    ax.grid()
    
    plt.show()


# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):
    
    #Condiciones iniciales
    M = 2 # Masa del carro
    m = 1 # Masa de la pertiga
    l = 1 # Longitud de la pertiga
    g=9.81
    numerador = g * np.sin(theta) + np.cos(theta) * ((-f - m * l * np.power(v, 2) * np.sin(theta)) / (M + m))
    denominador = l * (4/3 - (m * np.power(np.cos(theta), 2) / (M + m)))
    return numerador / denominador

if __name__ == "__main__":
    delta_t=0.001                             #0.001
    x = np.arange(-90, 90, delta_t)
    simular(10, 0.0001, 45, 0, 0)
    #Partición Borrosa de Theta
    NP = ['NP', conjunto_borroso(-25, -5, -15, x,'NP')]
    Z = ['Z', conjunto_borroso(-10, 10, 0, x,'Z')]
    PP = ['PP', conjunto_borroso(5, 25, 15, x,'PP')]
    NG = ['NG', conjunto_borroso(-30, -20, 0, x,'NG')]
    PG = ['PG', conjunto_borroso(20, 30, 0, x,'PG')]

    theta = Theta(1,0,-15,0,15,0)
    theta.NG=NG[1]
    theta.NP=NP[1]
    theta.Z=Z[1]
    theta.PP=PP[1]
    theta.PG=PG[1]

    #Partición Borrosa de velocidad angular
    NP = ['NP', conjunto_borroso(-25, -5, -15, x,'NP')]
    Z = ['Z', conjunto_borroso(-10, 10, 0, x,'Z')]
    PP = ['PP', conjunto_borroso(5, 25, 15, x,'PP')]
    NG = ['NG', conjunto_borroso(-30, -20, 0, x,'NG')]
    PG = ['PG', conjunto_borroso(20, 30, 0, x,'PG')]

    velocidad = Theta(1,0,-15,0,15,0)
    velocidad.NG=NG[1]
    velocidad.NP=NP[1]
    velocidad.Z=Z[1]
    velocidad.PP=PP[1]
    velocidad.PG=PG[1]
                       
    theta.calcula_funcion(15,0.001)
    velocidad.calcula_funcion(9,0.001)

    #Buscar los mu distintos de 0 para maximo-> discriminar =0 y tomar el minimo
    #Tal vez no haga falta-> cumplir con reglas
    def minimo(objeto):
        minimo=1
        for item in theta.mu:
            if (theta.mu[item]!=0 and theta.mu[item]<minimo):
                minimo = theta.mu[item] 
    #Conjunto borroso de Fuerza
    #creacion de Particion Borrosa
    fuerza= Theta(1,0,-15,0,15,0)
    NP = ['NP', conjunto_borroso(-25, -5, -15, x,'NP')]
    Z = ['Z', conjunto_borroso(-10, 10, 0, x,'Z')]
    PP = ['PP', conjunto_borroso(5, 25, 15, x,'PP')]
    NG = ['NG', conjunto_borroso(-30, -20, 0, x,'NG')]
    PG = ['PG', conjunto_borroso(20, 30, 0, x,'PG')]

    fuerza.calcula_funcion(0,0.001)         #SE PODRIA BORRAR

    #Reglas de inferencia
    fuerza.mu['NG']=max(min(theta.mu['NG'],velocidad.mu['NG']),min(theta.mu['NP'],velocidad.mu['NG']), min(theta.mu['Z'],velocidad.mu['NG']), min(theta.mu['NG'],velocidad.mu['NP']), min(theta.mu['NP'],velocidad.mu['NP']), min(theta.mu['NG'],velocidad.mu['Z']))
    fuerza.mu['NP']=max(min(theta.mu['PP'],velocidad.mu['NG']), min(theta.mu['Z'],velocidad.mu['NP']), min(theta.mu['NP'],velocidad.mu['Z']), min(theta.mu['NG'],velocidad.mu['PP']))
    fuerza.mu['Z']=max(min(theta.mu['PG'],velocidad.mu['NG']), min(theta.mu['PP'],velocidad.mu['NP']), min(theta.mu['Z'],velocidad.mu['Z']), min(theta.mu['NP'],velocidad.mu['PP']), min(theta.mu['NG'],velocidad.mu['PG']))
    fuerza.mu['PP']=max(min(theta.mu['PG'],velocidad.mu['NP']), min(theta.mu['PP'],velocidad.mu['Z']), min(theta.mu['Z'],velocidad.mu['PP']), min(theta.mu['NP'],velocidad.mu['PG']))
    fuerza.mu['PG']=max(min(theta.mu['PG'],velocidad.mu['Z']), min(theta.mu['PG'],velocidad.mu['PP']), min(theta.mu['PG'],velocidad.mu['PG']), min(theta.mu['PP'],velocidad.mu['PP']), min(theta.mu['PP'],velocidad.mu['PG']), min(theta.mu['Z'],velocidad.mu['PG']))

#OBTENER LA POSICION DE F (DESBORROSIFICAR)->Función aparte

    num=0
    den=0
    for index, i in enumerate(fuerza.mu):
        num += i*fuerza.center[index]
        den += i
    Posicion_F= num/den

#Hacer una funcion aparte para los plots
#    plt.plot(x, NP[1], label="NP")
#    plt.plot(x, Z[1], label="Z")
#    plt.plot(x, PP[1], label="PP")
#    plt.plot(x, PG[1], label="PG")
#    plt.plot(x, NG[1], label="NG")
#    plt.legend()
#    plt.xlabel="Ángulo"
#    plt.show()


    
    