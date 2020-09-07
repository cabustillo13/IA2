import numpy as np
import matplotlib.pyplot as plt

#Datos continuos
def generar_datos_continuos(cantidad_ejemplos, cantidad_clases):
    
    x = np.zeros((cantidad_ejemplos,1))
    t = np.zeros((cantidad_ejemplos,1), dtype="uint8")   
    
    AMPLITUD_ALEATORIEDAD = 0.1 
    FACTOR_ANGULO = 0.79
    
    for i in range(cantidad_ejemplos):
        t[i] = AMPLITUD_ALEATORIEDAD * i + FACTOR_ANGULO
        x[i] = t[i] + np.random.randint(-2,2)
    return x, t

#Invocar la funcion para graficar
x2,t2 = generar_datos_continuos(300,3)
tamano = len(x2)
abcisa = list()
for i in range(tamano):
    abcisa.append(i)
    
plt.plot(abcisa,x2,t2)
plt.xlabel('epochs')
plt.ylabel('x vrs t')
plt.show()
