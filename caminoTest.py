from graph import AdjacencyListGraph 
g = AdjacencyListGraph()
g.add_vertex('A', True)
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')
g.add_vertex('G')
g.add_vertex('H')
g.add_vertex('I')
g.add_vertex('J')
g.add_vertex('K')
g.add_vertex('L')
g.add_edge('B', 'A')
#g.add_edge('A', 'D') #ciclo
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('D', 'E')
g.add_edge('E', 'F')
g.add_edge('F', 'G')
g.add_edge('F', 'H')
g.add_edge('H', 'I')
g.add_edge('I', 'K')
g.add_edge('I', 'J')
g.add_edge('I', 'L')

# Encuentra el camino más corto entre 'A' y 'D'
print(g.shortest_path('A', 'E'))  # Posible salida: ['A', 'B', 'C', 'D']