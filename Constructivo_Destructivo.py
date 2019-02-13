
# coding: utf-8

# In[1]:


from grafos import *


# In[2]:


g=Grafo()


# In[3]:


g.añadir_arista(5,2)
g.añadir_arista(5,0)
g.añadir_arista(2,6)
g.añadir_arista(6,0)
g.añadir_arista(6,3)
g.añadir_arista(0,3)


# In[4]:


g.dibujar('neato')


# In[5]:


def Destructivo(g, explicado=False):

    gg=deepcopy(g)
    G=[g]
    
    if explicado == True:
        
        textos=['Grafo inicial']
        E=[]
        
        ciclos=[i for i in gg.ciclos() if len(i)>3]

        while len(ciclos)>0:
            if (ciclos[0][1], ciclos[0][0]) in gg.aristas:
                gg.borrar_arista(ciclos[0][1], ciclos[0][0])
                g1=deepcopy(gg)
                G.append(g1)
                textos.append('Borramos la arista (' + str(ciclos[0][1]) + ',' + str(ciclos[0][0]) + ')')
                E.append((ciclos[0][1], ciclos[0][0]))
            else:
                gg.borrar_arista(ciclos[0][0], ciclos[0][1])
                g1=deepcopy(gg)
                G.append(g1)
                textos.append('Borramos la arista (' + str(ciclos[0][0]) + ',' + str(ciclos[0][1]) + ')')
                E.append((ciclos[0][0], ciclos[0][1]))

            ciclos=[i for i in gg.ciclos() if len(i)>3]

        L=[G[0].dibujar().render('0')]

        for i in range(1,len(G)):
            L.append(G[i].resaltar_arista(E[i-1]).render(str(i)))
        
        L.append(G[-1].dibujar().render(str(len(G))))
        
        textos.append('Grafo final')

        g.pasoapaso(L, textos)        
    
    else:
        
        ciclos=[i for i in gg.ciclos() if len(i)>3]

        while len(ciclos)>0:
            if (ciclos[0][1], ciclos[0][0]) in gg.aristas:
                gg.borrar_arista(ciclos[0][1], ciclos[0][0])
                g1=deepcopy(gg)
                G.append(g1)
                print('borro', (ciclos[0][1], ciclos[0][0]))
            else:
                gg.borrar_arista(ciclos[0][0], ciclos[0][1])
                g1=deepcopy(gg)
                G.append(g1)
                print('borro', (ciclos[0][0], ciclos[0][1]))

            ciclos=[i for i in gg.ciclos() if len(i)>3]

        return [gg, G]


# In[6]:


Destructivo(g, True)


# In[7]:


def Constructivo(gg, explicado=False):
    
    aristas=deepcopy(gg.aristas)
    g=Grafo()
    
    if explicado==True:
        
        G=[]
        textos=[]
        E=[]
        g1=Grafo()
    
        while len(aristas)>0:

            a=aristas[0]
            g.añadir_arista(a[0], a[1])
            g1=deepcopy(g)
            G.append(g1)
            textos.append('Añadimos la arista (' + str(a[0]) + ',' + str(a[1]) + ')')
            E.append((a[0], a[1]))
            aristas.remove((a[0],a[1]))
            if len([i for i in g.ciclos() if len(i)>3])>0:
                g.borrar_arista(a[0], a[1])
                g1=deepcopy(g)
                G.append(g1)
                textos.append('Borramos la arista (' + str(a[0]) + ',' + str(a[1]) + ')')
                E.append((a[0], a[1]))
        
        L=[G[0].dibujar().render('0')]
        
        for i in range(1,len(G)):
            L.append(G[i].resaltar_arista(E[i]).render(str(i)))
        
        L.append(G[-1].dibujar().render(str(len(G))))
        
        textos.append('Grafo final')

        g.pasoapaso(L, textos)
    
    else:
        
        while len(aristas)>0:

            a=aristas[0]
            g.añadir_arista(a[0], a[1])
            aristas.remove((a[0],a[1]))
            if len([i for i in g.ciclos() if len(i)>3])>0:
                g.borrar_arista(a[0], a[1])
        return g


# In[8]:


Constructivo(g, True)

