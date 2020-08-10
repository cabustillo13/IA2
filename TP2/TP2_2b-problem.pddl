(define (problem capp-pieza)
    (:domain capp)
    (:objects 
        x_p
        y_p
        z_p
        x_n
        y_n
        z_n
        s2
        s4
        s6
        s9
        s10
        h1
        h3
        h5
        h7
        h9
        h11
        h12
        slot
        through-hole
        blind-hole
        fresado
        taladrado
        torneado
        fresadora
        taladro
        torno
    )
    (:init 
        (orientacion x_p) ;x+
        (orientacion y_p) ;y+
        (orientacion z_p) ;z+
        (orientacion x_n) ;x-
        (orientacion y_n) ;y-
        (orientacion z_n) ;z-
        
        (feature s2)
        (feature s4)
        (feature s6)
        (feature s9)
        (feature s10)
        (feature h1)
        (feature h3)
        (feature h5)
        (feature h7)
        (feature h9)
        (feature h11)
        (feature h12)
        
        (tipo slot)
        (tipo through-hole)
        (tipo blind-hole)
        
        (operacion fresado)
        (operacion taladrado)
        (operacion torneado)

        (maq_herr fresadora fresado) ;maq_herr / operacion q realiza
        (maq_herr taladro taladrado)
        (maq_herr torno torneado)

        (montada-en fresadora) ;La pieza inicia montada en la fresadora 

        (feature-tipo s2 slot)
        (feature-tipo s4 slot)
        (feature-tipo s6 slot)
        (feature-tipo s9 slot)
        (feature-tipo s10 slot)
        (feature-tipo h1 blind-hole)
        (feature-tipo h3 through-hole)
        (feature-tipo h5 blind-hole)
        (feature-tipo h7 through-hole)
        (feature-tipo h9 through-hole)
        (feature-tipo h11 blind-hole)
        (feature-tipo h12 blind-hole)

        (orientacion-pieza x_n)
        (orientacion-feature s2 x_p)
        (orientacion-feature s4 x_n)
        (orientacion-feature s6 x_p)
        (orientacion-feature s9 z_p)
        (orientacion-feature s10 z_p)
        (orientacion-feature h1 z_p)
        (orientacion-feature h3 z_p)
        (orientacion-feature h5 z_p)
        (orientacion-feature h7 x_p)
        (orientacion-feature h9 x_p)
        (orientacion-feature h11 x_p)
        (orientacion-feature h12 x_p)

        (fabricable slot fresado)
        (fabricable blind-hole taladrado)
        (fabricable through-hole taladrado)
        (fabricable blind-hole torneado) ;solo puede fabricar h1

        (= (total-cost) 0) 
    )
    (:goal 
        (and
            (fabricada s2)
            (fabricada s4)
            (fabricada s6)
            (fabricada s9)
            (fabricada s10)
            (fabricada h1)
            (fabricada h3)
            (fabricada h5)
            (fabricada h7)
            (fabricada h9)
            (fabricada h11)
            (fabricada h12)
        )
    )
    (:metric minimize (total-cost))
)