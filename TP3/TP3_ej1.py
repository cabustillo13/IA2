import matplotlib.pyplot as plt

#Funcion de activacion
def funcionActivacion(valor,opcion):
    #Asociador Lineal
    if (opcion == 0):
        return(valor)
    #Heavyside
    elif (opcion == 1):
        if (valor >= 0):
            return(1)
        else:
            return(0)
    
#Calcular la salida de cada neurona
def salidaReal(wji,wkj,x,y,output):
    
    #Para la capa oculta
    for j in range(0,NEURONAS_CAPA_OCULTA):
        inputY = 0
        for i in range(0,NEURONAS_ENTRADA):
            inputY += wji[i][j]*x[i]
        #El sesgo -> se puede considerar un peso sinaptico adicional con un valor de entrada fijo en -1
        inputY -= wji[NEURONAS_ENTRADA-1][j]
        #Valor de salida de la neurona j
        y[j] =funcionActivacion(inputY,0)
        
    #Para la capa de salida
    for k in range(0, NEURONAS_SALIDA):
        inputZ = 0
        for j in range(0, NEURONAS_CAPA_OCULTA):
            inputZ += wkj[j][k] * y[j]
        # Sesgo de las neuronas de la capa de salida
        inputZ -= wkj[NEURONAS_CAPA_OCULTA - 1][k]
        # inputZ -= 1
        # Valor de salidad de la neurona k
        output[k] = funcionActivacion(inputZ,0)    
        
        return x,y,z    

#Calculo de Loss en Regression
def lossRegresion(output,t):
    loss = list()
    
    for i in range(len(output)):
        loss.append((output[i] - t[i])**2)
        
    plt.plot(loss)
    plt.show()
    

