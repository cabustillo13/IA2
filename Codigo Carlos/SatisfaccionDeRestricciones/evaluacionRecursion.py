import switcher

#Aca aplicamos la recursion    
def recursion (posicion, tareas,d,deadline):
    
    #tareas = tareas[:] #Se crea una copia de la lista dentro de la misma funcion para no alterar los valores iniciales de tareas
    aceptado = False
    tareas[posicion]=0 

    while not (aceptado): #while (aceptado != True)
        cond = True
        #Analisis de condiciones -> las condiciones que no se cumplen hacen que cond = False
        if (tareas[0]>=0):
            if (posicion == 0):
                cond=switcher.case0(cond, tareas, d)
            elif (posicion == 1):
                cond=switcher.case1(cond, tareas, d)
            elif (posicion == 2):
                cond=switcher.case2(cond, tareas, d)
            elif (posicion == 3):
                cond=switcher.case3(cond, tareas, d)
            elif (posicion == 4):
                cond=switcher.case4(cond, tareas, d)
            elif (posicion == 5):
                cond=switcher.case5(cond, tareas, d)
            elif (posicion == 6):
                cond=switcher.case6(cond, tareas, d)
            elif (posicion == 7):
                cond=switcher.case7(cond, tareas, d)
            elif (posicion == 8):
                cond=switcher.case8(cond, tareas, d)
            elif (posicion == 9):
                cond=switcher.case9(cond, tareas, d, deadline)
            else:
                print("Ocurrio un error al evaluar las restricciones")
        
        #Si el ultimo nodo retorna cond=True significa que es valido
        if(cond == True and posicion==9):
            return True
        #Si el nodo evaluado no es el ultimo, debe avanzar al proximo nodo y esperar la validacion
        elif(cond == True and posicion<9):
            posicion=posicion + 1
            aceptado = recursion(posicion, tareas,d,deadline)
            
            #Si el nodo es aceptado aca debe terminar el algoritmo
            if (aceptado): #if aceptado == True
                return True
                break
            #si el nodo no es aceptado -> es no valido y se evalua las siguientes condiciones
            else:
                cond = False
        #Si el nodo no es valido y no ha alcanzado el deadline -> se prueba un siguiente valor de tiempo
        #En este caso evaluamos en intervalo de 5 minutos
        if (cond == False and (tareas[posicion] + d[posicion]) < deadline):
            tareas[posicion] = tareas[posicion] + 5
        #Si el nodo no es valido y ya alcanzamos el deadline (ya recorrimos todo el dominio) -> retorna false y hace el backtraking
        if (cond == False and (tareas[posicion] + d[posicion]) >= deadline):
            return False
            break
        
    return False
