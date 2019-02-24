from grafos import *

def Kruskal_Constructivo(gg, explicado=False):
    
    aristas=deepcopy(gg.aristas)
    pesos = [gg.dic_pesos[i] for i in aristas]
    g=Grafo()
    pesos_nuevos=[]
    
    if explicado==True:
        
        textos=['Grafo inicial']
        E=[]

        while len(g.aristas) < len(gg.vertices)-1:

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
            E.append((a[0], a[1]))
            textos.append(mensaje)

            g.ponderado(pesos_nuevos)

        L=[gg.dibujar_ponderado('circo').render('0')]

        for i in range(1,len(textos)):
            L.append(gg.resaltar_arista(E[0:i], {}, 'red', '3', 'circo').render(str(i)))

        gg.pasoapaso(L, textos)
    
    else:
        
        while len(g.aristas) < len(gg.vertices)-1:

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
        
        L=[G[0].dibujar_ponderado('circo').render('0')]
        
        for i in range(1,len(G)-1):
            L.append(G[i].resaltar_arista(aristas_marcadas[i-1],{},'red','3','circo').render(str(i)))
        
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

