(define (domain aviones)
(:requirements :strips :action-costs)
(:predicates
	(en ?a ?b) 
	(avion ?a)
	(carga ?c)
	(aeropuerto ?a)
) 

(:functions
  (distancia ?origen ?destino)
  (total-cost)
)

(:action cargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?ap) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?a) 
		(not (en ?c ?ap))
		(increase (total-cost) 1)
	)
)
(:action descargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?a) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?ap) 
		(not (en ?c ?a))
		(increase (total-cost) 1)
	)
)
(:action volar
 :parameters ( ?a ?origen ?destino)
 :precondition
	(and (en ?a ?origen) (avion ?a) (aeropuerto ?origen) (aeropuerto ?destino))
 :effect
	(and 
		(en ?a ?destino) 
		(not (en ?a ?origen))
		(increase (total-cost) (distancia ?origen ?destino))
	)
)
)
