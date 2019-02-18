from copy import copy, deepcopy
from IPython.display import SVG, display, Image
import graphviz as gv
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
import math

class Grafo(object):
    
    def __init__(self, verts=[], aris=[]):   
        self.vertices=copy(verts)
        if len(aris)==0:
            self.aristas=[]
        else:
            self.aristas=copy(aris)
            for i in aris:
                for j in i:
                    if j not in self.vertices:
                        self.vertices.append(j)
        self.dic_pesos={}

    def __repr__(self):  
        return str("Grafo con "+str(len(self.vertices))+" vertices y "+str(len(self.aristas))+" lados")    

    def __str__(self):
        return str("Grafo con vertices "+str(self.vertices)+" y lados "+str(self.aristas))    

    def dibujar(self, motor='dot'):
        
        g=gv.Graph(format='svg', engine=motor)
        g.attr('node', shape='circle')
        g.attr('node', style='filled')

        for i in self.aristas:
            g.edge(str(i[0]), str(i[1]))
        
        for i in self.vertices_aislados():
            g.node(str(i))
            
        return g
    
    def dibujar_ponderado(self, motor='dot'):
        
        g=gv.Graph(format='svg', engine=motor)
        g.attr('node', shape='circle')
        g.attr('node', style='filled')

        for i in self.aristas:
            g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
        
        for i in self.vertices_aislados():
            g.node(str(i))
            
        return g

    def resaltar_arista(self, arista, pesos_nuevos={}, acolor='red', anchura='3', motor='neato'):
        
        arist=deepcopy(self.aristas)
        p=pesos_nuevos

        g=gv.Graph(format='svg', engine=motor)
        g.attr('node', shape='circle')
        g.attr('node', style='filled')

        if type(arista)==list:
            l1=[]
            l2=[]
            pl2=[]

            for i in arista:
                if i in arist or (i[1], i[0]) in arist:
                    l1.append(i)
                else:
                    l2.append(i)
                    if len(p)!=0:
                        pl2.append(p[i]) #Guardo el peso de la nueva arista que quiero añadir

            l3=[i for i in arist if i not in l1 and (i[1], i[0]) not in l1]

            if len(self.dic_pesos)==0:
                for i in l3:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l3:
                    if i in self.dic_pesos:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                    else:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[(i[1], i[0])]))


            g.attr('edge', color=acolor, penwidth=anchura)

            if len(self.dic_pesos)==0:
                for i in l1:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l1:
                    if i in self.dic_pesos:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                    else:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[(i[1], i[0])]))
                        
            if len(p)==0:
                for i in l2:
                    g.edge(str(i[0]), str(i[1]))
            else:
                for i in l2:
                    g.edge(str(i[0]), str(i[1]), str(p[i]))

        else:
            if arista not in arist and (arista[1], arista[0]) not in arist:
                if len(self.dic_pesos)==0:
                    for i in arist:
                        g.edge(str(i[0]), str(i[1]))
                else:
                    for i in arist:
                        g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                
                for i in self.vertices_aislados():
                    g.node(str(i))

                g.attr('edge', color=acolor, penwidth=anchura)
                if len(p)==0:
                    g.edge(str(arista[0]), str(arista[1]))
                else:
                    g.edge(str(arista[0]), str(arista[1]), str(p[arista]))


            else:
                if arista in arist:
                    arist.remove(arista)

                    if len(self.dic_pesos)==0:
                        for i in arist:
                            g.edge(str(i[0]), str(i[1]))
                    else:
                        for i in arist:
                            g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                
                    for i in self.vertices_aislados():
                        g.node(str(i))

                    g.attr('edge', color=acolor, penwidth=anchura)

                    if len(self.dic_pesos)==0:
                        g.edge(str(arista[0]), str(arista[1]))
                    else:
                        g.edge(str(arista[0]), str(arista[1]), str(self.dic_pesos[arista]))
                
                else:
                    arist.remove((arista[1], arista[0]))

                    if len(self.dic_pesos)==0:
                        for i in arist:
                            g.edge(str(i[0]), str(i[1]))
                    else:
                        for i in arist:
                            g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))
                
                    for i in self.vertices_aislados():
                        g.node(str(i))

                    g.attr('edge', color=acolor, penwidth=anchura)

                    if len(self.dic_pesos)==0:
                        g.edge(str(arista[0]), str(arista[1]))
                    else:
                        g.edge(str(arista[0]), str(arista[1]),str(self.dic_pesos[(arista[1], arista[0])]))

        return g

    def resaltar_nodo(self, nodo, ncolor='red', motor='neato'):
    
        g=gv.Graph(format='svg', engine=motor)
        g.attr('node', shape='circle')

        if type(nodo)==list:
            for i in nodo:
                g.node(str(i), style='filled', color=ncolor)
        else:
            g.node(str(nodo), style='filled', color=ncolor)

        g.attr('node', style='filled')

        if len(self.dic_pesos)==0:
            for i in self.aristas:
                g.edge(str(i[0]), str(i[1]))
        else:
            for i in self.aristas:
                g.edge(str(i[0]), str(i[1]), str(self.dic_pesos[i]))

        
        for i in self.vertices_aislados():
            g.node(str(i))

        
        return g

    def añadir_vertice(self, v):             # Me faltaría dar la lista de vertices y aristas ordenadas, cada vez que las toque
        if int(v) in self.vertices:
            return False
        else:
            self.vertices.append(int(v))
    
    def añadir_arista(self, u, v):  
        self.aristas.append((u,v))
    
        if u not in self.vertices:# Quiero que, si añado una arista creando vértices que no están en mi grafo, se añadan
            self.vertices.append(u)   # estos vértices a mi conjunto de vértices. 
        if v not in self.vertices:
            self.vertices.append(v)
    
    def añadir_arista_ponderada(self, u, v, peso):  # Añado arista y añado a dic_pesos tambien
        self.añadir_arista(u, v)
        self.dic_pesos[(u,v)]=peso
        
    def ponderado(self, pesos=[]):   # esta funcion me transforma mi grafo en poderado iniciando los pesos
                                             # a la lista de pesos que me den como argumento o a 0 en su defecto.
        if len(self.aristas) != len(pesos):
            print('Longitudes de aristas y pesos distintas.')
        else:
            for i in self.aristas:
                self.dic_pesos[i]=pesos[self.aristas.index(i)]
        return self.dic_pesos   # ME FALTA SABER CÓMO GUARDAR LOS PESOS COMO UN VARIABLE, PARA PODER PONER
                                # g.pesos  Y QUE ME LOS DEVUELVA
    
    def modificar_peso(self, arista, nuevo_peso):
        if arista not in self.aristas:
            print('La arista no esta en el grafo')
        else:
            self.dic_pesos[arista]=nuevo_peso
    
    def borrar_vertice(self, v):
        if v in self.vertices:
            self.vertices.remove(v) #Borro también todas las aristas adyacentes a v
            for i in self.aristas_incidentes(v):
                self.aristas.remove(i)
                del(self.dic_pesos[i])
        else:
            return False
        
    def borrar_arista(self, u, v):
        if (u,v) in self.aristas:
            self.aristas.remove((u,v))
            if (u,v) in self.dic_pesos:
                del(self.dic_pesos[(u,v)])
        elif (v,u) in self.aristas:
            self.aristas.remove((v,u))
            if (v,u) in self.dic_pesos:
                del(self.dic_pesos[(v,u)])
        else:
            return False
    
    def aristas_incidentes(self, v):
        aristas_incidentes=[i for i in self.aristas if v in i]
        return aristas_incidentes
    
    def identificar_vertices(self,a,b):
        
        if self.grado(a) >= self.grado(b):
            v_eliminado=b
            v=a
        else:
            v_eliminado=a
            v=b

        # reescribo las aristas
        a_nuevas=[]
        for i in self.aristas_incidentes(v_eliminado):
            if i[0]==v_eliminado:
                a_nuevas.append((v,i[1]))
            else:
                a_nuevas.append((i[0],v))    

        # elimino mi vértice 3 y añado las nuevas aristas siempre que no sean lazos
        self.borrar_vertice(v_eliminado)

        for i in a_nuevas:
            if i[0]!=i[1]:
                if i not in self.aristas and (i[1], i[0]) not in self.aristas:
                    self.añadir_arista(i[0], i[1])
                    

    def vecinos(self, v):     
        l=self.aristas_incidentes(v) 
        lista_vecinos=[]
        for i in l:
            if i[0] == v:
                lista_vecinos.append(i[1])
            else:
                lista_vecinos.append(i[0])
                
        return lista_vecinos
   

    def vertices_aislados(self):    # Devuelvo los vertices aislados, los que su grado es 0.
        l=[]
        
        for i in self.vertices:
            if self.grado(i)==0:
                l.append(i)
        
        return l
            
    def componentes_conexas(self): 

        self.comp_conexas=[]
        c=[]
        v=deepcopy(self.vertices)
        a=deepcopy(self.aristas)

        # Primero quitamos vertices aislados

        for i in self.vertices_aislados():
            self.comp_conexas.append([i])
            v.remove(i)
        
        while len(v)>0:

            v_a=v[0]
            c=[v_a]
            parar=False

            while parar==False:
                for i in c:
                    l=[k for k in self.aristas_incidentes(i) if k in a]
                    if len(l)==0:
                        parar=True
                    else:
                        for j in l:
                            if j[0]==i:
                                if j[1] not in c:
                                    c.append(j[1])
                            else:
                                if j[0] not in c:
                                    c.append(j[0])
                            a.remove(j)
            self.comp_conexas.append(c)
            for i in c:
                v.remove(i)
            c=[]

        return self.comp_conexas
    
    def conexo(self):    # Devuelvo true o false segun haya una o mas comp. conexas.
        
        l=self.componentes_conexas()
        
        if len(l)==1:
            return True
        else:
            return False
        
    def grado(self,v):    # Devuelvo un entero, el grado del vertice que se mete como argumento.
        
        if v not in self.vertices:
            return False
        else:
            l=self.aristas_incidentes(v) #numero de aristas incidentes, contando los lazos una sola vez, por lo que hay que
            gr=len(l)                          # incrementar en 1 por cada lazo
            
            laz = self.lazos()
            n = laz[self.vertices.index(v)][1]
            
            for i in range(n):
                gr=gr+1
            return gr
    
    def lazos(self):    # Devuelvo una lista de 2-uplas, (vertice, número de lazos de ese vertice)
        
        l = self.vertices
        a=deepcopy(self.aristas)
        lazos=[]
        
        for i in l:
            contador=0
            while (i,i) in a:
                contador = contador + 1   #cuento el número de lazos que tiene cada vertice
                a.remove((i,i))
            
            lazos.append((i, contador))
            
        return lazos
    
    def grados(self):    # Devuelvo una lista de 2-uplas, el vertice y su grado, ordenadas las uplas en el orden en que estan los
        l=[]            # vertices en self.vertices
        
        for i in self.vertices:
            l.append((i,self.grado(i)))
    
        return l
    
    def es_euleriano(self):     # digo si un grafo es euleriano o si tiene un camino de euler.
        
        if self.conexo()==False:
            return 0
        
        else:
            
            l = [i[1] for i in self.grados() if i[1]%2==0]
            
            if len(l)==len(self.grados()):
                return 1
            elif len(l)==len(self.grados())-2:
                return 2
            else:
                return 0
    
    def caminos_simples(self, v_inic, v_f):
        
        def auxiliar(v_f,c_actual,v_usados,caminos):
            v_actual = c_actual[-1]
            if v_actual == v_f:
                caminos.append(list(c_actual))
            else:
                for i in self.vecinos(v_actual):
                    if i not in v_usados:
                        c_actual.append(i)
                        v_usados.append(i)
                        auxiliar(v_f,c_actual,v_usados,caminos)
                        v_usados.remove(i)
                        c_actual.pop()
            return caminos
        
        return auxiliar(v_f,[v_inic],[v_inic],[])
    
    def ciclos(self, longitud=-1):
        L=[]         
        for i in self.vertices:
            for j in self.vecinos(i):
                l=self.caminos_simples(j, i)
                for k in l:
                    k.insert(0,i)
                    L.append(k)
        
        if longitud!=-1:
            L1=[i for i in L if len(i)>longitud]
            return L1
        else:
            return L
    
    def es_arbol(self):   #Ver que el tamaño es n-1 siendo n el orden
        
        if self.conexo() and len(self.aristas)==len(self.vertices)-1:
            return True
        else:
            return False

    def es_completo(self):
        grados=[i[1] for i in self.grados()]

        if len(set(grados))==1:
            return True
        else:
            return False
    
    def pasoapaso(self, lg, lt, cd=''):
        
        def plot(d=0):
            if cd == '':
                cod=['' for i in range(len(lg))]
            else:
                cod=cd            
            print(lt[d]) # mostrar algún mensaje
            
            if type(lg[d])==str:
                display(SVG(lg[d]))
            elif type(lg[d])==list:
                print(lg[d])
            else:
                print(lg[d])
            print(cod[d])
        
        interact(plot,d=IntSlider(min=0,max=len(lg)-1,step=1,value=0))

    def Prufer(self):
        P=[]
        g=deepcopy(self)

        if g.es_arbol()==False:
            return ValueError, 'El grafo NO es un árbol.'

        else:

            while len(g.vertices)>2:

                #Busco el nodo de menor etiqueta con grado 1

                n = [i for i in g.vertices if g.grado(i)==1]
                n.sort()
                print('n= ', n)
                borrar_nodo=n[0]
                print('n[0]= ', borrar_nodo)

                # Veo cual es su arista incidente y cojo el otro extremo

                borrar_arista = g.aristas_incidentes(borrar_nodo)[0]
                print('borrar arista= ', borrar_arista)


                if borrar_arista[0] == borrar_nodo:
                    añadir_nodo = borrar_arista[1]
                else:
                    añadir_nodo = borrar_arista[0]
                print('nodo añadido= ', añadir_nodo)

                # Ahora añado ese nodo al codigo Prufer P y borro el vertice del grafo

                P.append(añadir_nodo)
                print('P= ', P)

                print('vertices= ', g.vertices)


                g.borrar_vertice(borrar_nodo)


            return P
    
    def Secuencia_a_Grafo(self, lista):
    
        # Primero comprobamos que la lista introducida es una secuencia grafica 

        def Secuencia_Grafica(l):

            # ll guarda los grados de la sucesion grafica, el elemento 'i' de 'll', será el grado del vértice 'i' de 'verts    
            ll=deepcopy(l)

            if -1 in ll:
                return 0
                parar=True
            if len(set(ll))==1 and list(set(ll))[0]==0:
                print('La secuencia es grAfica')
                parar = True
            
            # Creo una lista 'verts' con las etiquetas que tendrán mis vértices en caso de ser una secuencia grafica.
            
            verts=[i+1 for i in range(len(l))]
            vertices_borrados=[]
            
            # En L guardaré mi secuencia de listas
            # En V guardaré las secuencias de vértices degradados, para luego reconstruir el grafo

            L=[deepcopy(ll)]
            V=[]
            parar=False
            
            while parar==False:
                maxi=max(ll)
                v_max=verts[ll.index(maxi)]
                vertices_borrados.append(v_max)
                ll.remove(maxi)
                verts.remove(v_max)
                
                # Creo una lista, pos, de posiciones y otra, val, de valores. En pos guardo las posiciones de los grados que reduzco,
                # para saber a qué vertices corresponden. En val guardo los valores-1 de los grados reducidos, porque los voy a sustituir
                # por 0 en ll temporalmente para poder ir buscando los sucesivos máximos de ll, para bajarles un grado.
                # Creo tambien una lista de vértices degradados para que, en la reconstrucción del grafo, sepa quien se unia con quien
                
                pos=[]
                vals=[]
                v_degradados=[]
                
                for i in range(maxi):
                    max2=max(ll)
                    vals.append(max2-1)         # Le tenemos que bajar un grado
                    pos.append(ll.index(max2))
                    ll[ll.index(max2)]=0
                
                for i in range(maxi):
                    ll[pos[i]]=vals[i]
                    v_degradados.append(verts[pos[i]])
                

                L=L+[deepcopy(ll)]
                V.append(deepcopy(v_degradados))
                
                #Aqui compruebo si tengo que parar ya
                if -1 in ll:
                    parar=True
                    return 0
                if len(set(ll))==1 and list(set(ll))[0]==0:
                    print('La secuencia es grAfica')
                    parar = True
                    return [L, V, vertices_borrados]
            
            
        listas=Secuencia_Grafica(lista)

        if listas!=0:

            gg=Grafo()
            
            # Primero vemos cuántos vértices hay y los que se han quedado sin eliminar, pues serán el punto de partida

            n=len(listas[0][0])
            for i in range(1,n+1):
                if i not in listas[2]:
                    gg.añadir_vertice(i)

            while len(listas[1])>0:
                # Ahora compruebo qué vértice toca añadir y con quien se une

                v_añadido=listas[2][-1]
                del(listas[2][-1])

                # Añado las aristas correspondientes al nuevo vertice

                for i in listas[1][-1]:
                    gg.añadir_arista(v_añadido,i)

                del(listas[1][-1])

            return gg
        
        else:
            return ValueError, 'La secuencia no es grafica.'