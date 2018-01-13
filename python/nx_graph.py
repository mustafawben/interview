"""
Use a standard graph analysis library such as NetworkX to compute the betweeness
centrality of the nodes.

 - https://networkx.github.io/documentation/stable/reference/index.html
"""

relationships = [
    {"parent": "alice", "child": "bob"},
    {"parent": "bob", "child": "charlie"},
    {"parent": "dean", "child": "edgar"}
]

import networkx as nx

G = nx.Graph()
edge_list = [("alice","bob") , ("bob", "charlie") , ("dean", "edgar")]
G.add_edges_from(edge_list)
print ("Betweenness Centrality: ", nx.betweenness_centrality(G))

# TODO: build a graph, compute the betweeness centrality
