from matplotlib import pyplot as plt

def graficar(tarea,d,deadline):
    #Cada maquina se representa con un color cuando una tarea la este utilizando
    #Torno: azul (b)
    #Equipo para pintar: rojo (r)
    #Pulidora: magenta (m)
    #Horno: amarillo(y)
    #Enamblaje: cyan(c)
    
    plt.hlines(y=0, xmin=tarea[0], xmax=d[0]+tarea[0], color ='b')
    plt.hlines(y=1, xmin=tarea[1], xmax=d[1]+tarea[1], color ='r')
    plt.hlines(y=2, xmin=tarea[2], xmax=d[2]+tarea[2], color ='r')
    plt.hlines(y=3, xmin=tarea[3], xmax=d[3]+tarea[3], color ='m')
    plt.hlines(y=4, xmin=tarea[4], xmax=d[4]+tarea[4], color ='b')
    plt.hlines(y=5, xmin=tarea[5], xmax=d[5]+tarea[5], color ='r')
    plt.hlines(y=6, xmin=tarea[6], xmax=d[6]+tarea[6], color ='y')
    plt.hlines(y=7, xmin=tarea[7], xmax=d[7]+tarea[7], color ='b')
    plt.hlines(y=8, xmin=tarea[8], xmax=d[8]+tarea[8], color ='m')
    plt.hlines(y=9, xmin=tarea[9], xmax=d[9]+tarea[9], color ='c')
    
    plt.title("Schedule")
    nombre= "deadline: " + str(deadline)
    plt.xlabel("Tiempo -> "+ nombre)
    plt.ylabel("Numero de tarea")
    plt.xlim(-0.1,deadline+0.1)
    plt.ylim(-0.1,9.5)
    plt.grid()
    plt.show()
