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
        Adds an edge to the graph with the provided weight
        if the same edge pairing already exhists, the weight will be overrided
        with the new weight

        Must be added twice since adjacency map is bidirectional
        """

        if u not in self.adjacency_map:
            self.adjacency_map[u] = dict()

        if v not in self.adjacency_map:
            self.adjacency_map[v] = dict()

        self.adjacency_map[u][v] = wt
        self.adjacency_map[v][u] = wt


    def remove_edge(self, u, v, wt=None):
        """
        Removes an edge from the graph and raises a KeyError
        if it does not exist

        If weight is None, will attempt to remove the edge

        If weight is not None, will check that the edge has the provided weight and 
        will through a KeyError if not 
        """

        if u not in self.adjacency_map:
            raise KeyError(f"Vertex not in graph: {u}")
        if v not in self.adjacency_map:
            raise KeyError(f"Vertex not in graph: {v}")

        if u not in self.adjacency_map[v]:
            raise KeyError(f"Edge not in graph: {v}, {u}")
        if v not in self.adjacency_map[u]:
            raise KeyError(f"Edge not in graph: {u}, {v}")

        if wt is not None and self.adjacency_map[u][v] != wt:
            raise KeyError(f"Edge does not match provided weight: {wt}")

        if wt is not None and self.adjacency_map[v][u] != wt:
            raise KeyError(f"Edge does not match provided weight: {wt}")

        del self.adjacency_map[u][v]
        del self.adjacency_map[v][u]


    def nbrs(self, v):
        """
        Returns the neighbors of a given vertex
        """

        return self.adjacency_map[v]

    def __len__(self):
        """
        Returns length as the number of vertices in the graph
        """
        return len(self.adjacency_map)
    
    def fewest_connections(self, origin_node):
        """
        Generates a dictionary tree based on the fewest number of jumps in the tree

        Finds how to get from `origin_node` to any other node in the fewest number of graph "jumps"
        Uses breadth first search

        Returns: A dictionary-tree showing traversal order and a dictionary of vertex: cost.
        """
        traversal_tree = dict() # empty dict for child:parent
        node_queue = [(None, origin_node)] # (parent, child) tuples we want to explore
        cost_tree = {}

        while node_queue: # Loop while the queue is not empty
            parent, child = node_queue.pop(0) # Get first in node
            if child in traversal_tree: # Skip if already visited
                continue
            traversal_tree[child] = parent # store parent : child
            if parent is None:
                cost_tree[child] = 0
            else:
                cost_tree[child] = self.adjacency_map[parent][child] + cost_tree[parent]

            for node in self.nbrs(child):
                node_queue.append((child, node)) # add all of b's neighbors to node_queue
            
        return traversal_tree, cost_tree

