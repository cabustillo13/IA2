import numpy as np
import evaluacionRecursion
import grafica

def main():
    k=10 #Cantidad de tareas
    tareas=np.zeros(k,int)
    
    d=[40,20,25,10,25,20,50,30,10,15] #d= Lista de duracion de cada tarea
    deadline = 125 
    
    #Esto lo hacemos para que en la evaluacionRecursion salte el principio de analisis de condiciones y de pier para empezar a avanzar en el tiempo
    #si lo dejaramos como una lista de ceros no se empezaria a mover y directamente marcaria que no se puede determinar una solucion
    for i in range(0,k):
        tareas[i]=-1
        
    pos_inicial=0
    #En python, todas las variables son punteros a objetos, que son manejados implicitamente
    #Lo que si hacemos es considerar el dato mutable
    rec= evaluacionRecursion.recursion(pos_inicial,tareas,d,deadline)
    
    if (rec == True):
        #Resultados finales de la solucion
        print("Las operaciones a realizar y su respectivo instante de inicializacion")
        print("Mecanizar Pieza 1:          en t0 = ", tareas[0])
        print("Pintado 1 de la Pieza 1:    en t1 = ", tareas[1])
        print("Pintado 2 de la Pieza 1:    en t2 = ", tareas[2])
        print("Pulir Pieza 1:              en t3 = ", tareas[3])
        print("Mecanizar Pieza 2:          en t4 = ", tareas[4])
        print("Pintura 1 de la Pieza 2:    en t5 = ", tareas[5])
        print("Recocido de la Pieza 3:     en t6 = ", tareas[6])
        print("Mecanizar Pieza 3:          en t7 = ", tareas[7])
        print("Pulir Pieza 3:              en t8 = ", tareas[8])
        print("Ensamblar 3 piezas:         en t9 = ", tareas[9])
        
        grafica.graficar(tareas,d,deadline)
    else:
        print("No se ha encontrado una solucion con ese deadline")
    
if __name__ == "__main__":
    main()
    
