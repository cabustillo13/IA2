#src- python -utc8
from matplotlib import pyplot as plt
from math import cos, sin, pow, pi
import numpy as np

delta_t=0.001                             #0.001
x = np.arange(-90, 90, delta_t)

class Theta:
    def __init__(self, valor,ng_center,np_center,z_center,pp_center,pg_center):
        self.NG=[]
        self.NP=[]
        self.Z=[]
        self.PP=[]
        self.PG=[]
        self.valor=valor                                        #valor actual cambia en cada iteracion (de abcisa)
        self.center = {'NG': ng_center,'NP': np_center,'Z': z_center,'PP': pp_center,'PG': pg_center}
        self.mu = {'NG': 0,'NP': 0,'Z': 0,'PP': 0,'PG': 0}      #valor de mu en cada particion SE QUEDA CON EL ULTIMO

    def calcula_funcion(self, valor, delta_t):
        self.valor = valor
        #valor de la ordenada deseada sumandole 90 que es desde donde empieza el vector y dividiendo por los pasos
        self.mu['NG'] = self.NG[int((valor+90)/delta_t)]
        self.mu['NP'] = self.NP[int((valor+90)/delta_t)]
        self.mu['Z'] = self.Z[int((valor+90)/delta_t)]
        self.mu['PP'] = self.PP[int((valor+90)/delta_t)]
        self.mu['PG'] = self.PG[int((valor+90)/delta_t)]
        
def conjunto_borroso(min, max, center, tag):
    #Creación de la partición borrosa, se tuvieron en cuenta 5 conjuntos borrosos
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

def simular(t_max, delta_t, theta_0, v_0, a_0, F):
    theta = (theta_0 * np.pi) / 180
    v = v_0
    a = a_0
    y = []
    T = np.arange(0, t_max, delta_t)
    index=0
    for t in T:
        a = calcula_aceleracion(theta, v, F[index])
        v = v + a * delta_t
        theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
        y.append(theta)
        index += 1 

    # fig, ax = plt.subplots()
    # ax.plot(x, y)

    # ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
    # ax.grid()
    
    # plt.show()

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

def crea_Theta():
    theta = Theta(1,-25,-15,0,15,25)
    NG = ['NG', conjunto_borroso(-30, -20, theta.center['NG'],'NG')]
    NP = ['NP', conjunto_borroso(-25, -5, theta.center['NP'],'NP')]
    Z = ['Z', conjunto_borroso(-10, 10, theta.center['Z'],'Z')]
    PP = ['PP', conjunto_borroso(5, 25, theta.center['PP'],'PP')]
    PG = ['PG', conjunto_borroso(20, 30, theta.center['PG'],'PG')]
    theta.NG=NG[1]
    theta.NP=NP[1]
    theta.Z=Z[1]
    theta.PP=PP[1]
    theta.PG=PG[1]
    return theta

def crea_Theta_p():
    velocidad = Theta(1,-50,-30,0,30,50)
    NG = ['NG', conjunto_borroso(-60, -40, theta.center['NG'],'NG')]
    NP = ['NP', conjunto_borroso(-50, -10, theta.center['NP'],'NP')]
    Z = ['Z', conjunto_borroso(-20, 20, theta.center['Z'],'Z')]
    PP = ['PP', conjunto_borroso(10, 50, theta.center['PP'],'PP')]
    PG = ['PG', conjunto_borroso(40, 60, theta.center['PG'],'PG')]
    velocidad.NG=NG[1]
    velocidad.NP=NP[1]
    velocidad.Z=Z[1]
    velocidad.PP=PP[1]
    velocidad.PG=PG[1]
    return velocidad

def crea_fuerza():
    fuerza = Theta(0,-250,-150,0,150,250)    
    NG = ['NG', conjunto_borroso(-300, -200, theta.center['NG'],'NG')]
    NP = ['NP', conjunto_borroso(-250, -50, theta.center['NP'],'NP')]
    Z = ['Z', conjunto_borroso(-100, 100, theta.center['Z'],'Z')]
    PP = ['PP', conjunto_borroso(50, 250, theta.center['PP'],'PP')]
    PG = ['PG', conjunto_borroso(200, 300, theta.center['PG'],'PG')]
    fuerza.NG=NG[1]
    fuerza.NP=NP[1]
    fuerza.Z=Z[1]
    fuerza.PP=PP[1]
    fuerza.PG=PG[1]
    return fuerza

if __name__ == "__main__":  
    theta = crea_Theta()
    velocidad = crea_Theta_p()
    fuerza = crea_fuerza()
    
    fuerza_lista = []

    for t in range(len(x)):

        theta.calcula_funcion(15,0.001) #Como obtener los nuevos valores de theta y v??
        velocidad.calcula_funcion(9,0.001)
        
        #Reglas de inferencia
        fuerza.mu['NG']=max(min(theta.mu['NG'],velocidad.mu['NG']),min(theta.mu['NP'],velocidad.mu['NG']), min(theta.mu['Z'],velocidad.mu['NG']), min(theta.mu['NG'],velocidad.mu['NP']), min(theta.mu['NP'],velocidad.mu['NP']), min(theta.mu['NG'],velocidad.mu['Z']))
        fuerza.mu['NP']=max(min(theta.mu['PP'],velocidad.mu['NG']), min(theta.mu['Z'],velocidad.mu['NP']), min(theta.mu['NP'],velocidad.mu['Z']), min(theta.mu['NG'],velocidad.mu['PP']))
        fuerza.mu['Z']=max(min(theta.mu['PG'],velocidad.mu['NG']), min(theta.mu['PP'],velocidad.mu['NP']), min(theta.mu['Z'],velocidad.mu['Z']), min(theta.mu['NP'],velocidad.mu['PP']), min(theta.mu['NG'],velocidad.mu['PG']))
        fuerza.mu['PP']=max(min(theta.mu['PG'],velocidad.mu['NP']), min(theta.mu['PP'],velocidad.mu['Z']), min(theta.mu['Z'],velocidad.mu['PP']), min(theta.mu['NP'],velocidad.mu['PG']))
        fuerza.mu['PG']=max(min(theta.mu['PG'],velocidad.mu['Z']), min(theta.mu['PG'],velocidad.mu['PP']), min(theta.mu['PG'],velocidad.mu['PG']), min(theta.mu['PP'],velocidad.mu['PP']), min(theta.mu['PP'],velocidad.mu['PG']), min(theta.mu['Z'],velocidad.mu['PG']))

        aa = list(fuerza.center.values())
        #DESBORROSIFICACION
        num = 0
        den = 0
        fuerza_c = list(fuerza.center.values())
        for index, i in enumerate(list(fuerza.mu.values())):
            num += i*fuerza_c[index]
            den += i
        fuerza.valor = num/den
        fuerza_lista.append(fuerza.valor)

    simular(10,0.0001,45,0,0,fuerza_lista)

#    plt.plot(x, NP[1], label="NP")
#    plt.plot(x, Z[1], label="Z")
#    plt.plot(x, PP[1], label="PP")
#    plt.plot(x, PG[1], label="PG")
#    plt.plot(x, NG[1], label="NG")
#    plt.legend()
#    plt.xlabel="Ángulo"
#    plt.show()


    
    