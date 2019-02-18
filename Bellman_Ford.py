from grafos import *

def Bellman_Ford(G, inicial, explicado=False):
    
    aristas=deepcopy(G.aristas)

    pesos=[G.dic_pesos[i] for i in aristas]

    nodos=deepcopy(G.vertices)

    v_inic=inicial
    m=[]

    n=[]
    
    if explicado:
        
        M=[]
        textos=['Inicio: ']

        # Creo mi matriz de distancias

        for i in nodos:
            n.append(i)

            if (v_inic,i) in aristas:
                m.append(pesos[aristas.index((v_inic,i))])

            elif (i,v_inic) in aristas:
                m.append(pesos[aristas.index((i, v_inic))])

            else:
                m.append(math.inf)
        m[inicial-1]=0
        
        m1=deepcopy(m)
        M.append(m1)

        iteraciones=len(nodos)-1

        # Empiezo a estudiar las distancias y a cambiarlas

        j=0
        while j < iteraciones:
            mm=deepcopy(m)
            for v_a in nodos:
                v_ady=G.vecinos(v_a)

                for i in v_ady:

                    if (v_a,i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i,v_a))]
                    if distancia < m[i-1]:
                        m[i-1]=distancia
                        n[i-1]=v_a
            
            m1=deepcopy(m)
            M.append(m1)
            textos.append('Iteración ' + str(j+1))
            
            if mm==m:
                j=iteraciones + 2
            else:
                j=j+1


        if j == iteraciones:
            mm=deepcopy(m)
            for v_a in nodos:
                v_ady=G.vecinos(v_a)

                for i in v_ady:
                    if (v_a,i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]

                    if distancia < m[i-1]:
                        m[i-1]=distancia
                        n[i-1]=v_a
            if mm!=m:
                m1=deepcopy(m)
                M.append(m1)
                textos.append('Iteración ' + str(iteraciones + 1) + '\n' + 'Hay ciclo negativo')
        
        G.pasoapaso(M,textos)

        
    
    else:

        # Creo mi matriz de distancias

        for i in nodos:
            n.append(i)

            if (v_inic,i) in aristas:
                m.append(pesos[aristas.index((v_inic,i))])

            elif (i,v_inic) in aristas:
                m.append(pesos[aristas.index((i, v_inic))])

            else:
                m.append(math.inf)
        m[inicial-1]=0
        print(m)
        iteraciones=len(nodos)-1

        # Empiezo a estudiar las distancias y a cambiarlas

        j=0
        while j < iteraciones:
            mm=deepcopy(m)
            for v_a in nodos:
                v_ady=G.vecinos(v_a)

                for i in v_ady:

                    if (v_a,i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i,v_a))]
                    if distancia < m[i-1]:
                        m[i-1]=distancia
                        n[i-1]=v_a
            print(m)
            if mm==m:
                j=iteraciones + 2
            else:
                j=j+1


        if j == iteraciones:
            mm=deepcopy(m)
            for v_a in nodos:
                v_ady=G.vecinos(v_a)

                for i in v_ady:
                    if (v_a,i) in aristas:
                        distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                    else:
                        distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]

                    if distancia < m[i-1]:
                        m[i-1]=distancia
                        n[i-1]=v_a
            if mm!=m:
                print('Hay ciclo negativo')

        return [m,n]
