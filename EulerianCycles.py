import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
# nxpdParams['show'] = 'ipynb'

#G = nx.DiGraph([('f', 'e'), ('d', 'c'), ('a', 'b'), ('c', 'd'), ('c', 'f'), ('f', 'd'), ('b', 'a'), ('a', 'd'), ('d', 'a'), ('e', 'a'), ('b', 'f'), ('a', 'c'), ('d', 'b')])
G = nx.DiGraph([('a', 'b'), ('b', 'c'), ('c', 'e'), ('e', 'a'), ('a', 'd'), ('d', 'c'), ('c', 'a')])
draw(G, layout='circo')

if nx.is_eulerian(G):
    cycle = nx.eulerian_circuit(G)
    
    edge_number = 1
    for e in cycle:
        G[e[0]][e[1]]['label'] = str(edge_number)
        edge_number += 1
else:
    print("There is no Eulerian cycle in this graph")

draw(G, layout='circo')