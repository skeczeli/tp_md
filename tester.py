from graph import AdjacencyListGraph, Vertex
g = AdjacencyListGraph()
A = Vertex('A', True)
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')
H = Vertex('H')
I = Vertex('I')
J = Vertex('J')
K = Vertex('K')
L = Vertex('L')
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
g.add_vertex(K)
g.add_vertex(L)
g.add_edge(A, B)
#g.add_edge(A, D) #ciclo
g.add_edge(B, C)
g.add_edge(B, D)
g.add_edge(D, E)
g.add_edge(E, F)
g.add_edge(F, G)
g.add_edge(F, H)
g.add_edge(H, I)
g.add_edge(I, K)
g.add_edge(I, J)
g.add_edge(I, L)
puentes = g.get_bridges()
print(puentes)
puente_1 = puentes[-4]
user = F
print(g.get_bridges_and_impacts(user)[1])