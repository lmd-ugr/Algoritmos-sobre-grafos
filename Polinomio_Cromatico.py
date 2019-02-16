from grafos import*
from sympy import *
x=Symbol("x")

# Forma Iterativa 

def Polinomio_Cromatico_Iterativo(g):
    
    def descomponer(L1, L2, long_ant_1, long_ant_2): # Las longitudes anteriores me sirven para saber qué elemento empiezo a estudiar 
    
        arboles_L1=0
        arboles_L2=0
        L1_copia=deepcopy(L1)
        L2_copia=deepcopy(L2)

        for i in range(long_ant_1, len(L1_copia)):

            # Si el elemento elegido no es un árbol, lo trabajo. Si lo fuera, no lo toco.

            if L1_copia[i].es_arbol()==False:

                print('Descompongo el elemento de L1: ', i)

                # Elemento de L1, entonces el grafo resultante al borrar arista va a L1, el resultante de identificar, a L2

                g1=deepcopy(L1[i])
                g2=deepcopy(L1[i])

                if (g1.ciclos(3)[0][0], g1.ciclos(3)[0][1]) in g1.aristas:
                    e=(g1.ciclos(3)[0][0], g1.ciclos(3)[0][1]) # arista a borrar
                else:
                    e=(g1.ciclos(3)[0][1], g1.ciclos(3)[0][0])

                # Por un lado, g1 será el grafo sin e y g2 el grafo con los vertices de e identificados

                g1.borrar_arista(e[0], e[1])
                #Una vez borrada, elimino los vértices aislados que puedan quedar
                for i in g1.vertices_aislados():
                    g1.borrar_vertice(i)

                gg=deepcopy(g1)
                if gg.es_arbol()==False:
                    arboles_L1=arboles_L1+1
                L1.append(gg)

                g2.identificar_vertices(e[0], e[1])
                gg=deepcopy(g2)

                # Si el grafo añadido es un árbol, lo cuento.

                if gg.es_arbol()==False:
                    arboles_L2=arboles_L2+1
                L2.append(gg)

        for i in range(long_ant_2, len(L2_copia)):

            if L2_copia[i].es_arbol()==False:

                print('Descompongo el elemento de L2: ', i)

                # Elemento de L2, entonces cambio las listas de destino de la descomposicion de mis grafos

                g1=deepcopy(L2[i])
                g2=deepcopy(L2[i])

                if (g1.ciclos(3)[0][0], g1.ciclos(3)[0][1]) in g1.aristas:
                    e=(g1.ciclos(3)[0][0], g1.ciclos(3)[0][1]) # arista a borrar
                else:
                    e=(g1.ciclos(3)[0][1], g1.ciclos(3)[0][0])

                # Por un lado, g1 será el grafo sin e y g2 el grafo con los vertices de e identificados

                g1.borrar_arista(e[0], e[1])
                #Una vez borrada, elimino los vértices aislados que puedan quedar
                for i in g1.vertices_aislados():
                    g1.borrar_vertice(i)

                gg=deepcopy(g1)
                if gg.es_arbol()==False:
                    arboles_L2=arboles_L2+1
                L2.append(gg)

                g2.identificar_vertices(e[0], e[1])
                gg=deepcopy(g2)
                if gg.es_arbol()==False:
                    arboles_L1=arboles_L1+1
                L1.append(gg)

        # He ido comprobando todos los grafos nuevos añadidos a L1 y L2, si he visto que todo son árboles, retorno True para terminar 
        # el proceso en la funcion POlinomio_Cromatico

        print(arboles_L1,arboles_L2)
        if arboles_L1==0 and arboles_L2==0:
            return [L1,L2, len(L1_copia), len(L2_copia), True]
        else:
            return [L1, L2, len(L1_copia), len(L2_copia), False]
    
    
    
    # ----------------------------------------------------------------------------------------

    
    n=len(g.vertices)
    pol=0

    # Primero compruebo que no sea completo ni árbol

    if g.es_arbol():
        return x*(x-1)**(n-1)
    
    else:

        # Aquí empiezo a reducir mi grafo hasta conseguir árboles
        # Cada vez que haga una iteracion, guardare los grafos resultantes en dos listas, una que sumara y otra que restara 
        # para el polinomio cromatico

        L1=[] # lista de grafos que suman
        L2=[] # lista de grafos que restan
        pols=[] # lista de polinomios cromaticos
        
        # La función dividir, me coge dos listas y un numero, iteracion: iteracion indica que cantidad de grafos debo romper de 
        #  cada lista. iteracion-1 es donde está el primer grafo que debo romper, los demás son sus siguientes. Además, f, si 
        # coge un grafo de L1, mandará ese grafo sin arista a L1 y el grafo con dicha arista identificada a L2.

        g1=deepcopy(g)
        g2=deepcopy(g)
        
        if (g1.ciclos(3)[0][0], g1.ciclos(3)[0][1]) in g1.aristas:
            e=(g1.ciclos(3)[0][0], g1.ciclos(3)[0][1]) # arista a borrar
        else:
            e=(g1.ciclos(3)[0][1], g1.ciclos(3)[0][0])
        
        # Por un lado, g1 será el grafo sin e y g2 el grafo con los vertices de e identificados
        
        g1.borrar_arista(e[0], e[1])
        #Una vez borrada, elimino los vértices aislados que puedan quedar
        for i in g1.vertices_aislados():
            g1.borrar_vertice(i)
        gg=deepcopy(g1)
        L1.append(gg)
        
        g2.identificar_vertices(e[0], e[1])
        gg=deepcopy(g2)
        L2.append(gg)
        
        
        
        H=descomponer(L1,L2,0,0)
        
        while H[4]==False:
            
            HH=descomponer(H[0], H[1], H[2], H[3])
            H=deepcopy(HH)
        
        
        for i in L1:
            if i.es_arbol():
                n=len(i.vertices)
                pol=pol + (x*(x-1)**(n-1))
                
        for i in L2:
            if i.es_arbol():
                n=len(i.vertices)
                pol=pol - (x*(x-1)**(n-1))
                
        
        return pol

    
    
    
# Forma Recursiva ---------------------------------------------------------------------------    


def Polinomio_Cromatico_Recursivo(G):
    
    lados=G.aristas
    
    if len(lados)==0:
        return x**len(G.vertices)
    
    l=lados[0]
    
    Gl=deepcopy(G)
    Gl.borrar_arista(l[0], l[1])
    
    Glp=deepcopy(G)
    Glp.identificar_vertices(l[0],l[1])
    return polcrom(Gl)-polcrom(Glp)
