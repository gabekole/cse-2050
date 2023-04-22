class Graph:
    def __init__(self, V=(), E=()):
        """
        Intiailizes the graph with the given vertices and edges
        
        Verticies are any iterable while the edges are expected to be in the form
        (first_vertex, second_vertex, weight)

        Using edges in any other form has undefined behavior.
        """

        self.adjacency_map = {}

        """"
        Internal map is of the form
        
        {
            Vertex_n0: {Vertex_m0 : weight_m0, Vertex_m1 : weight_m1 ...}
            Vertex_j0: {Vertex_k0 : weight_k0, Vertex_k1 : weight_k1 ...}
            ...
        }
        """

        for vertex in V:
            neighbor_map = dict()
            for edge in E:
                if edge[0] == vertex:
                    neighbor_map[edge[1]] = edge[2]
                elif edge[1] == vertex:
                    neighbor_map[edge[0]] = edge[2]
            self.adjacency_map[vertex] = neighbor_map

        
    def __contains__(self, object):
        return object in self.adjacency_map
        
    def add_vertex(self, v):
        """
        Adds a vertex to the graph
        """

        if v in self.adjacency_map:
            raise KeyError(f"Vertex already in graph: {v}")

        self.adjacency_map[v] = dict()

    def remove_vertex(self, v):
        """
        Removes a vertex from the graph and all references to it 

        Time complexity scales linearly with the number of vertexes in the graph 
        since all edges must be checked for removal 
        """

        if v not in self:
            raise KeyError(f"Vertex not in map: {v}")

        del self.adjacency_map[v]

        for edges in self.adjacency_map.values():
            if v in edges:
                del edges[v]


    def add_edge(self, u, v, wt):
        """
        Adds an edge to the graph
        """

    def remove_edge(self, u, v, wt):
        """ADD DOCSTRING"""

    def nbrs(self, v):
        """ADD DOCSTRING"""