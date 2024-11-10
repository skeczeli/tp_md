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
g.add_vertex(J) #Isolated vertex

g.add_edge(A, B)
g.add_edge(A, C)
g.add_edge(B, C)
g.add_edge(B, D)
g.add_edge(D, F)
g.add_edge(C, E)
g.add_edge(A, G)
g.add_edge(A, H)
g.add_edge(G, H)
g.add_edge(G, I)
g.add_edge(H, J)


print(g.connected_components(A))