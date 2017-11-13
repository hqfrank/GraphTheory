import networkx as nx
from nxpd import draw
G = nx.cycle_graph(4, create_using=nx.DiGraph())
draw(G)