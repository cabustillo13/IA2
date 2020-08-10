(define (domain capp)
(:requirements :equality :strips :action-costs)
(:predicates
	(orientacion ?o)
	(feature ?f)
    (tipo ?t)
    (operacion ?op)
    (feature-tipo ?f ?feat-tipo)
    (orientacion-pieza ?oa)
    (orientacion-feature ?f ?oa)
    (fabricable ?feat-tipo ?operacion)
    (fabricada ?feat)
    (maq_herr ?mh ?op)
    (montada-en ?mh)
) 

(:functions
    (total-cost)
)

(:action setup-orientacion
 :parameters ( ?orientacion-inicial ?orientacion-final )
 :precondition
	(and 
        (orientacion-pieza ?orientacion-inicial) 
        (orientacion ?orientacion-inicial) 
        (orientacion ?orientacion-final)
    )
 :effect
	(and 
		(orientacion-pieza ?orientacion-final)
		(not (orientacion-pieza ?orientacion-inicial))
        (increase (total-cost) 2)
	)
)

(:action op-fresado
 :parameters ( ?o ?f ?ft ?oper ?mh)
 :precondition
	(and 
        (orientacion-pieza ?o)
        (orientacion-feature ?f ?o)
        (orientacion ?o) 
        (feature ?f)
        (tipo ?ft)
        (feature-tipo ?f ?ft)
        (fabricable ?ft ?oper)
        (operacion ?oper)
        (= ?oper fresado)
        (maq_herr ?mh ?oper)
        (montada-en ?mh)
    )
 :effect
    (and
    (fabricada ?f)
    (increase (total-cost) 1)
    )
)

(:action op-taladrado
 :parameters ( ?o ?f ?ft ?oper ?mh)
 :precondition
	(and 
        (orientacion-pieza ?o)
        (orientacion-feature ?f ?o)
        (orientacion ?o) 
        (feature ?f)
        (tipo ?ft)
        (feature-tipo ?f ?ft)
        (fabricable ?ft ?oper)
        (operacion ?oper)
        (not (= ?f h1))
        (= ?oper taladrado)
        (maq_herr ?mh ?oper)
        (montada-en ?mh)
    )
 :effect
    (and
    (fabricada ?f)
    (increase (total-cost) 1)
    )
)

(:action op-torneado
 :parameters ( ?o ?f ?ft ?oper ?mh)
 :precondition
	(and 
        (orientacion-pieza ?o)
        (orientacion-feature ?f ?o)
        (orientacion ?o) 
        (feature ?f)
        (tipo ?ft)
        (feature-tipo ?f ?ft)
        (fabricable ?ft ?oper)
        (operacion ?oper)
        (= ?f h1)
        (= ?oper torneado)
        (maq_herr ?mh ?oper)
        (montada-en ?mh)
    )
 :effect
    (and
    (fabricada ?f)
    (increase (total-cost) 1)
    )
)

(:action montar-pieza
    :parameters (?mh1 ?oper1 ?mh2 ?oper2) ;mh1 es la maq_herr de la posicion actual y mh2 la maq_herr a utilizar
    :precondition 
    (and
        (operacion ?oper1)
        (operacion ?oper2)
        (maq_herr ?mh1 ?oper1)
        (maq_herr ?mh2 ?oper2)
        (montada-en ?mh1)
    )
    :effect 
    (and 
        (not(montada-en ?mh1))
        (montada-en ?mh2)
        (increase (total-cost) 3)
    )
)


)
