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

from Recocido_Simulado import simulated_annealing, search_position_of, generate_map
import random as rd
import numpy as np
from time import time

class Individuo():
    def __init__(self,genes=0,fitness=0):
        self.genes = genes
        self.fitness = fitness

def create_picking_list():
    picking_list = []
    all_PL = [] #lista de 5 listas picking
    print("Ordenes ficticias: ")
    for i in range(5): #5 listas de productos entre 4 y 7 productos c/u 
        for j in range(rd.randint(4,7)): #lista de picking variable entre 5 y 10
            value = rd.randint(1,48) #valor a buscar aleatorio
            if value not in picking_list:
                picking_list.append(value)
        all_PL.append(picking_list)
        print(picking_list)
        picking_list = []
    return all_PL #3

def generar_primer_poblacion(n_poblacion):
    poblacion = [] #poblacion es una lista de objetos Invidividuo
    #poblacion = np.zeros((n_poblacion,48),int)
    for i in range(n_poblacion):
        obj_list = []
        for j in range(48):
            producto = rd.randint(1,48) #incluye los extremos 1 y 48
            while producto in obj_list:
                producto = rd.randint(1,48)
            obj_list.append(producto)
        poblacion.append(Individuo(obj_list)) #pasa de ser una lista a objeto Individuo que contiene esa lista
    return poblacion

def calcular_fitness(lista,individuo): #individuo ordena nuevamente el mapa en esa disposicion
    return simulated_annealing(lista,individuo)

def seleccion(poblacion,n_poblacion,all_PL): #selecciono los k mejores.
    for individuo in poblacion: #para cada indivuduo de la poblacion calcula el fitness como la suma de los temple de todas las listas
        f_total = 0 #por individuo
        for lista in all_PL:
            fitness = calcular_fitness(lista,individuo.genes) 
            f_total += fitness
        individuo.fitness = f_total
        #print(individuo.fitness)
    k = int(0.25*n_poblacion) #nro de seleccionados
    seleccionados = []
    i = 0
    for m in range(k):
        seleccionados.append(Individuo())
    while i!=k:
        f_min = poblacion[0].fitness #semilla del primer fitness
        for individuo in poblacion:
            if individuo.fitness < f_min and individuo not in seleccionados:
                f_min = individuo.fitness
                seleccionados[i] = individuo
        i += 1
    return seleccionados

def crossover(seleccionados): #cruce de orden
    for i in range(0,len(seleccionados),2): #los seleccionados pares
        corte1 = rd.randint(1,46) #el 1 y 46 aseguran q haya al menos un nro a cada lado
        corte2 = rd.randint(1,46)
        listaA = seleccionados[i].genes #para tener un nombre +corto
        listaB = seleccionados[i+1].genes
        while cruce2 == cruce1: #por si se llegara a repetir
            cruce2 = rd.randint(1,46)
        if cruce1 > cruce2: #para mantener que cruce 1 sea menor que cruce2
            aux = cruce1
            cruce1 = cruce2
            cruce2 = aux
        print("cruce1:",cruce1,"cruce2:",cruce2)
        print("ListaA:\n",listaA,"ListaB:\n",listaB)
        newA = []
        newB = []
        for m in range(len(listaA)):
            newA.append(0)
            newB.append(0)
        for i in range(corte1,corte2+1):
            newA[i] = listaB[i]
            newB[i] = listaA[i]

        it = corte2+1 #sirve para iterar ---LISTA A
        actual = it #donde se va a guardar
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

        it = corte2+1 #sirve para iterar ---LISTA A
        actual = it #donde se va a guardar
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
        print("ListaA:\n",listaA,"ListaB:\n",listaB)
        seleccionados[i].genes = listaA
        seleccionados[i+1].genes = listaB
    return seleccionados

def evolucion(seleccionados):
    for i in range(len(seleccionados)):
        probab_de_mutar = rd.random()
        if probab_de_mutar < 0.1:
            gen1 = rd.randint(0,47)
            gen2 = rd.randint(0,47)
            while gen1 == gen2: #por si se llegara a repetir
                gen2 = rd.randint(0,47)
            #intercambian dos genes
            aux = seleccionados[i].genes[gen1]
            seleccionados[i].genes[gen1] = seleccionados[i].genes[gen2]
            seleccionados[i].genes[gen2] = aux
    return seleccionados

def genetic_algoritm():
    all_PL = create_picking_list() #3)
    n_poblacion = 8 #len(all_PL)) <-- <-- <-- <-- <-- <-- <-- <--
    poblacion = generar_primer_poblacion(n_poblacion) 
    
    generacion = 0
    max_generacion = 1

    while(generacion<max_generacion):
        seleccionados = seleccion(poblacion,n_poblacion,all_PL)
        seleccionados = crossover(seleccionados)
        seleccionados = evolucion(seleccionados)
        generacion += 1

def main():
    print("Ejercicio 6")
    rd.seed(None)
    #loading_station = (0,0) #4)
    t1 = time()
    genetic_algoritm()
    t2 = time()
    print("Tiempo de ejecucion:",round(t2-t1,2),"segundos")

if __name__ == "__main__":
    main()