import random
import networkx as nx
from matplotlib import pyplot as plt
from graph import AdjacencyListGraph, Vertex

def create_sparse_graph(graph, num_vertices, num_edges):
    random.seed(85)
    vertices = [Vertex(user=i) for i in range(num_vertices)]

    for v in vertices:
        graph.add_vertex(v)
    while graph._edge_count < num_edges:
        u, v = random.sample(vertices, 2)
        graph.add_edge(u, v)
    return graph, vertices

# Crear grafos dispersos de 10, 100 y 500 vértices
graph_10, vertices_10 = create_sparse_graph(AdjacencyListGraph(), 10, 8)
graph_100, vertices_100 = create_sparse_graph(AdjacencyListGraph(), 100, 50)
graph_500, vertices_500 = create_sparse_graph(AdjacencyListGraph(), 500, 300)

def visualize_graph(graph, vertices, title):
    G = nx.Graph()
    G.add_nodes_from([v.user for v in vertices])
    for v in vertices:
        for neighbor in graph.adjacency_list[v]:
            G.add_edge(v.user, neighbor.user)
    
    plt.figure(figsize=(8, 8))
    nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray", node_size=500, font_size=10)
    plt.title(title)
    plt.show()

# Visualizar grafos dispersos
visualize_graph(graph_10, vertices_10, "Sparse Graph with 10 Vertices")