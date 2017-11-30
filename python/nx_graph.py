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

# TODO: build a graph, compute the betweeness centrality
