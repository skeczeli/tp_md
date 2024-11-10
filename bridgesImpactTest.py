from graph import AdjacencyListGraph, Vertex
g = AdjacencyListGraph()
A = Vertex('A', True)
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
g.add_vertex(A)
g.add_vertex(B)
g.add_vertex(C)
g.add_vertex(D)
g.add_edge(A, B)
g.add_edge(B, C)
g.add_edge(A, C)
g.add_edge(C, D)



print(g.get_bridges_and_impacts(A))