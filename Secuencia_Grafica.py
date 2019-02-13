from copy import copy, deepcopy
from IPython.display import SVG, display, Image
import graphviz as gv
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
import math
from grafos import *

#SECUENCIA GRÁFICA DE UN GRAFO

def Secuencia_Grafica(G):
    l=[i[1] for i in G.grados()]
    ll=deepcopy(l)
    ll.sort()
    ll.reverse()
    #print(ll)
    L=[deepcopy(ll)]
    parar=False
    while parar==False:
        maxi=ll[0];
        del(ll[0])
        for j in range(maxi):
            ll[j]=ll[j]-1
        ll.sort()
        ll.reverse()
        #print(ll)
        L=L+[deepcopy(ll)]
        #print(L)
        #Aqui compruebo si tengo que parar ya
        if -1 in ll:
            print('La secuencia no es grAfica')
            parar=True
        if len(set(ll))==1 and list(set(ll))[0]==0:
            print('La secuencia es grAfica')
            parar = True
    return L


def Secuencia_a_Grafo(lista1, explicado=False):

    def n_vert_aumentados(l1,l2):
        ldef=[]
        l1.sort()
        l2.sort()
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                ldef.append((l1[i], l2[i]))
        return ldef


# DE SECUENCIA GRÁFICA A GRAFO
    
# -----------------------------------------------



    def grados_inic(l):
        return [i-1 for i in l]




# -----------------------------------------------
    if explicado:
        
        lista=deepcopy(lista1)
        lista.reverse()
        print(lista)
        gg=Grafo()
        l_inicial=lista[0]
        G=[]
        ars=[]
        textos=['Grafo inicial']
        contador=0
        for i in range(len(l_inicial)):
            gg.añadir_vertice(contador)
            contador=contador+1

        g1=deepcopy(gg)
        G.append(g1)

        for i in range(len(lista)-1):
            l=lista[i]
            l1=lista[i+1]
            ldef=n_vert_aumentados(l,l1)
            
            gg.añadir_vertice(contador)
            mensaje='Añado el vértice ' + str(contador)
            textos.append(mensaje)
            
            g1=deepcopy(gg)
            G.append(g1)
            dic=gg.grados()
            
            mens=[]

            for j in range(len(ldef)):

                dic=gg.grados()
                grad_inic=ldef[j][0]
                k=0
                parar = False
                
                while parar == False:
                    if dic[k][1] == grad_inic and (dic[k][0],contador) not in gg.aristas:
                        gg.añadir_arista(dic[k][0],contador)
                        mensaje=(dic[k][0], contador)
                        mens.append(mensaje)
                        
                        parar = True
                    else:
                        k=k+1
                        
            ars.append(mens)            
            textos.append('Añado las aristas: ' + str(mens))
            g1=deepcopy(gg)
            G.append(g1)
            contador=contador+1
        
        L=[G[0].dibujar().render(str(0))]
        
        j=0
        for i in range(1,len(G)):
            if i%2!=0:
                L.append(G[i].resaltar_nodo(int(textos[i][-1])).render(str(i))) 
            else:
                L.append(G[i].resaltar_arista(ars[j]).render(str(i)))
                j=j+1

        gg.pasoapaso(L, textos)
            
        
    else:
        lista=deepcopy(lista1)
        lista.reverse()
        gg=Grafo()
        l_inicial=lista[0]
        contador=0
        
        for i in range(len(l_inicial)):
            gg.añadir_vertice(contador)
            contador=contador+1

        for i in range(len(lista)-1):
            
            l=lista[i]
            l1=lista[i+1]
            ldef=n_vert_aumentados(l,l1)
            gg.añadir_vertice(contador)
            dic=gg.grados()

            for j in range(len(ldef)):

                dic=gg.grados()
                grad_inic=ldef[j][0]
                k=0
                parar = False
                
                while parar == False:

                    if dic[k][1] == grad_inic and (dic[k][0],contador) not in gg.aristas:
                        gg.añadir_arista(dic[k][0],contador)
                        parar = True
                    else:
                        k=k+1
                        
            contador=contador+1
            
        return gg

