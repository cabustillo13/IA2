#Ejercicio6:
#Consigna: implementar un AG para resolver el problema de optimizar
#la ubicacion de los productos del almacen, de manera de optimizar
#el picking de los mismos. Cosidere que:
#1) El layout del almacen esta fijo, solo debe determinarse el lugar 
#    donde se coloca cada producto
#2) Cada producto tiene una ubicacion en el almacen, que define unas
#    coordenadas, un pasillo y una estanteria
#3) Cada orden incluye un conjunto de productos que deben ser 
#    despachados en su totalidad
#4) El picking comienza y termina en una bahia de carga, de posic fija
#5) El "costo" del picking es proporcional a la distancia recorrida
#6) Se debe generar un conjunto de ordenes ficticias, simulando ordenes
#    reales que el almacen tendria que satisfacer. Las ordenes deberian 
#    tener cantidades distintas de articulos e incluir distinto mix de
#    articulos (Stock Keeping Unit) cada una.

#Individuo: almacen con cierta disposicion de productos
#Genes: disposicion de productos (48)
#Fitness: distancia de recocido simulado

from TP1_ej5 import simulated_annealing
import random as rd
import numpy as np
from time import time

class Individuo():
    def __init__(self,genes=[],fitness=0):
        self.genes = genes
        self.fitness = fitness

def create_picking_list():
    picking_list = []
    all_PL = []                          
    print("Ordenes ficticias: ")
    for i in range(5):                   #lista de 5 listas de picking 
        for j in range(rd.randint(4,8)): #lista de picking variable entre 4 y 8
            value = rd.randint(1,48)     #valor a buscar aleatorio
            if value not in picking_list:
                picking_list.append(value)
        all_PL.append(picking_list)
        print(picking_list)
        picking_list = []
    return all_PL 

def generar_primer_poblacion(n_poblacion):
    poblacion = []                      #poblacion es una lista de objetos Invidividuo
    for i in range(n_poblacion):
        genes = []
        for j in range(48):
            producto = rd.randint(1,48) #incluye los extremos 1 y 48
            while producto in genes:
                producto = rd.randint(1,48)
            genes.append(producto)
        poblacion.append(Individuo(genes,0)) #pasa de ser una lista a objeto Individuo que contiene esa lista
    return poblacion

def calcular_fitness(lista,individuo): #individuo ordena nuevamente el mapa en esa disposicion
    return simulated_annealing(lista,individuo,False)

def seleccion(poblacion,n_poblacion,all_PL): #selecciono los k mejores (20%)
    for individuo in poblacion:              #para cada indivuduo de la poblacion calcula el fitness como la suma de los temple de todas las listas
        f_total = 0                          #por individuo inicia en 0 y luego le sumamos lo acumulado
        for lista in all_PL:
            f_total += calcular_fitness(lista,individuo.genes) 
        individuo.fitness = f_total
    k = int(0.20*n_poblacion)                #nro de seleccionados
    if k%2 == 1:                             #para que los seleccionados sean pares
        k += 1
    seleccionados = []
    i = 0
    for m in range(k):
        seleccionados.append(Individuo())
    while i!=k:
        j = 0
        f_min = poblacion[j].fitness         #valor semilla
        while poblacion[j] in seleccionados: #corrige cuando el 1er elemento fue seleccionado->ya no sirve de semilla
            j += 1
            f_min = poblacion[j].fitness
            
        for individuo in poblacion:
            if individuo.fitness <= f_min and individuo not in seleccionados:
                f_min = individuo.fitness
                seleccionados[i] = individuo
        i += 1
    return seleccionados

def crossover(seleccionados):               #Crossover por cruce de orden
    for i in range(0,len(seleccionados),2): #los seleccionados pares
        corte1 = rd.randint(1,46)           #1 y 46 aseguran q haya al menos un nro a cada lado
        corte2 = rd.randint(1,46)           #recordar que el ultimo indice es 47
        listaA = seleccionados[i].genes     #para tener un nombre +corto
        listaB = seleccionados[i+1].genes
        while corte1 == corte2:             #por si se llegara a repetir
            corte2 = rd.randint(1,46)
        if corte1 > corte2:                 #para mantener que cruce 1 sea menor que cruce2
            corte1,corte2 = corte2,corte1
        newA = []
        newB = []
        for m in range(len(listaA)):
            newA.append(0)
            newB.append(0)

        for j in range(corte1,corte2+1):    #corte 2 inclusive, por esto el +1
            newA[j] = listaB[j]
            newB[j] = listaA[j]
        it = corte2+1                       #sirve para iterar ---LISTA A
        actual = it                         #donde se va a guardar
        while actual != corte1:
            if actual == len(listaA):
                actual = 0
            num = listaA[it]
            while num in newA:
                it += 1
                if it == len(listaA):
                    it = 0
                num = listaA[it]
            newA[actual] = num
            actual += 1

        it = corte2+1                       #sirve para iterar ---LISTA B
        actual = it                         #donde se va a guardar
        while actual != corte1:
            if actual == len(listaB):
                actual = 0
            num = listaB[it]
            while num in newB:
                it += 1
                if it == len(listaB):
                    it = 0
                num = listaB[it]
            newB[actual] = num
            actual += 1
        seleccionados[i].genes = newA
        seleccionados[i+1].genes = newB
    return seleccionados

def mutacion(seleccionados):
    for ind in seleccionados:
        probab_de_mutar = rd.random()
        if probab_de_mutar < 0.15:
            gen1 = rd.randint(0,47)
            gen2 = rd.randint(0,47)
            while gen1 == gen2:         #por si se llegara a repetir
                gen2 = rd.randint(0,47)
            ind.genes[gen1],ind.genes[gen2] = ind.genes[gen2],ind.genes[gen1]
    return seleccionados

def buscar_el_mejor(poblacion):
    fitness_min = poblacion[0].fitness #semilla de fitness
    mejor = poblacion[0]               #semilla de individuo
    for individuo in poblacion:
        if individuo.fitness < fitness_min:
            fitness_min = individuo.fitness
            mejor = individuo
    return mejor

def genetic_algoritm():
    all_PL = create_picking_list() #3)
    n_poblacion = 40 #<-- <-- <-- <-- <-- <--TAMAÑO DE POBLACION
    poblacion = generar_primer_poblacion(n_poblacion) 
    
    generacion = 0
    max_generacion = 50

    while(generacion<max_generacion): #criterio de parada: tiempo transcurrido
        print("----\nGeneracion",generacion+1,"\nSeleccion")
        seleccionados = seleccion(poblacion,n_poblacion,all_PL)
        print("Cross-over")
        seleccionados = crossover(seleccionados)
        print("Mutacion")
        seleccionados = mutacion(seleccionados)
        generacion += 1
    print("El mejor individuo de la poblacion es:")
    mejor=buscar_el_mejor(poblacion)
    print(mejor.genes)

def main():
    print("Ejercicio 6")
    rd.seed(None)
    t1 = time()
    genetic_algoritm()
    t2 = time()
    print("Tiempo de ejecucion:",round((t2-t1)/60,2),"minutos")

if __name__ == "__main__":
    main()