
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
        textos=['Inicio: ']

        # Creo mi matriz de distancias

        for i in nodos:
            m.append(math.inf)
            n.append(i)
        m[v_inic-1]=0
        #print('m= ', m)

        # Empiezo a estudiar las distancias y a cambiarlas

        v_a=v_inic


        while len(escogidos)!=len(nodos):  #Termino el algoritmo cuando no haya mas vertices adyacentes

            v_ady=[i for i in g.vecinos(v_a) if i not in escogidos]
            #print('vertices adyacentes:', v_ady)

            for i in v_ady:

                if (v_a,i) in aristas:
                    distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                else:
                    distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                if distancia < m[i-1]:
                    #print('Cambio distancia ', m[i-1])
                    #print(' por ', distancia)
                    m[i-1]=distancia
                    n[i-1]=v_a

            h=deepcopy(m)
            M.append(h)


            # Cojo los nodos adyacentes y escojo como v_a aquel cuya distancia a v_inic sea la menor

            siguientes=[m[i-1] for i in nodos if i not in escogidos]
            #print(siguientes)

            v_a = m.index(min(siguientes)) + 1
            #print('vertice actual= ', v_a)

            escogidos.append(v_a)
            #print('escogidos: ', escogidos)
            
        for i in range(len(M)):
            textos.append('Iteración ' + str(i+1))

        g.pasoapaso(M, textos)
        
        
    else:

        # Creo mi matriz de distancias

        for i in nodos:
            m.append(math.inf)
            n.append(i)
        m[v_inic-1]=0
        #print('m= ', m)


        # Empiezo a estudiar las distancias y a cambiarlas

        v_a=v_inic


        while len(escogidos)!=len(nodos):  #Termino el algoritmo cuando no haya mas vertices adyacentes

            v_ady=[i for i in g.vecinos(v_a) if i not in escogidos]
            #print('vertices adyacentes:', v_ady)

            for i in v_ady:

                if (v_a,i) in aristas:
                    distancia = m[v_a-1] + pesos[aristas.index((v_a,i))]
                else:
                    distancia = m[v_a-1] + pesos[aristas.index((i, v_a))]
                if distancia < m[i-1]:
                    #print('Cambio distancia ', m[i-1])
                    #print(' por ', distancia)
                    m[i-1]=distancia
                    n[i-1]=v_a

            print('m= ', m)


            # Cojo los nodos adyacentes y escojo como v_a aquel cuya distancia a v_inic sea la menor

            siguientes=[m[i-1] for i in nodos if i not in escogidos]
            #print(siguientes)

            v_a = m.index(min(siguientes)) + 1
            #print('vertice actual= ', v_a)

            escogidos.append(v_a)
            #print('escogidos: ', escogidos)

        return ['Pesos=', m, 'Ruta= ', n]
