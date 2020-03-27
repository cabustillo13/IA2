#Recocido Simulado
#Carlos Bustillo, Legajo 11586, Mecatronica

##RESUMEN
#Hace referencia a un proceso termodinamico, donde en el temple el material se calienta mas alla de su
#T de recristalizacion y despues se deja enfriar de manera paulativa
#La variable de T va a definir el tipo de busqueda.

##ALGORITMO
#Entradas: Tinicial, Tfinal, c (cte de enfriamiento), n (# de mov. hasta alcanzar el equilibrio termico)
#           funcion muestrear: solucion aleatoria
#           funcion mover: da una solucion vecina
#           funcion energia: da el valor de la energia o costo
#Salida: solucion que minimiza la energia

##DESARROLLO
import random as rand
import matplotlib.pyplot as plt
import numpy as np
import math as magic

#inicializacion 
##solucion aleatoria inicial
x = rand.randint(0,50) #elegi un valor entero en un rango prestablecido
##valor obtenido de la funcion muestrear
u = magic.sin(x/10) #math.magic te permite tratar las clases como si fueran funciones

##Ti: Temperatura inicial
Ti = 1000
##cte: constante de enfriamiento
cte = 0.90
##Con esta variable vamos a obtener el # de mov. hasta alcanzar el equilibrio termico
contador = 0
##Van a servir para graficarla fig 1
xpoints = []
ypoints = []
##Van a servir para graficarla fig 2
energia = []
prob = []

while Ti >= 0.0001:
    contador = contador + 1
    ##Se perturba la solucion, pero se trata de que la solucion inicial no salga del rango de x
    z = rand.randint(0,50)

    u = magic.sin(x/10)
    aux = magic.sin(z/10)
    if aux < u:
        #Se cambia el valor de X -> disminuye la T
        x = z
        Ti = Ti * cte
        xpoints.append(x)
        ypoints.append(aux)

    else:
        #NOTA: Lo importante de este metodo es que si la solucion NO es menor, no la desechamos
        #Se busca un numero aleatorio con distribucion uniforme ( entre 0 y 1)
        random_number = rand.uniform(0,1)
        #Se determina el delta(T) a partir de la formula de Bolztman -> cambio: diferencias de energia
        #K= cte de Bolztman K
        cambio = (aux - u)/ (1*Ti) #Para la simulacion K=1
        #p: Probabilidad de Bolztman
        p = 0
        p = magic.exp(-cambio)
    
        if random_number < p:
            #Se cambia el valor de X -> disminuye la T
            x = z
            Ti = cte*Ti
            xpoints.append(x)
            ypoints.append(aux)
            energia.append(cambio)
            prob.append(p)

print("Valor de Tf: ",x)
print("Valor de la funcion muestrear para Tf: ",magic.sin(x/10))
print("Cantidad de movimientos: ", contador)

##NOTA: Como se toma valores aleatorias, las graficas al principio varian
plt.plot(xpoints, color = "C3")
plt.grid(True)
plt.xlabel('Valores de evolucion de la solucion')
plt.ylabel('Valores de funcion muestreo')
plt.title('Grafica 1')
plt.show()

plt.plot(energia, prob, color = "C3")
plt.grid(True)
plt.xlabel('Cambio de Energia')
plt.ylabel('Probabilidad de Bolztman')
plt.title('Grafica 2')
plt.show()


##BIBLIOGRAFIA
#https://es.coursera.org/lecture/resolucion-busqueda/algoritmo-recocido-simulado-sa-LfzCo
