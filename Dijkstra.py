from grafos import *

def Dijkstra(gg, inicial, explicado=False):
    
    g=deepcopy(gg)

    aristas=deepcopy(g.aristas)

    pesos=[g.dic_pesos[i] for i in aristas]

    nodos=g.vertices

    v_inic=inicial
    escogidos=[v_inic]
    m=[]
    n=[]
        
    if explicado:
        M=[]
        textos=['']
        notas=['Vector inicial']

        # Creo mi matriz de distancias

        for i in nodos:
            m.append(math.inf)
            n.append(v_inic)
        
        m[v_inic-1]=0
        h=deepcopy(m)
        h1=deepcopy(n)
        M.append({'Distancias':h, 'Ruta':h1})

        # Empiezo a estudiar las distancias y a cambiarlas

        v_a=v_inic


        while len(escogidos)!=len(nodos):  #Termino el algoritmo cuando no haya mas vertices adyacentes

            v_ady=[i for i in g.vecinos(v_a) if i not in escogidos]
            l=[]

            for i in v_ady:

                if (v_a,i) in aristas:
                    distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                else:
                    distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                if distancia < m[i-1]:
                    m[i-1]=distancia
                    n[i-1]=v_a
                    l.append(i)

            notas.append('Actualizamos distancia a los siguientes nodos: ' + str(l))
            h=deepcopy(m)
            h1=deepcopy(n)
            M.append({'Distancias':h, 'Ruta':h1})


            # Cojo los nodos adyacentes y escojo como v_a aquel cuya distancia a v_inic sea la menor

            siguientes=[m[i-1] for i in nodos if i not in escogidos]

            v_a = m.index(min(siguientes)) + 1

            escogidos.append(v_a)
            
            textos.append('Marcamos el vértice ' + str(v_a))

        textos.append('')
        notas.append('Vector final')
        h=deepcopy(m)
        h1=deepcopy(n)
        M.append({'Distancias':h, 'Ruta':h1})
        g.pasoapaso(M, notas, textos)
        
        
        
    else:

        # Creo mi matriz de distancias

        for i in nodos:
            m.append(math.inf)
            n.append(v_inic)
        m[v_inic-1]=0

        # Empiezo a estudiar las distancias y a cambiarlas

        v_a=v_inic


        while len(escogidos)!=len(nodos):  # Termino el algoritmo cuando no haya más vertices adyacentes

            v_ady=[i for i in g.vecinos(v_a) if i not in escogidos]

            for i in v_ady:

                if (v_a,i) in aristas:
                    distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                else:
                    distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                if distancia < m[i-1]:
                    m[i-1]=distancia
                    n[i-1]=v_a

            print('m= ', m)


            # Cojo los nodos adyacentes y escojo como v_a aquel cuya distancia a v_inic sea la menor

            siguientes=[m[i-1] for i in nodos if i not in escogidos]

            v_a = m.index(min(siguientes)) + 1

            escogidos.append(v_a)

        dic={'Pesos': m, 'Ruta': n}    

        return dic
