import numpy as np
import matplotlib.pyplot as plt

##########
#Se propone funciones sigmoidales para notar superposicion de las clases
def generar_nuevos_datos(cantidad_ejemplos, cantidad_clases):
    x = np.zeros((cantidad_ejemplos, 2))
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  

    k = [-0.4, 0, 0.4]  #corrimiento horizontal de las curvas
    output_range = [] #lista dinamica desde 0 a la cantidad de clases -1
    r1 = 0 
    while(r1 < cantidad_clases): 
        output_range.append(r1) 
        r1 += 1

    count = 0
    for i in range(cantidad_ejemplos):
        x[i][0] = np.random.uniform(-1,1)        #x
        #t[i] = np.random.choice(output_range)           
        if i >= (int)(cantidad_ejemplos/cantidad_clases)*(count+1):
            count += 1 
        t[i] = count

        #ReLU nos va a servir para punto 6)
        c2 = k[t[i]]
        c1 = 10    
        x[i][1] = 1/(1+np.exp(-c1*(x[i][0]-c2)))  #y

    return x, t
##########

##########
#Calculo de Loss en Regression MSE -> Nos vas a servir para el punto 5.a) 
def lossRegresion(output,t):
    loss = list()
    
    for i in range(len(output)):
        loss.append((output[i] - t[i])**2)
        
    plt.plot(loss)
    plt.show()
#############

#Generar nuevos tipos de datos -> En este caso usamos seno hiperbolico y coseno hiperbolico para que el conjunto nos aparezca como una linea recta donde aparece un solamiento de las clases
######### #Funcion sigmoidal
def generar_nuevos_datos(cantidad_ejemplos,cantidad_clases):
    
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
        x1 = radios * np.sinh(angulos)
        x2 = radios * np.cosh(angulos)
        x[indices] = np.c_[x1, x2]
        t[indices] = clase
        
    plt.scatter(x[:, 0], x[:, 1], s=40, cmap=plt.cm.Spectral)
    plt.show()
    
    return x, t
###########

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
   return max_scores[:][0]


# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, pesos, learning_rate, epochs, paso=0, flag=False):
   # Cantidad de filas (i.e. cantidad de ejemplos)
   m = np.size(x, 0)
   loss_list = list()
   epochs_list = list()
   lossTraining = list()
 
   for i in range(epochs):
       resultados_feed_forward = ejecutar_adelante(x, pesos)
       y = resultados_feed_forward["y"]
       h = resultados_feed_forward["h"]
       z = resultados_feed_forward["z"]
 
       exp_scores = np.exp(y)
       sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)
       p = exp_scores / sum_exp_scores
       loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))

       if i%1000 == 0:
        #    print("Loss epoch", i, ":", loss)
           loss_list.append(loss)
           epochs_list.append(i)
        
       if flag and i%paso==0:
            lossTraining.append(loss)
 
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
  
   # fig, ax = plt.subplots()
   # ax.plot(epochs_list, loss_list)
   # ax.set(xlabel='Epochs', ylabel='Loss')
   # ax.grid()
   # plt.show()
 
   return {"y": y, "pesos": pesos, "lossT": lossTraining}

def validation(x, t, pesos, learning_rate, epochs, tolerancia, paso, lossTrain):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0)
    loss_list = list()
    epochs_list = list()
    lossValidation = list()
   
    for i in range(epochs):
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]
 
        exp_scores = np.exp(y)
        sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)
        p = exp_scores / sum_exp_scores
       
        loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))
       
        if i%paso == 0:
            lossValidation.append(loss)
            if abs(lossTrain[i]-lossValidation[i]) > tolerancia:
                break
        
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]
 
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
    
    plt.plot(np.arange(0,epochs,paso), lossValidation)
    plt.plot(np.arange(0,epochs,paso), lossTrain)
    plt.legend(["LossValidation", "LossTraining"])
    plt.show()
    return lossValidation
#Aca entramos con los parametros ya optimizados


def k_fold(K, pesos, LEARNING_RATE, EPOCHS, numero_ejemplos, numero_clases):
   Lrate_list = np.linspace(0.1,LEARNING_RATE,K)
   epochs_list = np.arange(EPOCHS,EPOCHS+1000*K,1000,dtype=int)
 
   p_learning_rate = {"performance": list(), "value": Lrate_list} #performance learning rate
   p_epochs = {"performance": list(), "value": epochs_list}
  
   for i in range(K): #quedan fijos los epochs
       x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
 
       ret = train(x, t, pesos, Lrate_list[i], EPOCHS)
       y = ret["y"]
       pesos = ret["pesos"]
     
     #clasificar(x, pesos)
       predicted_class = np.argmax(y, axis=1)
       p_learning_rate["performance"].append(np.mean(predicted_class == t))
   
   
   p = p_learning_rate["performance"]
   index = p.index(max(p)) #la maxima performance
   LEARNING_RATE = p_learning_rate["value"][index] #best learning rate
   print("Best learning rate:", LEARNING_RATE)
   print(p_learning_rate["performance"])
 
   for i in range(K): #quedan fijo LEARNING RATE
       x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
 
       ret = train(x, t, pesos, LEARNING_RATE, epochs_list[i])
       y = ret["y"]
       pesos = ret["pesos"]
 
       predicted_class = np.argmax(y, axis=1)
       p_epochs["performance"].append(np.mean(predicted_class == t))
 
   p = p_epochs["performance"]
   index = p.index(max(p)) #la maxima performance
   EPOCHS = p_epochs["value"][index] #best learning rate
   print("Best epochs value:", EPOCHS)
   print(p_epochs["performance"])
   
   return LEARNING_RATE, EPOCHS



def iniciar(numero_clases, numero_ejemplos, graficar_datos):
   x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
   x2, t2 = generar_datos_clasificacion((int)(numero_ejemplos/10), numero_clases) #nuevos datos para test
   x3, t3 = generar_datos_clasificacion((int)(numero_ejemplos/5), numero_clases)
 
 
 
   if graficar_datos:
       plt.scatter(x[:, 0], x[:, 1], c=t)
       plt.show()
 
       plt.scatter(x2[:, 0], x2[:, 1], c=t2)
       plt.show()
 
   NEURONAS_CAPA_OCULTA = 100
   NEURONAS_ENTRADA = 2
   pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)
 
   LEARNING_RATE=1
   EPOCHS=1000
  
   LEARNING_RATE, EPOCHS = k_fold(10, pesos, LEARNING_RATE, EPOCHS, numero_ejemplos, numero_clases) #K=10
   paso = 200
   tol = 0.001 
   
   training = train(x, t, pesos, LEARNING_RATE, EPOCHS, paso, True)
   lossTraining = training["lossT"]

   lossValidation = validation(x2, t2, pesos, LEARNING_RATE, EPOCHS, tol, paso, lossTraining)
   

   

   # etapa_training = train(x, t, pesos, LEARNING_RATE, EPOCHS)
   # y = etapa_training["y"]
   # pesos = etapa_training["pesos"]
 
   # predicted_class = np.argmax(y, axis=1)
   # print('Precision de ENTRENAMIENTO: %.2f' % (np.mean(predicted_class == t)))
  
   # etapa_test = train(x2,t2,pesos,LEARNING_RATE,EPOCHS)
   # y2 = etapa_test["y"]
   # predicted_class = np.argmax(y2, axis=1)
   # print('Precision de TEST: %.2f' % (np.mean(predicted_class == t2)))
 
iniciar(numero_clases=3, numero_ejemplos=300, graficar_datos=False)

