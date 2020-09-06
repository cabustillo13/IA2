import numpy as np
import matplotlib.pyplot as plt

def generar_datos_continuos(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1
    n = int(cantidad_ejemplos / cantidad_clases)
#probar
#    gg=np.random.dirichlet(np.ones(10),size=1)
######################    
    angulos = np.linspace(1 * np.pi * FACTOR_ANGULO, (1 + 1) * np.pi * FACTOR_ANGULO, n)
    x = np.zeros((cantidad_ejemplos, 1))
    t = np.zeros(cantidad_ejemplos, dtype="uint8") 
    suma = np.arange(0,cantidad_ejemplos,1)
    z = np.arange(0,cantidad_ejemplos,1)

    t = AMPLITUD_ALEATORIEDAD * (np.cos(angulos)+suma)
    x = t + np.random.uniform(-1,1,cantidad_ejemplos)
    
    plt.plot(z, x, t)
    plt.show()

generar_datos_continuos(300,1)
