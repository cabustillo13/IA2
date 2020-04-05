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
#4) El pickung comienza y termina en una bahia de carga, de posic fija
#5) El "costo" del picking es proporcional a la distancia recorrida
#6) Se debe generar un conjunto de ordenes ficticias, simulando ordenes
#    reales que el almacen tendria que satisfacer. Las ordenes deberian 
#    tener cantidades distintas de articulos e incluir distinto mix de
#    articulos (Stock Keeping Unit) cada una.

import TP1_ej3 as A_star
import random as rd

class Individuo():
    def __init__(self,genoma,fitness):
        self.genoma = genoma
        self.fitness = fitness

def create_picking_list(map):
    picking_list = []
    for i in range(rd.randint(5,10)): #lista de picking variable entre 5 y 10
        value = rd.randint(1,8*2*3) #valor a buscar aleatorio
        pos = A_star.search_position_of(value,map)
        if pos not in picking_list:
            picking_list.append(pos)
    print(picking_list) #3
    return picking_list

def genetic_algoritm():
    individuos = 30
    max_iter = 50
    poblacion = []
    pass

def main():
    print("Ejercicio 6")
    rd.seed(None)
    map = A_star.generate_map(3,3) #1) 2)
    picking_list = create_picking_list(map) #3)
    loading_station = (0,3) #4)
    print(map[picking_list[0]])

if __name__ == "__main__":
    main()