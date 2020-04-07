#Forma de implementacion de un switch en python sin diccionario
def case0(cond, tareas, d):
    if not(tareas[0] + d[0] <= tareas[1] or tareas[1]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[2] or tareas[2]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[4] or tareas[4] + d[4] <= tareas[0] or tareas[4]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[7] or tareas[7] + d[7] <= tareas[0] or tareas[7]<0):
        cond = False    
    return cond

def case1(cond, tareas, d):
    if not(tareas[1] + d[1] <= tareas[3] or tareas[3]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[1] or tareas[0]<0):
        cond = False
    if not(tareas[1] + d[1] <= tareas[2] or tareas[2] + d[2] <= tareas[1] or tareas[2]<0):
        cond = False
    if not(tareas[1] + d[1] <= tareas[5] or tareas[5] + d[5] <= tareas[1] or tareas[5]<0):
        cond = False
    return cond
    
def case2(cond, tareas, d):
    if not(tareas[2] + d[2] <= tareas[3] or tareas[3]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[2] or tareas[0]<0):
        cond = False
    if not(tareas[1] + d[1] <= tareas[2] or tareas[2] + d[2] <= tareas[1] or tareas[1]<0):
        cond = False
    if not(tareas[2] + d[2] <= tareas[5] or tareas[5] + d[5] <= tareas[2] or tareas[5]<0):
        cond = False
    return cond

def case3(cond, tareas, d):    
    if not(tareas[3] + d[3] <= tareas[9] or tareas[9]<0):
        cond = False
    if not(tareas[1] + d[1] <= tareas[3] or tareas[1]<0):
        cond = False
    if not(tareas[2] + d[2] <= tareas[3] or tareas[2]<0):
        cond = False
    if not(tareas[3] + d[3] <= tareas[8] or tareas[8] + d[8] <= tareas[3] or tareas[8]<0):
        cond = False
    return cond

def case4(cond, tareas, d):
    if not(tareas[4] + d[4] <= tareas[5] or tareas[5]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[4] or tareas[4] + d[4] <= tareas[0] or tareas[0]<0):
        cond = False
    if not(tareas[4] + d[4] <= tareas[7] or tareas[7] + d[7] <= tareas[4] or tareas[7]<0):
        cond = False
    return cond

def case5(cond, tareas, d):
    if not(tareas[4] + d[4] <= tareas[5] or tareas[4]<0):
        cond = False
    if not(tareas[5] + d[5] <= tareas[9] or tareas[9]<0):
        cond = False
    if not(tareas[1] + d[1] <= tareas[5] or tareas[5] + d[5] <= tareas[1] or tareas[1]<0):
        cond = False
    if not(tareas[2] + d[2] <= tareas[5] or tareas[5] + d[5] <= tareas[2] or tareas[2]<0):
        cond = False
    return cond

def case6(cond, tareas, d):
    if not(tareas[6] + d[6] <= tareas[7] or tareas[7]<0):
        cond = False
    return cond

def case7(cond, tareas, d):
    if not(tareas[6] + d[6] <= tareas[7] or tareas[6]<0):
        cond = False
    if not(tareas[7] + d[7] <= tareas[8] or tareas[8]<0):
        cond = False
    if not(tareas[4] + d[4] <= tareas[7] or tareas[7] + d[7] <= tareas[4] or tareas[4]<0):
        cond = False
    if not(tareas[0] + d[0] <= tareas[7] or tareas[7] + d[7] <= tareas[0] or tareas[0]<0):
        cond = False
    return cond

def case8(cond, tareas, d):
    if not(tareas[7] + d[7] <= tareas[8] or tareas[7]<0):
        cond = False
    if not(tareas[8] + d[8] <= tareas[9] or tareas[9]<0):
        cond = False
    if not(tareas[3] + d[3] <= tareas[8] or tareas[8] + d[8] <= tareas[3] or tareas[3]<0):
        cond = False
    return cond

def case9(cond, tareas, d, deadline):
    if not(tareas[9] <= deadline):
        cond = False
    if not(tareas[8] + d[8] <= tareas[9] or tareas[8]<0):
        cond = False
    if not(tareas[3] + d[3] <= tareas[9] or tareas[3]<0):
        cond = False
    if not(tareas[5] + d[5] <= tareas[9] or tareas[5]<0):
        cond = False
    return cond


 
