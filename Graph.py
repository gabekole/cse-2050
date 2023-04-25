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
    
    def fewest_connections(self, origin_node, destination_node):
        """
        Attempts to find the path with the fewest connections to the provided `destination_node` from 
        `origin_node`

        Finds how to get from `origin_node` to `destination_node` in the fewest number of graph "jumps"
        Uses breadth first search

        Returns: A dictionary-tree showing traversal order
        """

        path_queue = []
        path_queue.append([origin_node]) # Initialze the queue with the first path

        
        while path_queue: # Looop while the queue is not empty
            path = path_queue.pop(0) # Get the first path from the queue
            last_node = path[-1] # Get the last node in the path (leaf)
            
            if last_node == destination_node: # Path ends at the destination

                dictionary_path = dict() # Initialize a dictionary path to generate from the list path
                first_node = path[0] # Special case of first node must be accounted for

                dictionary_path[first_node] = None

                for previous, current in zip(path, path[1:]):
                    dictionary_path[current] = previous


                dictionary_distance = dict()
                dictionary_distance[first_node] = 0

                for previous, current in zip(path, path[1:]):
                    dictionary_distance[current] = self.adjacency_map[previous][current] + dictionary_distance[previous]
                    

                return dictionary_path, dictionary_distance
            

            for adjacent in self.nbrs(last_node): # Create a new path for each neighbor and add to queue
                new_path = list(path)
                new_path.append(adjacent)
                path_queue.append(new_path)

        raise ValueError(f'No path from {origin_node} to {destination_node}')

