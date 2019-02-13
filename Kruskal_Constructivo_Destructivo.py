
# coding: utf-8

# In[1]:


from grafos import *


# In[2]:


g=Grafo()


# In[3]:


g.añadir_arista(1,2)
g.añadir_arista(1,3)
g.añadir_arista(3,2)
g.añadir_arista(3,4)
g.añadir_arista(3,5)


# In[4]:


g.ponderado([20,30,40, 25, 35])


# In[5]:


g.dibujar_ponderado()


# In[6]:


def Kruskal_Constructivo(gg, explicado=False):
    
    aristas=deepcopy(gg.aristas)
    pesos = [gg.dic_pesos[i] for i in aristas]
    g=Grafo()
    pesos_nuevos=[]
    
    if explicado==True:
        
        G=[gg]
        textos=['Grafo inicial']

        while len(aristas)>1:

            mini=min(pesos)
            pesos_nuevos.append(mini)

            a=aristas[pesos.index(mini)]

            g.añadir_arista(a[0], a[1])        
            aristas.remove((a[0],a[1]))
            pesos.remove(mini)

            if len([i for i in g.ciclos() if len(i)>3])>0:
                g.borrar_arista(a[0], a[1])
                pesos_nuevos.remove(mini)

            mensaje='Añado la arista ' + str((a[0], a[1]))
            textos.append(mensaje)

            g.ponderado(pesos_nuevos)
            g1=deepcopy(g)
            G.append(g1)

        L=[G[0].dibujar_ponderado().render('0')]

        for i in range(1,len(G)):
            L.append(G[i].resaltar_arista(G[i].aristas[-1]).render(str(i)))

        gg.pasoapaso(L, textos)
    
    else:
        
        while len(aristas)>1:

            mini=min(pesos)
            pesos_nuevos.append(mini)

            a=aristas[pesos.index(mini)]

            g.añadir_arista(a[0], a[1])        
            aristas.remove((a[0],a[1]))
            pesos.remove(mini)

            if len([i for i in g.ciclos() if len(i)>3])>0:
                g.borrar_arista(a[0], a[1])
                pesos_nuevos.remove(mini)

            g.ponderado(pesos_nuevos)
        
        return g
        
    


# In[7]:


Kruskal_Constructivo(g, True)


# In[8]:


def Kruskal_Destructivo(g, explicado=False):

    gg=deepcopy(g)
    pesos_nuevos=[]
    aristas=gg.aristas
    a_borradas=[]
    ciclos=[i for i in gg.ciclos() if len(i)>3]
    
    if explicado==True:
        
        G=[g, g]
        textos=['Grafo inicial']
        aristas_marcadas=[]

        # Primero cojo mi arista de mayor peso

        pesos=[gg.dic_pesos[i] for i in aristas]

        while len(ciclos)>0:

            maxi=max(pesos)
            a_candidata=aristas[pesos.index(maxi)]

            for i in ciclos:
                if i[0]==a_candidata[0]:
                    gg.borrar_arista(a_candidata[0], a_candidata[1])
                    a_borradas.append((a_candidata[0], a_candidata[1]))
                    break

            pesos.remove(maxi)
            ciclos=[i for i in gg.ciclos() if len(i)>3]

            gg.ponderado(pesos)  
            g1=deepcopy(gg)
            G.append(g1)
            mensaje='Borro la arista ' + str((a_candidata[0], a_candidata[1]))
            textos.append(mensaje)
            aristas_marcadas.append((a_candidata[0], a_candidata[1]))
        
        L=[G[0].dibujar_ponderado().render('0')]
        
        for i in range(1,len(G)-1):
            L.append(G[i].resaltar_arista(aristas_marcadas[i-1]).render(str(i)))
        
        L.append(G[-1].dibujar_ponderado().render(str(len(G))))
        textos.append('')

        gg.pasoapaso(L, textos)
    
    else:
        
        # Primero cojo mi arista de mayor peso

        pesos=[gg.dic_pesos[i] for i in aristas]

        while len(ciclos)>0:

            maxi=max(pesos)
            a_candidata=aristas[pesos.index(maxi)]

            for i in ciclos:
                if i[0]==a_candidata[0]:
                    gg.borrar_arista(a_candidata[0], a_candidata[1])
                    a_borradas.append((a_candidata[0], a_candidata[1]))
                    break

            pesos.remove(maxi)
            ciclos=[i for i in gg.ciclos() if len(i)>3]

            gg.ponderado(pesos)
            
        return gg   


# In[9]:


Kruskal_Destructivo(g, True)
