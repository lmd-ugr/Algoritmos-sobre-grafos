from grafos import *

# DE CÓDIGO PRUFER A ÁRBOL              
        
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
 
