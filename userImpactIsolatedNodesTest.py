from graph import AdjacencyListGraph, Vertex
g = AdjacencyListGraph()

A = Vertex('A', True)
B = Vertex('B', True)
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')
H = Vertex('H')
I = Vertex('I')
J = Vertex('J')

g.add_vertex(A)
g.add_vertex(B)
g.add_vertex(C)
g.add_vertex(D)
g.add_vertex(E)
g.add_vertex(F)
g.add_vertex(G)
g.add_vertex(H)
g.add_vertex(I)
g.add_vertex(J)

g.add_edge(A, B)
g.add_edge(A, C)
g.add_edge(A, D)
g.add_edge(A, E)
g.add_edge(A, F)
g.add_edge(A, G)
g.add_edge(A, H)
g.add_edge(A, I)
g.add_edge(A, J)

print(g.connected_components(A))