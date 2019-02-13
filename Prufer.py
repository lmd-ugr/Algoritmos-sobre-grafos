
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
from grafos import *


# In[14]:


g=Grafo()


# In[15]:


g.añadir_arista(2,3)
g.añadir_arista(1,2)
g.añadir_arista(2,4)
g.añadir_arista(2,5)


# In[16]:


g.dibujar('neato')


# In[21]:


def Codigo_Prufer(g1, explicado=False):    
    
    g=deepcopy(g1)
    gg=deepcopy(g)
    
    #Primero compruebo que es un árbol
    
    if g.es_arbol()==False:
        return 0
    else:
        if explicado:
            
            G=[] # Aquí guardo los grafos que voy obteniendo
            
            P=[]
            
            PP=[] # Aqui guardo los distintos pasos de creacion de P
            
            nodos_borrados=[]
            
            textos=[]

            while len(g.vertices)>2:

                #Busco el nodo de menor etiqueta con grado 1

                n = [i for i in g.vertices if g.grado(i)==1]
                n.sort()
                borrar_nodo=n[0]


                # Veo cual es su arista incidente y cojo el otro extremo

                borrar_arista = g.aristas_incidentes(borrar_nodo)[0]


                if borrar_arista[0] == borrar_nodo:
                    añadir_nodo = borrar_arista[1]
                else:
                    añadir_nodo = borrar_arista[0]



                # Ahora añado ese nodo al codigo Prufer P y borro el vertice del grafo

                P.append(añadir_nodo)
                
                p=deepcopy(P)
                
                PP.append(p)
                
                nodos_borrados.append(borrar_nodo)
                
                mensaje= 'Borramos el nodo ' + str(borrar_nodo) + ' y añadimos a P su nodo adyacente, ' + str(g.vecinos(borrar_nodo)[0]) 
                
                textos.append(mensaje)

                gg=deepcopy(g)

                G.append(gg)
                
                g.borrar_vertice(borrar_nodo)
            
            PP.append(p)
            
            textos.append('Grafo final')
            
            gg=deepcopy(g)

            G.append(gg)
            
            L=[]

            for i in range(len(G)-1):
                L.append(G[i].resaltar_nodo(nodos_borrados[i]).render(str(i)))
            
            L.append(G[-1].dibujar().render(str(len(G))))
                
            g.pasoapaso(L, textos, PP)
            
            return P
        
        else:
            
            P=[]

            while len(g.vertices)>2:

                #Busco el nodo de menor etiqueta con grado 1

                n = [i for i in g.vertices if g.grado(i)==1]
                n.sort()
                borrar_nodo=n[0]

                # Veo cual es su arista incidente y cojo el otro extremo

                borrar_arista = g.aristas_incidentes(borrar_nodo)[0]


                if borrar_arista[0] == borrar_nodo:
                    añadir_nodo = borrar_arista[1]
                else:
                    añadir_nodo = borrar_arista[0]



                # Ahora añado ese nodo al codigo Prufer P y borro el vertice del grafo

                P.append(añadir_nodo)


                g.borrar_vertice(borrar_nodo)
            

            # if explicado:
            #     pasoapaso(G) o la que sea donde has guardado texto + imagen
            return P # return solo P


# In[22]:


P=Codigo_Prufer(g, True)


# In[23]:


def Prufer_a_Arbol(P1, explicado=False):
    
    P=deepcopy(P1)
    g=Grafo()
    
    if explicado:
        
        G=[] #Aquí guardo los grafos que voy formando
        
        textos=[]
        
        aristas_añadidas=[]

        vertices=[i+1 for i in range(len(P)+2)]
        
        p2=deepcopy(P)
        v=deepcopy(vertices)
        PP=[(p2, v)]

        # Parto del grafo vacío de n vértices

        for i in vertices:
            g.añadir_vertice(str(i))

        gg=deepcopy(g)
        G.append(gg)
        textos.append('Grafo de partida')

        while len(P)>0:
            borrar_nodo=[i for i in vertices if i not in P][0]
            g.añadir_arista(borrar_nodo, P[0])
            aristas_añadidas.append((borrar_nodo, P[0]))
            
            mensaje='Añadimos la arista (' + str(borrar_nodo) + ',' + str(P[0]) + ')'
            textos.append(mensaje)
            
            gg=deepcopy(g)
            G.append(gg)

            vertices.remove(borrar_nodo)
            P.remove(P[0])
            
            p2=deepcopy(P)
            v=deepcopy(vertices)
            PP.append((p2, v))

        g.añadir_arista(vertices[0], vertices[1])
        aristas_añadidas.append((vertices[0], vertices[1]))
        
        mensaje='Añadimos la arista (' + str(vertices[0]) + ',' + str(vertices[1]) + ')'
        textos.append(mensaje)

        gg=deepcopy(g)
        G.append(gg)
        
        PP.append('Grafo final')

        L=[G[0].dibujar().render(str(0))]

        for i in range(1,len(G)-1):
            L.append(G[i].resaltar_arista(aristas_añadidas[i-1]).render(str(i)))

        L.append(G[-1].dibujar().render(str(len(G))))

        g.pasoapaso(L, textos, PP)
    
    else:
        
        vertices=[i+1 for i in range(len(P)+2)]

        # Parto del grafo vacío de n vértices

        for i in vertices:
            g.añadir_vertice(str(i))

        while len(P)>0:
            borrar_nodo=[i for i in vertices if i not in P][0]
            g.añadir_arista(borrar_nodo, P[0])

            vertices.remove(borrar_nodo)
            P.remove(P[0])

        g.añadir_arista(vertices[0], vertices[1])
        
        return g
        


# In[24]:


Prufer_a_Arbol(P, True);

