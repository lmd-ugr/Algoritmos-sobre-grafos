from grafos import *

def Kauffman_Malgrange(g, explicado=False):
    
    #Producto de matrices
    def producto(a,b):
        c=[]
        k=0


        while k < len(a):  # Contador FILAS
            i=0
            aux=[]  #En aux guardaré los elementos definitivos, los que compondrán la fila de mi nueva matriz
            while i < len(a):   # Contador COLUMNAS

                l=[]     # l contiene todos los productos de la fila por la columna, pero yo solo necesito los que
                        # no sean infinito
                for j in range(len(a)):   # Contador ELEMENTOS FILA-COLUMNA

                    if a[k][j]== math.inf or b[j][i]==math.inf:  # Si alguno de mis elementos es infinito, el result
                        l.append(math.inf) # es infinito, lo añado a l.

                    elif a[k][j][-1] == b[j][i][0]:  # Si lo que tengo es t-upla por t-upla y coinciden sus extremos
                        l.append(a[k][j][:-1]+b[j][i]) # añado el camino a l
                        #print(a[k][j][:-1], ' + ', )

                    elif type(a[k][j])==list:   # Si a es una lista, veo si b también lo es o no
                        if type(b[j][i])==list:
                            for g in a[k][j]:
                                for h in b[j][i]:
                                    if g[-1]==h[0]:
                                        #print(g[:-1], ' + ', h)
                                        l.append(g[:-1]+h)
                        else:
                            for g in a[k][j]:
                                if g[-1]==b[j][i][0]:
                                    #print(g[:-1], ' + ', b[j][i][0])
                                    l.append(g[:-1]+b[j][i])


                # Ahora limpio l, me quedo con el camino si hubiera y, si no, con infinito.

                s=[v for v in l if v!= math.inf]
                if len(s)==1:
                    aux.append(s[0])
                elif len(s)>1:
                    aux.append(s)
                else:
                    aux.append(math.inf)
                i=i+1

            c.append(aux)

            k=k+1

        return c
    
    
    # Ahora, una vez obtenida la nueva matriz, deberiamos proceder a limpiarla, es decir, si hay algún ciclo,
    # sustituirlo por un infinito. 

    # Hago una primera limpieza para quitar los ciclos y, si resulta que un elemento de M tenia 3 ciclos, 
    # en lugar de sustituirlos por tres infinitos, quiero quedarme solo con un infinito y no tener una lista ya


    # 1ª LIMPIEZA

    def limp1(M):

        for i in range(len(M)):
            for j in range(len(M[i])):
                if type(M[i][j])==list:

                    for k in range(len(M[i][j])):
                        if len(M[i][j][k]) > len(set(M[i][j][k])):
                            M[i][j][k]=math.inf

                    # Cuando acabo este for, puedo obtener listas con tuplas e infinitos, sustituyo entonces ese 
                    # elemento de M por la misma lista pero sin infinitos.
                    auxi=[s for s in M[i][j] if s != math.inf]

                    if len(auxi)==1:
                        M[i][j]=auxi[0]
                        #print(M[i][j])
                    elif len(auxi)==0:
                        M[i][j]=math.inf
                    else:
                        M[i][j]=auxi
                        
                elif type(M[i][j])==tuple:  # Compruebo que no se repita ningún vértice
                    #print(M[i][j])
                    if len(M[i][j]) > len(set(M[i][j])):   
                        M[i][j]=math.inf 

        return M
    
    
    
    # 2ª LIMPIEZA, me quedo solo con un infinito, no con muchos en el mismo elemento M_ij de M.
    def limp2(M):
    
        for i in range(len(M)):
            for j in range(len(M[i])):
                if type(M[i][j])==list:
                    if set(M[i][j])=={math.inf}:
                        M[i][j]=math.inf
        return M

#-----------------------------------------------------------------------------------------------------------
    
    # Ahora empieza el algoritmo
   
    if explicado:
        
        m=[]  # Cojo mi matriz primera m
        H=[] # Aquí voy guardando las matrices obtenidas para mostrar el proceso paso a paso
        textos=[]
        iter=1

        v=g.vertices

        for i in range(len(v)):
            n=[]
            for j in range(len(v)):
                if (v[i], v[j]) in g.aristas or (v[j],v[i]) in g.aristas:
                    n.append((v[i], v[j]))
                else:
                    n.append(math.inf)
            m.append(n)

        a=deepcopy(m)
        H.append(a)
        textos.append('Matriz de partida \n')

        #print(m)
        M=producto(m,m)
        a=deepcopy(M)
        H.append(a)
        textos.append('Multiplicación latina. Iteración: ' + str(iter) + '\n')

        M=limp1(M)
        a=deepcopy(M)
        H.append(a)
        textos.append('Primera limpieza, sustituimos los ciclos por infinitos. Iteración: ' + str(iter) + '\n')

        M=limp2(M)
        a=deepcopy(M)
        H.append(a)
        textos.append('Segunda limpieza: Si un elemento de la matriz posee varios infinitos, los reducimos a uno solo. Iteración: ' + str(iter) + '\n')
        #print(M)
        iter=iter+1

        for i in range(len(g.vertices)-3):

            M=producto(M,m)
            a=deepcopy(M)
            H.append(a)
            textos.append('Multiplicación latina. Iteración: ' + str(iter) + '\n')

            M=limp1(M)
            a=deepcopy(M)
            H.append(a)
            textos.append('Primera limpieza, sustituimos los ciclos por infinitos. Iteración: ' + str(iter) + '\n')

            M=limp2(M)
            a=deepcopy(M)
            H.append(a)
            textos.append('Segunda limpieza: Si un elemento de la matriz posee varios infinitos, los reducimos a uno solo. Iteración: ' + str(iter) + '\n')
            #print(M)
            iter=iter+1

        # En l guardo mis caminos hamiltonianos

        l=[]

        for i in M:
            for j in i:
                if j!=math.inf:
                    l.append(j)


        H.append(l)
        textos.append('Caminos Hamiltonianos: ')
        
        g.pasoapaso(H, textos)


    else:
        
        m=[]  # Cojo mi matriz primera m

        v=g.vertices

        for i in range(len(v)):
            n=[]
            for j in range(len(v)):
                if (v[i], v[j]) in g.aristas or (v[j],v[i]) in g.aristas:
                    n.append((v[i], v[j]))
                else:
                    n.append(math.inf)
            m.append(n)

        #print(m)
        M=producto(m,m)

        M=limp1(M)
    
        M=limp2(M)
        #print(M)

        for i in range(len(g.vertices)-3):

            M=producto(M,m)
        
            M=limp1(M)
        
            M=limp2(M)
            #print(M)
            

        # En l guardo mis caminos hamiltonianos

        l=[]

        for i in M:
            for j in i:
                if j!=math.inf:
                    l.append(j)


        return l

