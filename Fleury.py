from grafos import *
import tempfile

def Fleury(g, explicado=False):
    
    def vertice_inicial(g):
    
        l=g.vertices

        if g.es_euleriano()==1:
            v=l[0]
            return v
        elif g.es_euleriano()==2:
            v = [i[0] for i in g.grados() if i[1]%2!=0][0]
            return v
        else:
            return -1
            
    if vertice_inicial(g)==-1:
        return False
    
    elif explicado:
        gg=deepcopy(g)
        textos=[]
        E=[]
        v_inic=vertice_inicial(gg)
        V=[v_inic]
        verts=gg.vertices
        aris=gg.aristas
        v_a=v_inic
        
        if g.es_euleriano()==1:
            s = 'Circuito '
        else:
            s = 'Camino '
        
        Circuito = [s + 'de Euler: []']

        while len(verts)>1:
            
            a_incidentes=gg.aristas_incidentes(v_a)  # Miro cuantas aristas salen del vertice
            
            if len(a_incidentes)==1:    # Si solo sale una arista, la cojo y cojo el otro extremo y los meto en V y E, y ya terminaría el while
                E.append(a_incidentes[0])
                gg.borrar_arista(a_incidentes[0][0], a_incidentes[0][1]) #Borro tanto la arista como el vértice
                mensaje='Eliminamos la airsta (' + str(a_incidentes[0][0]) + ',' + str(a_incidentes[0][1]) + ')' 
                textos.append(mensaje)  
                verts.remove(v_a)

                if a_incidentes[0][0]==v_a:
                    v_a=a_incidentes[0][1]
                    V.append(v_a)
                else:
                    v_a=a_incidentes[0][0]
                    V.append(v_a)
                    
                EE=deepcopy(V)
                Circuito.append(s + 'de Euler: ' + str(EE))

            else:
                parar=False
                i=0
                while parar==False and i<=len(a_incidentes):
                    gg.borrar_arista(a_incidentes[i][0], a_incidentes[i][1])

                    if gg.conexo():
                        E.append(a_incidentes[i]) 

                        if a_incidentes[i][0]==v_a:
                            V.append(a_incidentes[i][1])
                            v_a=a_incidentes[i][1]
                        else:
                            V.append(a_incidentes[i][0])
                            v_a=a_incidentes[i][0]
                            
                        mensaje='Eliminamos la airsta (' + str(a_incidentes[i][0]) + ',' + str(a_incidentes[i][1]) + ')'
                        textos.append(mensaje)
                        EE=deepcopy(V)
                        Circuito.append(s + 'de Euler: ' + str(EE))
                        parar=True
                    else:
                        gg.añadir_arista(a_incidentes[i][0], a_incidentes[i][1])
                        i = i+1 
        
        fout= fout = tempfile.NamedTemporaryFile()
        L=[g.dibujar('circo').render(fout.name+str('0'))]
        textos.insert(0, 'Grafo inicial')

        for i in range(1,len(textos)):
            L.append(g.resaltar_arista(E[0:i], {}, 'lightgrey', '3', 'circo').render(fout.name+str(i)))

        g.pasoapaso(L, textos, Circuito)
        
    else:        
        gg=deepcopy(g)
        E=[]
        v_inic=vertice_inicial(gg)
        V=[v_inic]
        verts=gg.vertices
        aris=gg.aristas
        v_a=v_inic

        while len(verts)>1:
            
            a_incidentes=gg.aristas_incidentes(v_a)  # Miro cuantas aristas salen del vertice
            
            if len(a_incidentes)==1:    # Si solo sale una arista, la cojo y cojo el otro extremo y los meto en V y E, y ya terminaría el while
                E.append(a_incidentes[0])
                gg.borrar_arista(a_incidentes[0][0], a_incidentes[0][1]) #Borro tanto la arista como el vértice
                verts.remove(v_a)

                if a_incidentes[0][0]==v_a:
                    v_a=a_incidentes[0][1]
                    V.append(v_a)
                else:
                    v_a=a_incidentes[0][0]
                    V.append(v_a)

            else:
                parar=False
                i=0
                while parar==False and i<=len(a_incidentes):
                    gg.borrar_arista(a_incidentes[i][0], a_incidentes[i][1])

                    if gg.conexo():
                        E.append(a_incidentes[i]) 

                        if a_incidentes[i][0]==v_a:
                            V.append(a_incidentes[i][1])
                            v_a=a_incidentes[i][1]
                        else:
                            V.append(a_incidentes[i][0])
                            v_a=a_incidentes[i][0]
                            
                        parar=True
                        
                    else:
                        gg.añadir_arista(a_incidentes[i][0], a_incidentes[i][1])
                        i = i+1 
        
        return V
            
