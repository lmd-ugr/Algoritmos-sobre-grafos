
# coding: utf-8

# In[1]:


from grafos import *


# In[2]:


g=Grafo()


# In[3]:


g.añadir_arista(1,2)
g.añadir_arista(1,3)
g.añadir_arista(1,4)
g.añadir_arista(1,5)
g.añadir_arista(2,3)
g.añadir_arista(4,5)
g.añadir_arista(5,6)
g.añadir_arista(7,5)


# In[4]:


g.dibujar('neato')


# In[6]:


def Hierholzer(gg, explicado=False):
    
    if explicado:
        g=deepcopy(gg)
        g1=deepcopy(g)
        G=[g1]
        textos=[]
        C=[]
        CC=[]
        aristas_marcadas=[]

        # Añado la arista

        l=[i for i in g.vertices if g.grado(i)%2!=0]
        g.añadir_arista(l[0], l[1])
        textos.append('Grafo inicial. Arista añadida: ' + str((l[0], l[1])))

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
            
        L=[G[0].resaltar_arista((l[0], l[1])).render('0')]

        for i in range(1,len(G)):
            L.append(G[i].resaltar_arista(aristas_marcadas[i-1]).render(str(i)))

        g.pasoapaso(L, textos, t)

    else:
        g=deepcopy(gg)
        C=[]

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


# In[7]:


Hierholzer(g, True)
