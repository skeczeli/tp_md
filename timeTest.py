import random
import timeit
from graph import AdjacencyListGraph, Vertex

def create_sparse_graph(graph, num_vertices, num_edges):
    vertices = [Vertex(user=i) for i in range(num_vertices)]

    for v in vertices:
        graph.add_vertex(v)
    while graph._edge_count < num_edges:
        u, v = random.sample(vertices, 2)
        graph.add_edge(u, v)
    return graph

# Crear grafos dispersos de 10, 100 y 500 vertices
graph_10 = create_sparse_graph(AdjacencyListGraph(), 10, 8)
graph_100 = create_sparse_graph(AdjacencyListGraph(), 100, 50)
graph_1000 = create_sparse_graph(AdjacencyListGraph(), 1000, 500)

# Medir tiempo para encontrar caminos más cortos
def shortest_path_time(grafo, size):
    tiempo_total = 0
    ejecuciones = 1000
    
    for a in range(ejecuciones):
        # Generar un par aleatorio de nodos entre 0 y size-1
        nodo_inicio = random.randint(0, size-1)
        nodo_destino = random.randint(0, size-1)
        
        # Evitar que el nodo de inicio sea el mismo que el de destino
        while nodo_inicio == nodo_destino:
            nodo_destino = random.randint(0, size-1)
        
        # Medir el tiempo de ejecución para encontrar el camino más corto
        tiempo_ejecucion = timeit.timeit(lambda: grafo.shortest_path(nodo_inicio, nodo_destino), number=1)
        tiempo_total += tiempo_ejecucion
    
    tiempo_promedio = tiempo_total / ejecuciones
    print(f"Tiempo promedio para {ejecuciones} ejecuciones de {size} nodos: {tiempo_promedio} segundos")

# Medir tiempo para obtener puentes e impactos
def bridges_and_impacts_time(grafo, size):
    tiempo_total = 0
    ejecuciones = 1000
    
    for a in range(ejecuciones):
        # Seleccionar un nodo aleatorio como nodo de inicio
        nodo_inicio = random.choice(list(grafo.adjacency_list.keys()))  # Obtener un vértice aleatorio de la lista de vértices
        
        # Medir el tiempo de ejecución para obtener los puentes e impactos
        tiempo_ejecucion = timeit.timeit(lambda: grafo.get_bridges_and_impacts(nodo_inicio), number=1)
        tiempo_total += tiempo_ejecucion
    
    tiempo_promedio = tiempo_total / ejecuciones
    print(f"Tiempo promedio para {ejecuciones} ejecuciones de {size} nodos: {tiempo_promedio} segundos")


def connected_components_time(grafo, size):
    tiempo_total = 0
    ejecuciones = 1000
    
    for a in range(ejecuciones):
        # Seleccionar un nodo aleatorio como nodo de inicio
        nodo_inicio = random.choice(list(grafo.adjacency_list.keys()))  # Obtener un vértice aleatorio de la lista de vértices
        
        # Medir el tiempo de ejecución para obtener las componentes conexas
        tiempo_ejecucion = timeit.timeit(lambda: grafo.connected_components(nodo_inicio), number=1)
        tiempo_total += tiempo_ejecucion
    
    tiempo_promedio = tiempo_total / ejecuciones
    print(f"Tiempo promedio para {ejecuciones} ejecuciones de {size} nodos: {tiempo_promedio} segundos")


# Medir el tiempo para cada grafo
print("\nMedición de tiempo para grafo de 10 vértices - Caminos más cortos:")
shortest_path_time(graph_10, 10)

print("\nMedición de tiempo para grafo de 100 vértices - Caminos más cortos:")
shortest_path_time(graph_100, 100)

print("\nMedición de tiempo para grafo de 1000 vértices - Caminos más cortos:")
shortest_path_time(graph_1000, 1000)

print("\nMedición de tiempo para grafo de 10 vértices - Puentes e Impactos:")
bridges_and_impacts_time(graph_10, 10)

print("\nMedición de tiempo para grafo de 100 vértices - Puentes e Impactos:")
bridges_and_impacts_time(graph_100, 100)

print("\nMedición de tiempo para grafo de 1000 vértices - Puentes e Impactos:")
bridges_and_impacts_time(graph_1000, 1000)

print("\nMedición del tiempo de ejecución para encontrar puentes e impactos en un grafo de 10 vértices:")
connected_components_time(graph_10, 10)

print("\nMedición del tiempo de ejecución para encontrar puentes e impactos en un grafo de 100 vértices:")
connected_components_time(graph_100, 100)

print("\nMedición del tiempo de ejecución para encontrar puentes e impactos en un grafo de 1000 vértices:")
connected_components_time(graph_1000, 1000)