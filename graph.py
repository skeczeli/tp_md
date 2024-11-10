from collections import deque
class Vertex:
    def __init__(self, user, is_critical=False):
        self.user = user
        self.is_critical = is_critical

    def __repr__(self):
        return f"{self.user}"
    
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.user == other.user
    
    def __hash__(self):
        return hash(self.user)

class AdjacencyListGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.critical_users = {}
        self._edge_count = 0

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
            if v.is_critical:
                self.critical_users[v] = v

    def delete_vertex(self, v):
        if v in self.adjacency_list:
            for adj_vertex in self.adjacency_list[v]:
                self.adjacency_list[adj_vertex].remove(v)
                self._edge_count -= 1
            del self.adjacency_list[v]
            del self.critical_users[v]
        else: raise Exception(f"No existe {v}")
    
    def add_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list:
            if v not in self.adjacency_list[u]:
                self.adjacency_list[u].append(v)
                self.adjacency_list[v].append(u)
                self._edge_count += 1

    def delete_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list:
            if v in self.adjacency_list[u]:
                self.adjacency_list[u].remove(v)
                self.adjacency_list[v].remove(u)
                self._edge_count -= 1
        else: raise Exception(f"No existe {(u, v)}")

    def exists_edge(self, u, v):
        return u in self.adjacency_list and v in self.adjacency_list[u]

    def order(self):
        return len(self.adjacency_list)

    def edge_count(self):
        return self._edge_count

    def get_vertex(self, v):
        return self.adjacency_list.get(v, None)

    def get_adjacency_list(self, v):
        return self.adjacency_list.get(v, []) 

    def __str__(self):
        return f"Adjacency List: {self.adjacency_list}\nEdge Count: {self._edge_count}"
    
    def get_bridges(self):
        depth = 0
        disc = {v: -1 for v in self.adjacency_list}  # Tiempo de descubrimiento de cada vértice
        low = {v: -1 for v in self.adjacency_list}   # Menor profundidad alcanzable para cada vértice
        parents = {v: None for v in self.adjacency_list}  # Padres de cada vértice en la DFS
        bridges = []

        def dfs(u):
            nonlocal depth
            disc[u] = low[u] = depth
            depth += 1
            for v in self.get_adjacency_list(u):
                if disc[v] == -1:  # v no fue visitado
                    parents[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:  # Condición de puente
                        bridges.append((u, v))
            
                elif v != parents[u]:  # v es un vértice visitado y no es el padre de u
                    low[u] = min(low[u], disc[v])

        for vertex in self.adjacency_list:
            if disc[vertex] == -1:
                dfs(vertex)

        return bridges
    

    def bridge_impact(self, start, edge, orden_puente=0, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        for neighbor in self.get_adjacency_list(start):
            if neighbor not in visited:
                if (start, neighbor) == edge or (neighbor, start) == edge:
                    # Contar nodos alcanzables sin usar la arista 'edge'
                    orden_puente += self.counter_dfs(neighbor, start)
                else:
                    # Continuar la DFS normalmente
                    orden_puente = self.bridge_impact(neighbor, edge, orden_puente, visited)[1]
        
        return (len(visited), orden_puente)

    def counter_dfs(self, start, v, counter=0, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        # Iniciar el contador en 1 para contar el nodo actual
        total_counter = 1

        for neighbor in self.get_adjacency_list(start):
            if neighbor not in visited and neighbor != v:
                # Acumular el total de nodos alcanzables desde este nodo
                total_counter += self.counter_dfs(neighbor, v, counter, visited)
        
        return total_counter
    

    # alternativa que debería ser más eficiente:
    def get_connected_component(self, start_node):
        visited = set()
        def dfs(u):
            visited.add(u)
            for v in self.get_adjacency_list(u):
                if v not in visited:
                    dfs(v)
        dfs(start_node)
        return visited

    def get_bridges_and_impacts(self, start_node): #Busca los puentes para la componente del start_node
        connected_component = self.get_connected_component(start_node)
        depth = 0
        disc = {v: -1 for v in self.adjacency_list}  # Discovery time of each vertex
        low = {v: -1 for v in self.adjacency_list}   # Lowest discovery time reachable
        parents = {v: None for v in self.adjacency_list}  # Parents of each vertex in DFS
        bridges = []
        impacts = {}  # Dictionary to store impact of each bridge

        total_nodes = len(connected_component)
        if total_nodes == 1: return [], {} 
        def dfs(u):
            nonlocal depth
            disc[u] = low[u] = depth
            depth += 1
            subtree_size = 1  # Include the current node
            for v in self.get_adjacency_list(u):
                if disc[v] == -1:
                    parents[v] = u
                    child_subtree_size = dfs(v)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        # (u, v) is a bridge
                        bridges.append((u, v))
                        # Impact is the size of the subtree rooted at v
                        impacts[(u, v)] = (child_subtree_size / total_nodes)*100

                    subtree_size += child_subtree_size

                elif v != parents[u]:
                    low[u] = min(low[u], disc[v])
            return subtree_size

        if disc[start_node] == -1:
            dfs(start_node)

        return bridges, impacts
    


    

    def shortest_path(self, start, end):
            if start not in self.adjacency_list or end not in self.adjacency_list:
                return None  # Retorna None si alguno de los nodos no existe


            visited = set()  # Conjunto para mantener los nodos visitados
            queue = deque([(start, [start])])  #Queue de BFS que almacena el nodo actual y el camino hasta él

            while len(queue) > 0:
                current, path = queue.popleft()
                visited.add(current)

                # Si encontramos el nodo final, devolvemos el camino
                if current == end:
                    return path

                # Explora los nodos adyacentes no visitados
                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)

            return None  # Retorna None si no hay camino entre los nodos
    

    def connected_components(self, user):
        components = []
        visited = set()  # Keep track of all visited nodes
        vertex_amount = 1
        visited.add(user)  
        def dfs(u, visited, component, excluded_edges):
            component[0] += 1
            visited.add(u)
            if u.is_critical:           # Mark the node as visited
                component.append(u)       # Add node to the current component
            for v in self.get_adjacency_list(u):
                # Check if the edge (u, v) or (v, u) is in the list of excluded edges
                if v not in visited and (u, v) not in excluded_edges and (v, u) not in excluded_edges:
                    dfs(v, visited, component, excluded_edges)

        # Iterate over neighbors to start DFS for each component
        for neighbour in self.get_adjacency_list(user):
            if neighbour in visited:
                continue
            component = []  # Stores nodes for the current connected component
            component.append(0)
            dfs(neighbour, visited, component, self.get_adjacency_list(user))
            components.append(component)
            vertex_amount += component[0]

        for list in components:
            list[0] = f'{((vertex_amount - list[0]) / vertex_amount) * 100}%'

        return components

