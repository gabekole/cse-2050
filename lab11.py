class Graph_AS:
    def __init__(self, verticies, edges):
        self._AS = dict()
        
        for vert in verticies:

            adjacent_to = set()

            for edge in edges:
                if edge[0] == vert:
                    adjacent_to.add(edge[1])
            
            self._AS[vert] = adjacent_to


    def __len__(self):
        return len(self._AS)

    def __iter__(self):
        return iter(self._AS)

    def __contains__(self, object):
        return object in self._AS

    def add_vertex(self, v):
        self._AS[v] = set()

    def add_edge(self, e):
        origin = e[0]
        end = e[1]

        self._AS[origin].add(end)

    def remove_vertex(self, v):
        if v not in self:
            raise KeyError("Vertex not in graph")

        del self._AS[v]

        for adjacency_set in self._AS.values():
            adjacency_set.remove(v)

    def remove_edge(self, e):
        if e[0] not in self._AS or e[1] not in self._AS[e[0]]:
            raise KeyError("Edge not in graph")

        self._AS[e[0]].remove(e[1])

    def _neighbors(self, v):

        return self._AS[v]
    












class Graph_ES:
    def __init__(self, verticies, edges):
        self.verticies = verticies
        self.edges = edges

    def __len__(self):
        return len(self.verticies)

    def __iter__(self):
        return iter(self.verticies)

    def __contains__(self, object):
        return object in self.verticies

    def add_vertex(self, v):
        self.verticies.add(v)

    def add_edge(self, e):
        self.edges.add(e)

    def remove_vertex(self, v):
        if v not in self:
            raise KeyError("Vertex not in graph")

        relevant_edges = [] # Keep track of all edges connected to vertex

        for edge in self.edges:
            if v in edge:
                relevant_edges.append(edge)

        self.verticies.remove(v)

        for edge in relevant_edges:
            self.edges.remove(edge)

    def remove_edge(self, e):
        if e not in self.edges:
            raise KeyError("Edge not in graph")

        self.edges.remove(e)

    
    def _neighbors(self, v):

        neighbors = set()

        for edge in self.edges:
            if v != edge[0]:
                continue
            neighbors.add(edge[1])

        return neighbors