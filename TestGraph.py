from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """
        
              200         40
        A ---------- B -------- C
        |       ____/           |
    200 |   __/ 140             |
        | /                     |
        D ----------------------
                          150
        
        
        """

        vertices = {'A', 'B', 'C', 'D'}
        edges = ('A', 'B', 200), ('B', 'C', 40), ('C', 'D', 150), ('A', 'D', 200), ('B', 'D', 140)

        self.g = Graph(vertices, edges)

    def test_add_vertex(self):
        start_length = len(self.g)

        self.g.add_vertex('E')

        self.assertEqual(len(self.g), start_length + 1)

    def test_nbrs(self):
        expected_neighbors_1 = dict()
        expected_neighbors_1['B'] = 40
        expected_neighbors_1['D'] = 150

        self.assertEqual(self.g.nbrs('C'), expected_neighbors_1)

        expected_neighbors_2 = dict()
        expected_neighbors_2['A'] = 200
        expected_neighbors_2['D'] = 140
        expected_neighbors_2['C'] = 40

        self.assertEqual(self.g.nbrs('B'), expected_neighbors_2)

        expected_neighbors_3 = dict()
        expected_neighbors_3['B'] = 200
        expected_neighbors_3['D'] = 200

        self.assertEqual(self.g.nbrs('A'), expected_neighbors_3)

        expected_neighbors_4 = dict()
        expected_neighbors_4['C'] = 150
        expected_neighbors_4['B'] = 140
        expected_neighbors_4['A'] = 200

        self.assertEqual(self.g.nbrs('D'), expected_neighbors_4)

    def test_edge_addition(self):
        self.g.add_edge('B', 'D', 20)

        expected_neighbors_1 = dict()
        expected_neighbors_1['C'] = 150
        expected_neighbors_1['B'] = 20
        expected_neighbors_1['A'] = 200

        self.assertEqual(self.g.nbrs('D'), expected_neighbors_1)

        self.g.add_edge('C', 'A', 100)
        
        expected_neighbors_2 = dict()
        expected_neighbors_2['B'] = 200
        expected_neighbors_2['D'] = 200
        expected_neighbors_2['C'] = 100


        self.assertEqual(self.g.nbrs('A'), expected_neighbors_2)

    def test_edge_removal(self):

        self.assertRaises(KeyError, lambda : self.g.remove_edge('B', 'A', 100))
        self.assertRaises(KeyError, lambda : self.g.remove_edge('E', 'A', 100))
        self.assertRaises(KeyError, lambda : self.g.remove_edge('N', 'A'))

        self.g.remove_edge('B', 'A')

        expected_neighbors_1 = dict()
        expected_neighbors_1['D'] = 200
        self.assertEqual(self.g.nbrs('A'), expected_neighbors_1)

        self.assertRaises(KeyError, lambda : self.g.remove_edge('A', 'B'))

        self.g.remove_edge('D', 'A')
        self.assertEqual(self.g.nbrs('A'), dict())


    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """
        
              200         40
        A ---------- B -------- C
        |       ____/           |
    200 |   __/ 140             |
        | /                     |
        D ----------------------
                          150
        
        
        """

        vertices = {'A', 'B', 'C', 'D'}
        edges = ('A', 'B', 200), ('B', 'C', 40), ('C', 'D', 150), ('A', 'D', 200), ('B', 'D', 140)

        self.g = Graph(vertices, edges)

    # Alg: Breadth first search
    # Why: Since we don't care about the weighting on each edge, and we want the fastest connection, 
    #    Breath first search works well in this case.
    def test_fewest_flights(self):
        """
        Tests that the `fewest_connections` method works properly in the graph class
        """
        fewest_connections_tree_1, distance_tree_1 = self.g.fewest_connections('C')
        self.assertEqual(fewest_connections_tree_1, {'C': None, 'B': 'C', 'D': 'C', 'A': 'B'})
        self.assertEqual(distance_tree_1, {'C': 0, 'B': 40, 'D': 150, 'A': 240})

        fewest_connections_tree_2, distance_tree_2 = self.g.fewest_connections('D')
        self.assertEqual(fewest_connections_tree_2, {'D': None, 'C': 'D', 'A': 'D', 'B': 'D'} )
        self.assertEqual(distance_tree_2, {'D': 0, 'C': 150, 'A': 200, 'B': 140})

    
    # Alg: Dijkstra's algorithm
    # Why: We want the shortest paths in a weighted graph, this is what dijkstra is for
    def test_shortest_path(self):
        """
        Tests that the shortest path method works properly
        """
        traversal_map_1, distance_tree_1 = self.g.shortest_path('C')

        self.assertEqual(traversal_map_1, {'C': None, 'B': 'C', 'D': 'C', 'A': 'B'})
        self.assertEqual(distance_tree_1, {'B': 40, 'A': 240, 'D': 150, 'C': 0})

        traversal_map_2, distance_tree_2 = self.g.shortest_path('A')
        self.assertEqual(traversal_map_2, {'A': None, 'B': 'A', 'D': 'A', 'C': 'B'})
        self.assertEqual(distance_tree_2, {'B': 200, 'D': 200, 'C': 240, 'A': 0})

        traversal_map_3, distance_tree_3 = self.g.shortest_path('B')
        self.assertEqual(traversal_map_3, {'B': None, 'A': 'B', 'C': 'B', 'D': 'B'})
        self.assertEqual(distance_tree_3, {'C': 40, 'A': 200, 'B': 0, 'D': 140})


    # Alg: Prims Algorithm
    # Why: Because it is designed to create a minimum spanning tree which is what this case is all about
    def test_minimum_salt(self):
        """
        Tests that the shortest_total_path method works properly
        """
        traversal_map_1, edge_map_1 = self.g.shortest_total_path('C')

        self.assertEqual(traversal_map_1, {'C': None, 'B': 'C', 'D': 'B', 'A': 'B'})
        self.assertEqual(edge_map_1, {'B': 40, 'A': 200, 'C': 0, 'D': 140})

        traversal_map_2, edge_map_2 = self.g.shortest_total_path('A')
        self.assertEqual(traversal_map_2, {'A': None, 'B': 'C', 'D': 'B', 'C': 'B'})
        self.assertEqual(edge_map_2, {'A': 0, 'D': 140, 'B': 40, 'C': 40})

        traversal_map_3, edge_map_3 = self.g.shortest_total_path('B')
        self.assertEqual(traversal_map_3, {'B': None, 'A': 'B', 'C': 'B', 'D': 'B'})
        self.assertEqual(edge_map_3, {'C': 40, 'A': 200, 'D': 140, 'B': 0})

unittest.main()