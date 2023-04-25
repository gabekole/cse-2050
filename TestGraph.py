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
        """ADD DOCSTRING"""
        shortest_path_tree_1, distance_tree_1 = self.g.fewest_connections('C', 'D')
        self.assertEqual({'C': None, 'D': 'C'}, shortest_path_tree_1)

        shortest_path_tree_2, distance_tree_2 = self.g.fewest_connections('C', 'A')
        self.assertEqual(3, len(shortest_path_tree_2))

        shortest_path_tree_3, distance_tree_3 = self.g.fewest_connections('B', 'D')
        self.assertEqual(2, len(shortest_path_tree_3))
 

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_shortest_path(self):
        """ADD DOCSTRING"""

    # TODO: Which alg do you use here, and why?
    # Alg:
    # Why:
    def test_minimum_salt(self):
        """ADD DOCSTRING"""

unittest.main()