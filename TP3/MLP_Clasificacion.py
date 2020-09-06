import numpy as np
import matplotlib.pyplot as plt

#Datos nuevos
#Se propone funciones sigmoidales para notar superposicion de las clases
def generar_nuevos_datos(cantidad_ejemplos, cantidad_clases):
    x = np.zeros((cantidad_ejemplos,2))
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  
    count = 0
    sigma = [0.2,0.3,0.4]

    for i in range(cantidad_ejemplos):
        x[i][0] = np.random.uniform(-1,1)
        if i >= (int)(cantidad_ejemplos/cantidad_clases)*(count+1):
            count += 1 
        t[i] = count
        
        x[i][1] = 1/(np.sqrt(2*np.pi)*sigma[count])*np.exp(-0.5*np.power((x[i][0]/sigma[count]),2))    

    # plt.scatter(x[:,0], x[:,1], c=t)
    # plt.show()
    return x, t

#Datos continuos
def generar_datos_continuos(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1
    n = int(cantidad_ejemplos / cantidad_clases)

    angulos = np.linspace(1 * np.pi * FACTOR_ANGULO, (1 + 1) * np.pi * FACTOR_ANGULO, n)
    x = np.zeros((cantidad_ejemplos,1), dtype="uint8")
    t = np.zeros(cantidad_ejemplos, dtype="uint8") 
    suma = np.arange(0,cantidad_ejemplos,1)
    z = np.arange(0,cantidad_ejemplos,1)

    t = AMPLITUD_ALEATORIEDAD * (np.cos(angulos)+suma)
    x = t + np.random.uniform(-1,1,cantidad_ejemplos)
    x=np.reshape(cantidad_ejemplos,1)
    #plt.plot(z, x, t)
    #plt.show()
    return x, t

#Datos originales
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

def inicializar_pesos(n_entrada, n_capa_2, n_capa_3, REGRESION=False):
    randomgen = np.random.default_rng()
    #Para clasificacion
    if REGRESION==False:
        w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
        b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))
        w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
        b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))
    #Para regresion
    else:
        w1 = 0.1 * randomgen.standard_normal((n_entrada,n_capa_2))
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

def regresion(x, t, pesos, learning_rate, epochs, tolerancia, paso=0, flag=False):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0)
    loss_list = list()
    epochs_list = list()
    lossRegresion = list()
    
    cont=0
    for i in range(epochs):
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]
        
        mse = (np.square(t - x)).mean(axis=None )

        if i%1000 == 0:
            #    print("Loss epoch", i, ":", loss)
            loss_list.append(mse)
            epochs_list.append(i)
            
        if flag and i%paso==0:
            lossRegresion.append(mse)

        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]
 
        dL_dy = 2*(t-y)/m  # ... excepto para la clase correcta
        dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2
        
        dL_dh = dL_dy.dot(w2)
        #Agregar la funcion sigmoide
        sigm=(1/(1 + np.exp(-x)))
        dL_dz = dL_dh * sigm * (1-sigm)      # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
        
        dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1
        w1 = w1 -learning_rate * dL_dw1 #Ajuste de pesos
        b1 = b1 -learning_rate * dL_db1
        w2 = w2 -learning_rate * dL_dw2
        b2 = b2 -learning_rate * dL_db2
        pesos["w1"] = w1 #Extraccion de pesos como variables locales
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2   

    return {"y": y, "pesos": pesos, "lossT": lossRegresion}

