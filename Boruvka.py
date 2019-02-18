from grafos import *

def Boruvka(g, explicado=False):
    
    pesos=[g.dic_pesos[i] for i in g.aristas]
    pesosord=deepcopy(pesos); pesosord.sort()
    aristas_G=deepcopy(g.aristas)
    vertices_G=deepcopy(g.vertices)
    T=Grafo()
    pes=[]
    
    if explicado==True:
    
        G=[]
        textos=[]

        for v in vertices_G:
            if v not in T.vertices:
    
                aristas_ady=g.aristas_incidentes(v)
                aristas_candid=[i for i in aristas_ady if i not in T.aristas]
                pesos_candid=[pesos[aristas_G.index(i)] for i in aristas_candid]
                mini=min(pesos_candid)
                pes.append(mini)
                arista_def=aristas_candid[pesos_candid.index(mini)]
                T.añadir_arista_ponderada(arista_def[0],arista_def[1],g.dic_pesos[(arista_def[0],arista_def[1])])
                mensaje='Añado la arista ' + str((arista_def[0],arista_def[1]))
                textos.append(mensaje)
                gg=deepcopy(T)
                G.append(gg)
                

        # hago que las componentes conexas sean conjuntos para luego comprobar si una arista esta en una comp conexa

        comp_conex=[]
        for i in T.componentes_conexas():
            comp_conex.append(set(i))

        #Ahora cojo todas las aristas que no estén en mi árbol y me quedo con sus pesos

        aristas_conex=[i for i in aristas_G if i not in T.aristas]
        pesos_conex=[g.dic_pesos[i] for i in aristas_conex]
        
        while len(T.componentes_conexas()) >1:

            # Ahora cojo la arista de menor peso y pregunto, si no forma ciclo (que es lo mismo que estar en la misma comp conexa),
            # la añado

            mini=min(pesos_conex)

            candidata = aristas_conex[pesos_conex.index(mini)]; 
            aristas_conex.remove(candidata)
            pesos_conex.remove(mini)

            i=0

            while i < len(comp_conex):

                if candidata[0] in comp_conex[i]:
                    if candidata[1] in comp_conex[i]:
                        i=len(comp_conex) + 1
                    else:
                        T.añadir_arista_ponderada(candidata[0], candidata[1], g.dic_pesos[(candidata[0], candidata[1])])
                        pes.append(mini)
                        mensaje='Añado la arista ' + str((candidata[0], candidata[1]))
                        textos.append(mensaje)
                        gg=deepcopy(T)
                        G.append(gg)
                        i=len(comp_conex) + 1
                else:
                    i=i+1


            comp_conex=[]
            for i in T.componentes_conexas():
                comp_conex.append(set(i))
        
        L=[]

        for i in range(len(G)):
            L.append(G[i].resaltar_arista(G[i].aristas[-1]).render(str(i)))
        
        T.pasoapaso(L, textos)
        
    else:
        
        for v in vertices_G:
            if v not in T.vertices:
    
                aristas_ady=g.aristas_incidentes(v)
                aristas_candid=[i for i in aristas_ady if i not in T.aristas]
                pesos_candid=[pesos[aristas_G.index(i)] for i in aristas_candid]
                mini=min(pesos_candid)
                arista_def=aristas_candid[pesos_candid.index(mini)]
                pes.append(mini)
                T.añadir_arista(arista_def[0],arista_def[1])  
            
        # hago que las componentes conexas sean conjuntos para luego comprobar si una arista esta en una comp conexa

        comp_conex=[]
        for i in T.componentes_conexas():
            comp_conex.append(set(i))

        #Ahora cojo todas las aristas que no estén en mi árbol y me quedo con sus pesos

        aristas_conex=[i for i in aristas_G if i not in T.aristas]
        pesos_conex=[g.dic_pesos[i] for i in aristas_conex]
        
        while len(T.componentes_conexas()) >1:

            # Ahora cojo la arista de menor peso y pregunto, si no forma ciclo (que es lo mismo que estar en la misma comp conexa),
            # la añado

            mini=min(pesos_conex)

            candidata = aristas_conex[pesos_conex.index(mini)]; 
            aristas_conex.remove(candidata)
            pesos_conex.remove(mini)

            i=0

            while i < len(comp_conex):

                if candidata[0] in comp_conex[i]:
                    if candidata[1] in comp_conex[i]:
                        i=len(comp_conex) + 1
                    else:
                        T.añadir_arista(candidata[0], candidata[1])
                        pes.append(mini)
                        i=len(comp_conex) + 1
                else:
                    i=i+1


            comp_conex=[]
            for i in T.componentes_conexas():
                comp_conex.append(set(i))
                
        T.ponderado(pes)
        
        return T
