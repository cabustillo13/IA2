#Aplicación del algoritmo A* para la obtención de un camino óptimo dentro de un almacén
##Calculo de la trayecoria óptima de un brazo robótico de 6 grados de libertad
Para la trayectoria del brazo robótico se usa una función llamada _generate_map_, que admite un parametro (_tam_: cantidad de puntos por cada dirección), genera un mapa en 6D con esa cantidad de puntos.  Luego se generan los obstáculos, se definió arbitrariamente que el 10% del espacio articular esté ocupado por obstáculos. Se calcula como (cant. de punt**6/100), por eso se eleva tan rápido el tiempo de ejecución a medida que se aumenta la cantidad de puntos. Se han usado 15 puntos.
Se generaron posiciones iniciales y finales entre 0 y la cantidad de puntos menos 1 y luego se aplicó el algoritmo A*. Luego a través de un condicional se evalúa si la posición está en los obstáculos, no se lo agrega como vecino de la posición actual.
Se guarda el camino en la variable path para cada nodo y devuelve el mismo.

##Obtención de un camino óptimo dentro de un almacén
En primera instancia se crea el mapa del almacén mediante una función que admite tres parámetros: el orden del almacén (números del 1 al 48 de manera ordenada, ya creados por defecto aunque se puede modificar), la cantidad de filas y columnas de las estanterías, que en este caso están dadas según la consigna pero pueden ser modificadas. La función puede crearse de manera más dinámica dependiendo de lo que se necesite.

Para la realización de este algoritmo se utilizó un método en el cual se crean dos listas (inicialmente vacías) que se llamarán OPEN y CLOSED, en las cuales se guardarán los nodos abiertos pero no explorados y los ya explorados respectivamente. Se trabajó con clases, siendo los atributos de cada nodo sus costes g, la heurística h y el valor f y un apuntador a su padre; como métodos se usan funciones con las cuales se calculan f, g y h. Se comprueba en cada nodo el costo _f(n)=g(n)+h(n)_ y se avanza expandiendo el nodo hijo de menor costo. Si para un nodo ubicado en la lista cerrada se comprueba que el costo de la ruta a través del nodo explorado es menor al del costo que tenía anteriormente, se lo agrega a la lista abierta. 
La heurística utilizada en este algoritmo es similar a la distancia de Manhattan pero elevada al cuadrado, esto es, la distancia teniendo en cuenta solo movimientos verticales y horizontales en cuanto a la posición del nodo actual elevada al cuadrado.

Para localizar las posiciones entre las cuales realizar la búsqueda se usa la función _search position of_, la cual admite un parámetro valor y el mapa a usar; dependiendo de si el valor se encuentra a izquierda o derecha del pasillo central, devuelve el valor de la columna anterior o siguiente respectivamente. El problema encontrada con este diseño fue al hallar la posición inicial (0,0), la función devuelve el valor -1 porque resta uno a las columnas.

*COMPLETAR CON EL FUNCIONAMIENTO DEL ALGORITMO*
Cada vez que el nodo avanza se guarda el camino generado por el mismo de la siguiente manera: luego de llegar al nodo objetivo, se recorre ese nodo en sentido inverso a través del padre de cada nodo hasta llegar al nodo raiz.  

#Aplicación de Temple Simulado para la obtención del orden óptimo de picking de un almacén

El objetivo de este problema es obtener el orden óptimo para la operación de _picking_ en un almacén, utilizando el método de Temple simulado.

##Algoritmo
A continuación se hace mención de los parámetros que intervienen en el algoritmo:
-Estado inicial: En este caso el estado inicial es una lista que contiene las posiciones en donde se debe realizar el picking (las posiciones por las que debo pasar). Estas están ubicadas de manera aleatoria en la lista.

-Temperatura inicial: Es el estado inicial con el que se cuenta 

-Temperatura final: Es el valor final

-Perfil de descenso de temperatura: indica la razón a la cual va a disminuir la temeratura en cada iteración. La variación de este perfil condiciona la obtención de los resultados.