def validation(x, t, pesos, learning_rate, epochs, tolerancia, paso, lossTrain):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0)
    loss_list = list()
    epochs_list = list()
    lossValidation = list()

    cont=0
    for i in range(epochs):
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]
        
        #clasificacion
        
        exp_scores = np.exp(y)
        sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)
        p = exp_scores / sum_exp_scores
        
        loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))


        if i%paso == 0:
            lossValidation.append(loss)
            #Parada temprana para validacion -> valor del error absoluto
            valor = lossTrain[cont]-lossValidation[cont]
            if abs(valor)>tolerancia and i > (int)(0.1*epochs): #inicialmente pueden tener un desfasaje alto
                break
            cont = cont+1
        
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]
 
        ##ACA DEFINO EL FLAG
        flag = False
        
        if flag == False:
 
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
            w1 = w1 -learning_rate * dL_dw1 #Ajuste de pesos
            b1 = b1 -learning_rate * dL_db1
            w2 = w2 -learning_rate * dL_dw2
            b2 = b2 -learning_rate * dL_db2
            pesos["w1"] = w1 #Extraccion de pesos como variables locales
            pesos["b1"] = b1
            pesos["w2"] = w2
            pesos["b2"] = b2   
    
        else:
            
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
            w1 =w1 -learning_rate * dL_dw1 #Ajuste de pesos
            b1 =b1 -learning_rate * dL_db1
            w2 =w2 -learning_rate * dL_dw2
            b2 =b2 -learning_rate * dL_db2
            pesos["w1"] = w1 #Extraccion de pesos como variables locales
            pesos["b1"] = b1
            pesos["w2"] = w2
            pesos["b2"] = b2
            
    #len(lossTrain) es constante, mientras que len(lossValidation) varia debido a la tolerancia impuesta en la parada temprana
    #Lo que hacemos es eliminar los datos de la lista lossTrain -> si quisieramos podemos hacer un .copy() para duplicar la lista 
    #Por ahora no hace falta ese paso, porque solo necesitamos esta lista para graficar
    
    tamano = len(lossValidation)
    del lossTrain[tamano:len(lossTrain)] #A partir de tamano hasta el ultimo elemento de la lista lossValidation se descartan
    
    plt.plot(np.arange(0,tamano*paso,paso), lossValidation)   #np.arange(valor inicial, valor final, paso)
    plt.plot(np.arange(0,tamano*paso,paso), lossTrain)
    plt.legend(["lossValidation", "lossTrain"])
    plt.show()

def test(x, t, pesos, REGRESION=False):
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    y = resultados_feed_forward["y"]
    h = resultados_feed_forward["h"]
    z = resultados_feed_forward["z"]
    if REGRESION==True:
        performance=(np.mean(np.square(t - x)))
        print("Eficiencia en test: ", performance)
    else:
        predicted_class = np.argmax(y, axis=1)
        performance=(np.mean(predicted_class == t))
        print("Eficiencia en test: ", performance)

def k_fold(K, pesos, LEARNING_RATE, EPOCHS, numero_ejemplos, numero_clases, REGRESION=False):
    Lrate_list = np.linspace(0.1,LEARNING_RATE,K)
    epochs_list = np.arange(EPOCHS,EPOCHS+1000*K,1000,dtype=int)
    
    p_learning_rate = {"performance": list(), "value": Lrate_list} #performance learning rate
    p_epochs = {"performance": list(), "value": epochs_list}
    
    paso=200
    tol=0.025

    if REGRESION==True:
        for i in range(K): #quedan fijos los epochs
            x, t = generar_datos_continuos(numero_ejemplos, numero_clases)
            
            ret = regresion(x, t, pesos, Lrate_list[i], EPOCHS, tol)
            
            y = ret["y"]
            pesos = ret["pesos"]
            
            p_learning_rate["performance"].append(np.mean(np.square(t - x)))
        
        p = p_learning_rate["performance"]
        index = p.index(max(p)) #la maxima performance
        LEARNING_RATE = p_learning_rate["value"][index] #best learning rate
        #print("Best learning rate:", LEARNING_RATE)
        #print(p_learning_rate["performance"])
        
        for i in range(K): #quedan fijo LEARNING RATE
            x, t = generar_datos_continuos(numero_ejemplos, numero_clases)
        
            ret = regresion(x, t, pesos, LEARNING_RATE, epochs_list[i], tol)
            y = ret["y"]
            pesos = ret["pesos"]
        
            p_epochs["performance"].append(np.mean(np.square(t - x)))
        
        p = p_epochs["performance"]
        index = p.index(max(p)) #la maxima performance
        EPOCHS = p_epochs["value"][index] #best learning rate
        #print("Best epochs value:", EPOCHS)
        #print(p_epochs["performance"])

    else:
        for i in range(K): #quedan fijos los epochs
            x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
        
            ret = train(x, t, pesos, Lrate_list[i], EPOCHS)
            y = ret["y"]
            pesos = ret["pesos"]
            
            predicted_class = np.argmax(y, axis=1)
            p_learning_rate["performance"].append(np.mean(predicted_class == t))
        
        
        p = p_learning_rate["performance"]
        index = p.index(max(p)) #la maxima performance
        LEARNING_RATE = p_learning_rate["value"][index] #best learning rate
        #print("Best learning rate:", LEARNING_RATE)
        #print(p_learning_rate["performance"])
        
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
        #print("Best epochs value:", EPOCHS)
        #print(p_epochs["performance"])
        
    return LEARNING_RATE, EPOCHS

