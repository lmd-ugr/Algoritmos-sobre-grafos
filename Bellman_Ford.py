
# coding: utf-8

# In[12]:


from grafos import *


# In[13]:


import math


# In[14]:


g=Grafo()


# In[15]:


g.añadir_arista(1,2)
g.añadir_arista(1,3)
g.añadir_arista(3,2)
g.añadir_arista(4,2)
g.añadir_arista(4,3)


# In[16]:


g.ponderado([5,10,-5,10,10])


# In[17]:


g.dibujar_ponderado('circo')


# In[18]:


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
        
        g.pasoapaso(M,textos)

        
    
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


# In[19]:


Bellman_Ford(g,1,True)


# In[20]:


Bellman_Ford(g,1)


# In[21]:


for i in g.vertices:
    print('Vértice ' + str(i) + ': ')
    b=Bellman_Ford(g,i)
    print('Output:', b, '\n')

