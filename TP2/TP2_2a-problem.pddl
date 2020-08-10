(define (problem carga-aerea) 
    
    ;Se recomienda utilizar additive heuristic
    ; ./fast-downward.py TP2_2a-domain.pddl TP2_2a-problem.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"
    ;o
    ; ./fast-downward.py TP2_2a-domain.pddl TP2_2a-problem.pddl --evaluator "hcea=cea()" --search "lazy_greedy([hcea], preferred=[hcea])"

    (:domain aviones)         
    (:objects                 
        LA01                  
        LA02
        LA03
        LA04
        AA01
        AA02
        AA03
        FB01
        FB02
        FB03
        MDZ ;Mendoza
        AEP ;Buenos Aires
        COR ;Cordoba
        SFN ;Santa Fe
        IGB ;Rio Negro
        FERTILIZANTE
        TELA-GRANIZO
        COSECHADORA
        AUTOPARTES
        ELECTRONICA
    )
    (:init 
        (avion LA01)
        (avion LA02)
        (avion LA03)
        (avion LA04)
        (avion AA01)
        (avion AA02)
        (avion AA03)
        (avion FB01)
        (avion FB02)
        (avion FB03)
        (aeropuerto MDZ)
        (aeropuerto AEP)
        (aeropuerto COR)
        (aeropuerto SFN)
        (aeropuerto IGB)
        (carga FERTILIZANTE)
        (carga TELA-GRANIZO)
        (carga COSECHADORA)
        (carga AUTOPARTES)
        (carga ELECTRONICA)
        (en LA01 MDZ)
        (en LA02 AEP)
        (en LA03 COR)
        (en LA04 MDZ) 
        (en AA01 SFN)
        (en AA02 MDZ)
        (en AA03 AEP)
        (en FB01 COR)
        (en FB02 AEP)
        (en FB03 SFN)
        (en FERTILIZANTE AEP)
        (en TELA-GRANIZO SFN)
        (en COSECHADORA MDZ)
        (en AUTOPARTES COR)
        (en ELECTRONICA IGB)
        (= (total-cost) 0) 
        (= (distancia MDZ AEP) 3) ;Datos calculados en funcion de los km entre aeropuertos con distancias reales
        (= (distancia MDZ COR) 2) ;distancia_entre_aeropuertos / 300 y se aproxima al entero
        (= (distancia MDZ SFN) 3)
        (= (distancia MDZ IGB) 3)

        (= (distancia AEP MDZ) 3) 
        (= (distancia AEP COR) 2)
        (= (distancia AEP SFN) 1)
        (= (distancia AEP IGB) 4)

        (= (distancia COR MDZ) 2)
        (= (distancia COR AEP) 2)
        (= (distancia COR SFN) 1)
        (= (distancia COR IGB) 4)
        
        (= (distancia SFN MDZ) 3)
        (= (distancia SFN AEP) 1)
        (= (distancia SFN COR) 1)   
        (= (distancia SFN IGB) 5)

        (= (distancia IGB MDZ) 3)
        (= (distancia IGB AEP) 4)
        (= (distancia IGB COR) 4)   
        (= (distancia IGB SFN) 5)

        (= (distancia MDZ MDZ) 0)
        (= (distancia AEP AEP) 0)
        (= (distancia COR COR) 0)
        (= (distancia SFN SFN) 0)
        (= (distancia IGB IGB) 0)
    )
    (:goal 
        (and
            (en FERTILIZANTE SFN)
            (en TELA-GRANIZO MDZ)
            (en COSECHADORA COR)
            (en AUTOPARTES AEP)
            (en ELECTRONICA COR) ;Lo interesante de esta carga es que inicialmente esta en IGB pero no hay aviones alla
        )
    )
    (:metric minimize (total-cost))
)