def iniciar(set_datos, numero_clases, numero_ejemplos, graficar_datos=False):
    if set_datos == 1:
        print("Set de datos original:")
        x, t = generar_datos_clasificacion(numero_ejemplos, numero_clases)
        x2, t2 = generar_datos_clasificacion((int)(numero_ejemplos/5), numero_clases) #datos para validation
        x3, t3 = generar_datos_clasificacion((int)(numero_ejemplos/10), numero_clases) #datos para el test
    elif set_datos == 2:
        print("Nuevo set de datos:")
        x, t = generar_nuevos_datos(numero_ejemplos, numero_clases)
        x2, t2 = generar_nuevos_datos((int)(numero_ejemplos/5), numero_clases) #datos para validation
        x3, t3 = generar_nuevos_datos((int)(numero_ejemplos/10), numero_clases) #datos para el test
    else:
        x, t = generar_datos_continuos(numero_ejemplos, numero_clases)
        x2, t2 = generar_datos_continuos((int)(numero_ejemplos/5), numero_clases) #datos para validation
        x3, t3 = generar_datos_continuos((int)(numero_ejemplos/10), numero_clases) #datos para el test

    if (set_datos==1 or set_datos==2):

        NEURONAS_CAPA_OCULTA = 100
        NEURONAS_ENTRADA = 2
        pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases, REGRESION=False)
    
        LEARNING_RATE=1
        EPOCHS=1000
        
        # tt = train(x, t, pesos, LEARNING_RATE, EPOCHS)
        # pesos = tt["pesos"] #es necesario entrenar antes de k_fold?

        LEARNING_RATE, EPOCHS = k_fold(10, pesos, LEARNING_RATE, EPOCHS, numero_ejemplos, numero_clases, REGRESION=False) #K=10 #ej3
        paso = 200
        tol = 0.025
    
        training = train(x, t, pesos, LEARNING_RATE, EPOCHS, paso, True)
        lossTraining = training["lossT"]

        y= training["y"]
        print("Eficiencia en training", np.mean(np.argmax(y, axis=1) == t)) #ej 2a

        #Invocar funcion para graficar
        validation(x2, t2, pesos, LEARNING_RATE, EPOCHS, tol, paso, lossTraining) 
    
        #Test
        test(x3, t3, pesos) #ej 2b

    else:
        #Consideramos que set_datos=3 solo es para regresion
        NEURONAS_CAPA_OCULTA = 300
        NEURONAS_ENTRADA = 1
        pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=1,REGRESION=True)
        
        LEARNING_RATE=1
        EPOCHS=1000
        
        LEARNING_RATE, EPOCHS = k_fold(10, pesos, LEARNING_RATE, EPOCHS, numero_ejemplos, numero_clases, REGRESION=True) #K=10 #ej3
        
        paso = 200
        tol = 0.025
    
        training = regresion(x, t, pesos, LEARNING_RATE, EPOCHS, tol, paso, True)
        
        lossTraining = training["lossT"]

        flagPrueba = True
        #Para clasificacion
        if flagPrueba == True:
            y= training["y"]
            print("Eficiencia en training", np.mean(np.argmax(y, axis=1) == t)) #ej 2a
        else:
            print("Para regresion FALTAAAAAAAAAA")
            
        #Test
        test(x3, t3, pesos) #ej 2b


    if graficar_datos:
        plt.scatter(x[:, 0], x[:, 1], c=t)
        plt.show()

        plt.scatter(x2[:, 0], x2[:, 1], c=t2)
        plt.show()

        plt.scatter(x3[:, 0], x3[:, 1], c=t3)
        plt.show()
    
#iniciar(1, numero_clases=3, numero_ejemplos=300, graficar_datos=False) #set de datos originales 
#iniciar(2, numero_clases=3, numero_ejemplos=300, graficar_datos=False) #Nuevo set de datos #ej 4

iniciar(3, numero_clases=1, numero_ejemplos=300, graficar_datos=False) #Nuevo set de datos #ej 5
#FALTA AGREGAR LA REGRESION
