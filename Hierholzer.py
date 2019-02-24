from grafos import *

def Hierholzer(gg, explicado=False):
    
    if explicado:
        g=deepcopy(gg)
        
        if g.es_euleriano()==-1:
            return False

        elif g.es_euleriano()==2:
            g1=deepcopy(g)
            G=[]
            textos=[]
            C=[]
            CC=[]
            aristas_marcadas=[]

            # Añado la arista

            l=[i for i in g.vertices if g.grado(i)%2!=0]
            g.añadir_arista(l[0], l[1])
            textos.append('Grafo inicial. Arista añadida: ' + str((l[0], l[1])))

            g2=deepcopy(g)
            G.append(g2)

            ciclos=[i for i in g.ciclos() if len(i)>3]

            # Voy guardando mi partición en ciclos pero, el primer ciclo que debo coger tiene que incluir la arista que voy a eliminar.
            # Y los demás, deben empezar en vértices de los anteriores ciclos que tengan aristas adyacentes aún.

            parar=False
            for i in ciclos: # Recorro los ciclos de g, si encuentro uno de los vértices impares, miro a ver si el siguiente también lo 
                if i[0]==l[0]  or i[0]==l[1]: # es. En ese caso, me quedo con ese ciclo como el principal, sobre el que incluiré los demás.
                    if i[1]==l[0] or i[1]==l[1]:
                        C.append(i)
                        parar=True
                if parar==True:
                    break

            for i in range(len(C[0])-1): # Borro ahora las aristas que intervienen en mi ciclo principal
                g.borrar_arista(C[0][i], C[0][i+1])
                CC.append((C[0][i], C[0][i+1]))  
            
                                     # Esta condición es para no perder la arista añadida. Al resaltar la arista,
            CC.append((l[0], l[1]))  # como son paralelas, la función resaltar somo me representa una, pero en realidad
                                     # hay dos. Por eso la añado, para resaltarla. Pero solo una vez.

            aristas_marcadas.append(CC)
            g1=deepcopy(g)
            G.append(g1)
            textos.append('Borro el ciclo: ' + str(C[0]))

            # Empiezo a coger los demás ciclos de G, aquellos que empiecen en vértices ya marcados.

            s=set(C[0])
            ls=list(s)

            ciclos=[i for i in g.ciclos() if len(i)>3]

            while len(ciclos)>0:
                i=0
                stop=False

                while stop==False:

                    if ciclos[i][0] in s:
                        C.append(ciclos[i]) # Guardo los elementos de mi nuevo ciclo en ls para luego hacer set(ls) y tener ahi los verts
                                            # que he usado.
                        for j in ciclos[i]:
                            ls.append(j)
                        s=set(ls)
                        stop=True
                    else:
                        i=i+1
                CC=[]
                for j in range(len(ciclos[i])-1):
                    g.borrar_arista(ciclos[i][j], ciclos[i][j+1])
                    CC.append((ciclos[i][j], ciclos[i][j+1]))  

                aristas_marcadas.append(CC)
                g1=deepcopy(g)
                G.append(g1)
                textos.append('Borro el ciclo: ' + str(ciclos[i]))

                ciclos=[h for h in g.ciclos() if len(h)>3]

            #print(C)

            # Ahora introduzco todos los demás ciclos en mi ciclo principal, que ocupa la posición 0 en C dejando siempre la arista 
            # añadida al principio o al final del ciclo final.

            # Si el ciclo siguiente empieza con un vértice de mi arista añadida, lo añado en la posición C[0][2:].index(v_inicial)+2, ya
            # que los elementos 0 y 1 de C[0] es mi arista añadida. Si no, lo añado donde sea.

            K=deepcopy(C[0])
            t=['' , 'Camino de Euler: ' + str(K)]

            for i in C[1:]: # Empiezo en el segundo ciclo de C, el primero es mi ciclo principal

                if i[0]==l[0] or i[0]==l[1]:

                    pos=K[2:].index(i[0])+2
                    del(K[pos])

                    for j in range(len(i)-1,-1,-1):
                        K.insert(pos,i[j])


                else:
                    pos=K.index(i[0])
                    del(K[pos])

                    for j in range(len(i)-1,-1,-1):
                        K.insert(pos,i[j])

                t.append('Camino de Euler: ' + str(K))

            # Ahora borro la arista 

            del(K[0])
            t[-1]='Camino de Euler: ' + str(K)

            # WIDGETS 

            L=[G[0].resaltar_arista([(l[0], l[1]), (l[0], l[1])]).render('0')]

            for i in range(1,len(G)):
                L.append(G[i].resaltar_arista(aristas_marcadas[i-1]).render(str(i)))

            g.pasoapaso(L, textos, t)
            
        else:

            C=[]
            textos=['Grafo inicial']
            g1=deepcopy(g)
            G=[g1]
            E=[]
            e=[]
            
            c = [i for i in g.ciclos() if len(i)>3]

            while len(c)>0:
                C.append(c[0])

                for i in range(len(c[0])-1):
                    g.borrar_arista(c[0][i], c[0][i+1])
                    e.append((c[0][i], c[0][i+1]))

                g1=deepcopy(g)
                G.append(g1)
                textos.append('Eliminamos el ciclo: ' + str(e))
                c = [i for i in g.ciclos() if len(i)>3]
                E.append(e)
                e=[]

            # Unifico los ciclos

            C1=deepcopy(C[0])
            C2=['']
            C2.append('Circuito de Euler: ' + str(C1))
            del(C[0])

            for i in C:
                pos = C1.index(i[0])
                del(C1[0])
                for j in i:
                    C1.insert(pos, j)
                C2.append('Circuito de Euler: ' + str(C1))  
                    
            L=[G[0].dibujar('circo').render('0')]
            
            for i in range(1,len(G)):
                L.append(G[i].resaltar_arista(E[i-1],{},'red','3','circo').render(str(i)))

            g.pasoapaso(L, textos, C2)
            
        
    else:
        
        g=deepcopy(gg)
        C=[]

        if g.es_euleriano()==-1:
            return False

        elif g.es_euleriano()==2:

            # Añado la arista

            l=[i for i in g.vertices if g.grado(i)%2!=0]
            g.añadir_arista(l[0], l[1])

            ciclos=[i for i in g.ciclos() if len(i)>3]

            # Voy guardando mi partición en ciclos pero, el primer ciclo que debo coger tiene que incluir la arista que voy a eliminar.
            # Y los demás, deben empezar en vértices de los anteriores ciclos que tengan aristas adyacentes aún.

            parar=False
            for i in ciclos: # Recorro los ciclos de g, si encuentro uno de los vértices impares, miro a ver si el siguiente también lo 
                if i[0]==l[0]  or i[0]==l[1]: # es. En ese caso, me quedo con ese ciclo como el principal, sobre el que incluiré los demás.
                    if i[1]==l[0] or i[1]==l[1]:
                        C.append(i)
                        parar=True
                if parar==True:
                    break

            for i in range(len(C[0])-1): # Borro ahora las aristas que intervienen en mi ciclo principal
                    g.borrar_arista(C[0][i], C[0][i+1])

            # Empiezo a coger los demás ciclos de G, aquellos que empiecen en vértices ya marcados.

            s=set(C[0])
            ls=list(s)

            ciclos=[i for i in g.ciclos() if len(i)>3]

            while len(ciclos)>0:
                i=0
                stop=False

                while stop==False:

                    if ciclos[i][0] in s:
                        C.append(ciclos[i]) # Guardo los elementos de mi nuevo ciclo en ls para luego hacer set(ls) y tener ahi los verts
                                            # que he usado.
                        for j in ciclos[i]:
                            ls.append(j)
                        s=set(ls)
                        stop=True
                    else:
                        i=i+1

                for j in range(len(ciclos[i])-1):
                    g.borrar_arista(ciclos[i][j], ciclos[i][j+1])

                ciclos=[h for h in g.ciclos() if len(h)>3]

            #print(C)

            # Ahora introduzco todos los demás ciclos en mi ciclo principal, que ocupa la posición 0 en C dejando siempre la arista 
            # añadida al principio o al final del ciclo final.

            # Si el ciclo siguiente empieza con un vértice de mi arista añadida, lo añado en la posición C[0][2:].index(v_inicial)+2, ya
            # que los elementos 0 y 1 de C[0] es mi arista añadida. Si no, lo añado donde sea.

            K=deepcopy(C[0])

            for i in C[1:]: # Empiezo en el segundo ciclo de C, el primero es mi ciclo principal

                if i[0]==l[0] or i[0]==l[1]:

                    pos=K[2:].index(i[0])+2
                    del(K[pos])

                    for j in range(len(i)-1,-1,-1):
                        K.insert(pos,i[j])


                else:
                    pos=K.index(i[0])
                    del(K[pos])

                    for j in range(len(i)-1,-1,-1):
                        K.insert(pos,i[j])

            # Ahora borro la arista 

            del(K[0])

            return K

        else:
            c = [i for i in g.ciclos() if len(i)>3]

            while len(c)>0:
                C.append(c[0])

                for i in range(len(c[0])-1):
                    g.borrar_arista(c[0][i], c[0][i+1])

                c = [i for i in g.ciclos() if len(i)>3]

            # Unifico los ciclos

            C1=deepcopy(C[0])
            del(C[0])

            for i in C:
                pos = C1.index(i[0])
                del(C1[0])
                for j in i:
                    C1.insert(pos, j)
            return C1

