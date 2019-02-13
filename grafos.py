from copy import copy, deepcopy
from IPython.display import SVG, display, Image
import graphviz as gv
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
import math

class Grafo(object):
    
    def __init__(self, verts=[], aris=[]):   #Creo mi grafo y creo una lista de vertices y aristas vacia que voy a ir rellenando.
        self.vertices=copy(verts)
        self.aristas=copy(aris)
        self.dic_pesos={}
        #self.comp_conexas=[]

    def __repr__(self):  # ME FALLA AL DARME LA EXPLICACION, MIRAR POR EJEMPLO EL ALAGORITMO DE PRIM, ME PONE 0 VERTICES Y X LADOS
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
        else:
            return False
        
    def borrar_arista(self, u, v):
        if (u,v) in self.aristas:
            self.aristas.remove((u,v))
        elif (v,u) in self.aristas:
            self.aristas.remove((v,u))
        else:
            return False
    
    def aristas_incidentes(self, v):
        aristas_incidentes=[i for i in self.aristas if v in i]
        return aristas_incidentes
    
    def vecinos(self, v):     # Cojo las aristas incidentes en un vertice y añado a mi lista de vecinos los extremos de esas
        l=self.aristas_incidentes(v)   # aristas que no sean el vertice que estoy estudiando.
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
    
    """def componentes_conexas(self): # Quito todos los vertices aislados y lo que me queda es conexo.    
        
        l=self.vertices_aislados(self)
        vertices_copy=deepcopy(self.vertices)
        
        for i in l:
            self.comp_conexas.append([i])
            vertices_copy.remove(i)
        
        self.comp_conexas.append(vertices_copy)
        
        return self.comp_conexas"""
            
    def componentes_conexas(self): # Quito todos los vertices aislados y lo que me queda es conexo.    
        
        #try:
        #    return self.comp_conexas
        #except AttributeError:
        self.comp_conexas=[]
        c=[]
        v=deepcopy(self.vertices)
        a=deepcopy(self.aristas)
        # Primero quito vertices aislados

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
        
        l = [i[1] for i in self.grados() if i[1]%2==0]
        
        if len(l)==len(self.grados()):
            return True
        elif len(l)==len(self.grados())-2:
            return 2
        else:
            return False
    
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
    
    def ciclos(self):#Tengo que mejorarla porque me devuelve ciclos de longitud dos, tipo [1,2,1], entonces debo diferenciar
        L=[]         # si realmente hay aristas paralelas o es por no ser un grafo dirigido.
        for i in self.vertices:
            for j in self.vecinos(i):
                l=self.caminos_simples(j, i)
                for k in l:
                    k.insert(0,i)
                    L.append(k)
        return L
    
    def es_arbol(self):   #Ver que el tamaño es n-1 siendo n el orden
        
        if self.conexo() and len(self.aristas)==len(self.vertices)-1:
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

