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

    # Camino más corto entre dos usuarios
    def shortest_path(self, start, end):
            if start not in self.adjacency_list or end not in self.adjacency_list:
                return None

            visited = set()
            queue = deque([(start, [start])])

            while len(queue) > 0:
                current, path = queue.popleft()
                visited.add(current)

                if current == end:
                    return path

                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)

            return None 

    # Impacto sobre los usuarios críticos de perder un usuario en la red
    def connected_components(self, user):
        components = []
        visited = set()
        vertex_amount = 1
        visited.add(user)  
        def dfs(u, visited, component, excluded_edges):
            component[0] += 1
            visited.add(u)
            if u.is_critical: component.append(u)
            for v in self.get_adjacency_list(u):
                if v not in visited and (u, v) not in excluded_edges and (v, u) not in excluded_edges:
                    dfs(v, visited, component, excluded_edges)

        for neighbour in self.get_adjacency_list(user):
            if neighbour in visited:
                continue
            component = []
            component.append(0)
            dfs(neighbour, visited, component, self.get_adjacency_list(user))
            components.append(component)
            vertex_amount += component[0]

        for list in components:
            list[0] = f'{((vertex_amount - list[0]) / vertex_amount) * 100}%'

        return components


    # Conexiones críticas (puentes) e impacto sobre un usuario dado de perder cada una
    def get_connected_component(self, start_node):
        visited = set()
        def dfs(u):
            visited.add(u)
            for v in self.get_adjacency_list(u):
                if v not in visited:
                    dfs(v)
        dfs(start_node)
        return visited

    def get_bridges_and_impacts(self, start_node):
        connected_component = self.get_connected_component(start_node)
        depth = 0
        disc = {v: -1 for v in self.adjacency_list}
        low = {v: -1 for v in self.adjacency_list}
        parents = {v: None for v in self.adjacency_list}
        bridges = []
        impacts = {}

        total_nodes = len(connected_component)
        if total_nodes == 1: return [], {} 
        def dfs(u):
            nonlocal depth
            disc[u] = low[u] = depth
            depth += 1
            subtree_size = 1
            for v in self.get_adjacency_list(u):
                if disc[v] == -1:
                    parents[v] = u
                    child_subtree_size = dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((u, v))
                        impacts[(u, v)] = (child_subtree_size / total_nodes)*100

                    subtree_size += child_subtree_size

                elif v != parents[u]:
                    low[u] = min(low[u], disc[v])
            return subtree_size

        dfs(start_node)

        return bridges, impacts # Permite usar los puentes por separado, o tenerlos en relación a su impacto para el usuario
    
    # Método alternativo para conseguir puentes (mejor si no se busca conseguir el impacto sobre un usuario)
    def get_bridges(self):
        depth = 0
        disc = {v: -1 for v in self.adjacency_list}
        low = {v: -1 for v in self.adjacency_list}
        parents = {v: None for v in self.adjacency_list}
        bridges = []

        def dfs(u):
            nonlocal depth
            disc[u] = low[u] = depth
            depth += 1
            for v in self.get_adjacency_list(u):
                if disc[v] == -1:
                    parents[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        bridges.append((u, v))
            
                elif v != parents[u]:
                    low[u] = min(low[u], disc[v])

        for vertex in self.adjacency_list:
            if disc[vertex] == -1:
                dfs(vertex)

        return bridges