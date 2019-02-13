from grafos import *

def Floyd_Warshall(G, explicado=False):    
    
    #Extraigo los datos necesarios del grafo

    nodos=deepcopy(G.vertices)
    aristas=deepcopy(G.aristas)
    pesos=[G.dic_pesos[i] for i in aristas]
    #print(pesos)

    # Voy haciendo listas para cada nodo y, al final, esa lista la meto en m, como una de sus filas.

    m=[]
    fila=[]

    for i in nodos:
        for j in nodos:
            if (i,j) in aristas:
                fila.append(pesos[aristas.index((i,j))])
            elif (j,i) in aristas:
                fila.append(pesos[aristas.index((j,i))])
            elif i==j:
                fila.append(0)
            else:
                fila.append(math.inf)
                
        m.append(fila)
        fila=[]

    # Matriz que me indica el camino a seguir

    R=[]
    l=[]

    for i in nodos:
        for j in nodos:
            if i==j:
                l.append('-')
            else:
                l.append(j)
        R.append(l)
        l=[]
    
    if explicado:
        
        M=[]  # Aquí guardo las distintas matrices para los widgets
        textos=['Inicio']
        m1=deepcopy(m)
        M.append(m1)

        #Cambio los elementos de las matrices m y R.   

        s=0
        for k in nodos:
            for i in nodos:
                s=0
                #if i!=k:
                for j in nodos:
                    #if j!=i:
                    s = m[i-1][k-1] + m[k-1][j-1]
                    if(s < m[i-1][j-1]):

                        m[i-1][j-1] = s
                        R[i-1][j-1] = k
            m1=deepcopy(m)
            M.append(m1)
            textos.append('Nodo intermedio: ' + str(k))

        parar = False
        t=0

        #PRIMERO COMPRUEBO QUE NO HAY VALORES NEGATIVOS EN LA DIAGONAL. SI ES EL CASO, ES DECIR, PARAR == FALSE, ENTONCES HAGO UNA
        #SEGUNDA ITERACION DEL ALGORITMO

        while t <len(nodos) and parar == False:
            if m[t][t] < 0:
                m1=deepcopy(m)
                M.append(m1)
                textos.append('Hay elementos negativos en la diagonal, por tanto, hay ciclos negativos y no es posible hallar el camino de peso mínimo.')
                parar=True
            else:
                t=t+1

        if parar == False:    
            #print(parar)
            s=0
            mm=deepcopy(m)
            for k in nodos:
                for i in nodos:
                    s=0
                    #if i!=k:
                    for j in nodos:
                        #if j!=i:
                        s = m[i-1][k-1] + m[k-1][j-1]
                        if(s < m[i-1][j-1]):

                            m[i-1][j-1] = s



            if mm != m:
                m1=deepcopy(m)
                M.append(m)
                textos.append('Hay ciclos negativos, no se puede hallar el camino de peso mínimo.')
        
        g.pasoapaso(M, textos)
        
        return [M, textos]

        
    else:

        #Cambio de elementos de las matrices m y R.   

        s=0
        for k in nodos:
            for i in nodos:
                s=0
                if i!=k:
                    for j in nodos:
                        if j!=i:
                            s = m[i-1][k-1] + m[k-1][j-1]
                            if(s < m[i-1][j-1]):

                                m[i-1][j-1] = s
                                R[i-1][j-1] = k

        parar = False
        t=0

        #PRIMERO COMPRUEBO QUE NO HAY VALORES NEGATIVOS EN LA DIAGONAL. SI ES EL CASO, ES DECIR, PARAR == FALSE, ENTONCES HAGO UNA
        #SEGUNDA ITERACION DEL ALGORITMO

        while t <len(nodos) and parar == False:
            if m[t][t] < 0:
                #print('Hay ciclos negativos, no es posible hallar el camino de peso mínimo.')
                parar=True
            else:
                t=t+1

        if parar == False:    
            #print(parar)
            s=0
            mm=deepcopy(m)
            for k in nodos:
                for i in nodos:
                    s=0
                    if i!=k:
                        for j in nodos:
                            if j!=i:
                                s = m[i-1][k-1] + m[k-1][j-1]
                                if(s < m[i-1][j-1]):

                                    m[i-1][j-1] = s



            if mm != m:
                print('Hay ciclos negativos, no se puede hallar el camino de peso mínimo.')

        return [m,R]
