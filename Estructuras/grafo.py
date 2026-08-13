class Grafo:
    """Implementación de un grafo no dirigido."""

    def __init__(self):
        self._adjacency_list = {}

    def _normalize_vertex(self, vertex):
        return str(vertex).strip().upper()

    def add_vertex(self, vertex):
        vertex = self._normalize_vertex(vertex)
        if not vertex:
            raise ValueError("El nombre del vértice no puede estar vacío.")
        if vertex in self._adjacency_list:
            return False
        self._adjacency_list[vertex] = []
        return True

    def remove_vertex(self, vertex):
        vertex = self._normalize_vertex(vertex)
        if vertex not in self._adjacency_list:
            return False
        adjacent_vertices = list(self._adjacency_list[vertex])
        for adjacent_vertex in adjacent_vertices:
            self._adjacency_list[adjacent_vertex].remove(vertex)
        del self._adjacency_list[vertex]
        return True

    def add_edge(self, vertex1, vertex2):
        vertex1 = self._normalize_vertex(vertex1)
        vertex2 = self._normalize_vertex(vertex2)
        if vertex1 not in self._adjacency_list:
            raise ValueError(f"El vértice {vertex1} no existe.")
        if vertex2 not in self._adjacency_list:
            raise ValueError(f"El vértice {vertex2} no existe.")
        if vertex1 == vertex2:
            raise ValueError("No se permite conectar un vértice consigo mismo.")
        if vertex2 in self._adjacency_list[vertex1]:
            return False
        self._adjacency_list[vertex1].append(vertex2)
        self._adjacency_list[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1, vertex2):
        vertex1 = self._normalize_vertex(vertex1)
        vertex2 = self._normalize_vertex(vertex2)
        if vertex1 not in self._adjacency_list:
            return False
        if vertex2 not in self._adjacency_list:
            return False
        if vertex2 not in self._adjacency_list[vertex1]:
            return False
        self._adjacency_list[vertex1].remove(vertex2)
        self._adjacency_list[vertex2].remove(vertex1)
        return True

    def contains_vertex(self, vertex):
        vertex = self._normalize_vertex(vertex)
        return vertex in self._adjacency_list

    def contains_edge(self, vertex1, vertex2):
        vertex1 = self._normalize_vertex(vertex1)
        vertex2 = self._normalize_vertex(vertex2)
        if vertex1 not in self._adjacency_list:
            return False
        return vertex2 in self._adjacency_list[vertex1]

    def get_vertices(self):
        return sorted(self._adjacency_list.keys())

    def get_adjacent_vertices(self, vertex):
        vertex = self._normalize_vertex(vertex)
        if vertex not in self._adjacency_list:
            raise ValueError(f"El vértice {vertex} no existe.")
        return sorted(self._adjacency_list[vertex])

    def get_adjacency_list(self):
        result = {}
        for vertex in self.get_vertices():
            result[vertex] = self.get_adjacent_vertices(vertex)
        return result

    def get_adjacency_matrix(self):
        vertices = self.get_vertices()
        matrix = []
        for row_vertex in vertices:
            row = []
            for column_vertex in vertices:
                row.append(1 if self.contains_edge(row_vertex, column_vertex) else 0)
            matrix.append(row)
        return vertices, matrix

    def get_edges(self):
        edges = []
        registered_edges = set()
        for vertex1 in self.get_vertices():
            for vertex2 in self.get_adjacent_vertices(vertex1):
                edge = tuple(sorted((vertex1, vertex2)))
                if edge not in registered_edges:
                    registered_edges.add(edge)
                    edges.append(edge)
        return sorted(edges)

    def vertex_count(self):
        return len(self._adjacency_list)

    def edge_count(self):
        return len(self.get_edges())

    def clear(self):
        self._adjacency_list.clear()

    def is_empty(self):
        return self.vertex_count() == 0