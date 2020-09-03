#PARA PYTHON3
import TP3_ej1

import numpy as np
import matplotlib.pyplot as plt

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)
def generar_datos_clasificacion(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1
    n = int(cantidad_ejemplos / cantidad_clases)
    x = np.zeros((cantidad_ejemplos, 2))
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  
    randomgen = np.random.default_rng()

    for clase in range(cantidad_clases):
        radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(size=n)
        angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n)
        indices = range(clase * n, (clase + 1) * n)
        x1 = radios * np.sin(angulos)
        x2 = radios * np.cos(angulos)
        x[indices] = np.c_[x1, x2]
        t[indices] = clase

    return x, t

def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    randomgen = np.random.default_rng()

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

def ejecutar_adelante(x, pesos):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]
    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    h = np.maximum(0, z)
    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]
    return {"z": z, "h": h, "y": y}

def clasificar(x, pesos):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis=1)

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores[:, 0]

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, pesos, learning_rate, epochs):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0) 
    loss_list = list()
    epochs_list = list()

    for i in range(epochs):
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]

        exp_scores = np.exp(y)
        sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)
        p = exp_scores / sum_exp_scores
        loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))
        
        if i %1000 == 0:
            print("Loss epoch", i, ":", loss)
            loss_list.append(loss)
            epochs_list.append(i)

        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dy = p                # Para todas las salidas, L' = p (la probabilidad)...
        dL_dy[range(m), t] -= 1  # ... excepto para la clase correcta
        dL_dy /= m

        dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

        dL_dh = dL_dy.dot(w2.T)
        
        dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
        dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)

        dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1

        w1 += -learning_rate * dL_dw1 #Ajuste de pesos
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        pesos["w1"] = w1 #Extraccion de pesos como variables locales
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2

    predicted_class = np.argmax(y, axis=1)
    print('Precision de entrenamiento: %.2f' % (np.mean(predicted_class == t)))
    
    fig, ax = plt.subplots()
    ax.plot(epochs_list, loss_list)
    ax.set(xlabel='Epochs', ylabel='Loss')
    ax.grid()
    plt.show()

def iniciar(numero_clases, numero_ejemplos, graficar_datos):
    x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
    x2, t2 = generar_datos_clasificacion((int)(numero_ejemplos/10), numero_clases) #nuevos datos para test

    if graficar_datos:
        plt.scatter(x[:, 0], x[:, 1], c=t)
        plt.show()

        plt.scatter(x2[:, 0], x2[:, 1], c=t2)
        plt.show()

    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    LEARNING_RATE=1
    EPOCHS=10000
    #train(x, t, pesos, LEARNING_RATE, EPOCHS)
    train(x2,t2,pesos,LEARNING_RATE,EPOCHS)

iniciar(numero_clases=3, numero_ejemplos=300, graficar_datos=True)

#############
## TP3_ej1 ##
#############
#Train
# x1, t1, y1 = iniciar(numero_clases=3, numero_ejemplos=300, graficar_datos=True)

# #Test
# x2 = np.zeros((300, 2))
# pesos2 = inicializar_pesos(2,100,3)
# clasificar(x2,pesos2)

#Accuracy

