from grafos import *

def Prim(g, explicado=False):
    
    if explicado==True:
        
        G=[]
        textos=['Grafo inicial']

        #Primero escojo la arista de menor peso y un vértice suyo, será mi vértice inicial

        aristas=deepcopy(g.aristas)
        pesos=[g.dic_pesos[i] for i in aristas]

        mini=min(pesos)
        a_a=aristas[pesos.index(mini)]  # arista actual

        # v_a va siendo el vértice siguiente de la arista escogida y voy borrando las aristas seleccionadas, preguntando antes si forman
        # ciclos.


        gg=Grafo()
        V=[]
        A=[]

        gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
        mensaje='Añado la arista ' + str((a_a[0], a_a[1]))
        textos.append(mensaje)
        g1=deepcopy(gg)
        G.append(g1)
        aristas.remove(a_a)
        pesos.remove(mini)

        V.append(a_a[0])
        V.append(a_a[1])

        # Ahora, de las aristas incidentes en los vértices que ya he marcado, cojo la de menor peso.

        while len(gg.aristas) < (len(g.vertices)-1):

            a=[]
            for i in V:
                ll=[j for j in g.aristas_incidentes(i) if j in aristas]
                for k in ll:
                    if k not in a:
                        a.append(k)

            pesos_actuales= [g.dic_pesos[i] for i in a]
            mini=min(pesos_actuales)

            for i in a:
                if g.dic_pesos[i]==mini:
                    a_a=i
                    break

            gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
            aristas.remove(a_a)
            pesos.remove(mini)


            l=[i for i in gg.ciclos() if len(i)>3]


            if len(l)>0:
                mensaje='Escogeríamos la arista ' + str((a_a[0], a_a[1])) + ' pero forma un ciclo, así que, la eliminamos.'
                textos.append(mensaje)
                g1=deepcopy(gg)
                G.append(g1)
                gg.borrar_arista(a_a[0], a_a[1])

            else:
                mensaje='Añado la arista ' + str((a_a[0], a_a[1]))
                textos.append(mensaje)
                g1=deepcopy(gg)
                G.append(g1)
                V.append(a_a[0])
                V.append(a_a[1])

        g2=deepcopy(g)
        L=[g2.dibujar_ponderado('circo').render('0')]

        for i in range(len(G)):
            g2=deepcopy(g)
            L.append(g2.resaltar_arista(G[i].aristas, {}, 'red', '3', 'circo').render(str(i+1)))

        gg.pasoapaso(L, textos)

    else:
        
        #Primero escojo la arista de menor peso y un vértice suyo, será mi vértice inicial

        aristas=deepcopy(g.aristas)
        pesos=[g.dic_pesos[i] for i in aristas]

        mini=min(pesos)
        a_a=aristas[pesos.index(mini)]  # arista actual

        # v_a va siendo el vértice siguiente de la arista escogida y voy borrando las aristas seleccionadas, preguntando antes si forman
        # ciclos.


        gg=Grafo()
        V=[]
        A=[]

        gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
        aristas.remove(a_a)
        pesos.remove(mini)

        V.append(a_a[0])
        V.append(a_a[1])

        # Ahora, de las aristas incidentes en los vértices que ya he marcado, cojo la de menor peso.

        while len(gg.aristas) < (len(g.vertices)-1):

            a=[]
            for i in V:
                ll=[j for j in g.aristas_incidentes(i) if j in aristas]
                for k in ll:
                    if k not in a:
                        a.append(k)

            pesos_actuales= [g.dic_pesos[i] for i in a]
            mini=min(pesos_actuales)

            for i in a:
                if g.dic_pesos[i]==mini:
                    a_a=i
                    break

            gg.añadir_arista_ponderada(a_a[0], a_a[1], mini)
            aristas.remove(a_a)
            pesos.remove(mini)


            l=[i for i in gg.ciclos() if len(i)>3]


            if len(l)>0:
                gg.borrar_arista(a_a[0], a_a[1])

            else:
                V.append(a_a[0])
                V.append(a_a[1])
        
        return gg
